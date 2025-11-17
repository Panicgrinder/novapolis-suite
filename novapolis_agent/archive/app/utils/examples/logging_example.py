"""Archived example: logging_example.py

Archivkopie der Beispielimplementation.
"""
from app.utils.convlog import create_log_record, log_turn


def beispiel_logging() -> None:
    messages = [
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Wie ist das Wetter heute?"},
    ]

    response = "Keine aktuellen Wetterdaten verfügbar."
    log_entry = create_log_record(messages=messages, response=response)
    log_turn(log_entry)


if __name__ == "__main__":
    beispiel_logging()
