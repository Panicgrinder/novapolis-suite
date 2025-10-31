"""Beispiel für die Verwendung der Konversationszusammenfassung."""

from app.utils.convlog import create_log_record
from app.utils.summarize import summarize_turn


def beispiel_zusammenfassung() -> None:
    messages = [
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Was sind die Hauptmerkmale von Python?"},
    ]

    response = (
        "Python ist eine vielseitige Programmiersprache mit zahlreichen Stärken.\n\n"
        "Zu den wichtigsten Merkmalen von Python gehören:\n"
        "1. Einfache Syntax und Lesbarkeit\n"
        "2. Dynamische Typisierung\n"
        "3. Große Standardbibliothek\n"
        "4. Plattformunabhängigkeit\n"
        "5. Starke Community und umfangreiche Bibliotheken wie NumPy, Pandas und TensorFlow\n\n"
        "Wichtig ist, dass Python besonders für Einsteiger geeignet ist, aber dennoch für komplexe Aufgaben verwendet werden kann."
        " Beachte, dass Python im Vergleich zu kompilierten Sprachen wie C++ etwas langsamer sein kann, aber dies wird durch die"
        " Entwicklungsgeschwindigkeit oft ausgeglichen."
    )

    summary_data = summarize_turn(messages, response)

    print("Zusammenfassung:", summary_data["summary"])
    print("\nSchlüsselpunkte:")
    for index, fact in enumerate(summary_data["keyfacts"], 1):
        print(f"{index}. {fact}")

    log_entry = create_log_record(
        messages=messages,
        response=response,
        summary=summary_data["summary"],
        labels={"topic": "programming", "language": "python"},
    )

    print("\nZusammenfassung erstellt und bereit zum Loggen.")
    _ = log_entry


if __name__ == "__main__":
    beispiel_zusammenfassung()
