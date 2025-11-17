"""Archived example: summary_example.py

Archivkopie der Beispielimplementation.
"""
from app.utils.convlog import create_log_record
from app.utils.summarize import summarize_turn


def beispiel_zusammenfassung() -> None:
    messages = [
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Was sind die Hauptmerkmale von Python?"},
    ]
    response = "Python ist eine vielseitige Sprache."
    summary = summarize_turn(messages, response)
    log_entry = create_log_record(messages=messages, response=response, summary=summary.get("summary"))
    _ = log_entry


if __name__ == "__main__":
    beispiel_zusammenfassung()
