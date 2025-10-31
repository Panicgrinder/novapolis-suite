"""Beispiel für die Verwendung des Konversationsloggings."""

from app.utils.convlog import create_log_record, log_turn


def beispiel_logging() -> None:
    messages = [
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Wie ist das Wetter heute?"},
    ]

    response = (
        "Ich habe keinen Zugriff auf aktuelle Wetterdaten. Bitte überprüfen Sie einen Wetterdienst für die aktuellsten "
        "Informationen."
    )

    log_entry = create_log_record(
        messages=messages,
        response=response,
        summary="Wetterfrage ohne Zugriff auf aktuelle Daten",
        labels={"category": "wetter", "context_needed": True},
    )

    log_turn(log_entry)
    print("Konversation wurde geloggt.")


if __name__ == "__main__":
    beispiel_logging()
