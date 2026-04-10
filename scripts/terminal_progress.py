#!/usr/bin/env python3
"""Helpers for visible terminal progress during long-running commands."""

from __future__ import annotations

import queue
import subprocess
import threading
import time
from collections.abc import Mapping, Sequence

DEFAULT_HEARTBEAT_SECONDS = 15.0
_SPINNER_FRAMES = "|/-\\"


def format_duration(seconds: float) -> str:
    total_seconds = max(0, int(seconds))
    minutes, seconds_part = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds_part:02d}"
    return f"{minutes:02d}:{seconds_part:02d}"


def build_progress_message(
    label: str,
    *,
    elapsed_seconds: float,
    line_count: int,
    idle_seconds: float,
    spinner_index: int,
) -> str:
    spinner = _SPINNER_FRAMES[spinner_index % len(_SPINNER_FRAMES)]
    return (
        f"[progress] {spinner} {label}: laeuft seit {format_duration(elapsed_seconds)}"
        f" | Ausgabezeilen={line_count}"
        f" | letzte Aktivitaet vor {format_duration(idle_seconds)}"
    )


def _reader_worker(
    stream,
    output_queue: queue.Queue[str],
) -> None:
    try:
        for line in iter(stream.readline, ""):
            output_queue.put(line)
    finally:
        stream.close()


def run_command_with_heartbeat(
    command: Sequence[str],
    *,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    label: str,
    heartbeat_seconds: float = DEFAULT_HEARTBEAT_SECONDS,
    encoding: str = "utf-8",
    errors: str = "replace",
    timeout: int | None = None,
    live_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    process = subprocess.Popen(
        list(command),
        cwd=cwd,
        env=dict(env) if env is not None else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding=encoding,
        errors=errors,
        bufsize=1,
    )
    if process.stdout is None:
        raise RuntimeError("stdout pipe for progress command is not available")

    output_queue: queue.Queue[str] = queue.Queue()
    reader = threading.Thread(
        target=_reader_worker,
        args=(process.stdout, output_queue),
        daemon=True,
    )
    reader.start()

    output_parts: list[str] = []
    line_count = 0
    spinner_index = 0
    start = time.monotonic()
    last_activity = start
    last_heartbeat = start

    def drain_queue() -> None:
        nonlocal line_count, last_activity
        while True:
            try:
                line = output_queue.get_nowait()
            except queue.Empty:
                return
            output_parts.append(line)
            line_count += 1
            last_activity = time.monotonic()
            if live_output:
                print(line, end="", flush=True)

    while True:
        drain_queue()
        return_code = process.poll()
        now = time.monotonic()

        if return_code is not None:
            break

        if timeout is not None and (now - start) >= timeout:
            process.kill()
            process.wait()
            reader.join(timeout=1.0)
            drain_queue()
            raise subprocess.TimeoutExpired(list(command), timeout, output="".join(output_parts))

        if (now - last_heartbeat) >= heartbeat_seconds:
            print(
                build_progress_message(
                    label,
                    elapsed_seconds=now - start,
                    line_count=line_count,
                    idle_seconds=now - last_activity,
                    spinner_index=spinner_index,
                ),
                flush=True,
            )
            spinner_index += 1
            last_heartbeat = now

        time.sleep(0.1)

    reader.join(timeout=1.0)
    drain_queue()
    output_text = "".join(output_parts)
    return subprocess.CompletedProcess(list(command), return_code, output_text)
