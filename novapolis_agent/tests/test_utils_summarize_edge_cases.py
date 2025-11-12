from __future__ import annotations

from app.utils.summarize import (
    create_simple_summary,
    extract_key_points,
    llm_summarize,
    summarize_turn,
)


def test_extract_key_points_empty_and_markers() -> None:
    assert extract_key_points("") == []
    text = "Wichtig ist, dass wir testen. Daher folgt ein Ergebnis. Und noch ein Satz."
    pts = extract_key_points(text, max_points=3)
    assert len(pts) >= 2
    assert any("wichtig" in p.lower() for p in pts)
    assert any("daher" in p.lower() for p in pts)


def test_extract_key_points_fallback_uses_longest_sentences() -> None:
    text = "Kurz. Dies ist ein deutlich längerer Satz ohne Marker, der aufgenommen werden soll. Noch einer."
    pts = extract_key_points(text, max_points=2)
    assert len(pts) == 2
    assert any("längerer Satz" in p for p in pts)


def test_create_simple_summary_truncation() -> None:
    msgs = [{"role": "user", "content": "x" * 200}]
    resp = "y" * 300
    s = create_simple_summary(msgs, resp)
    assert "..." in s  # Trunkierung aktiv
    assert "Nutzer fragte nach" in s and "Antwort:" in s


def test_summarize_turn_heuristic() -> None:
    msgs = [{"role": "user", "content": "Bitte fasse zusammen."}]
    resp = "Zusammenfassend ist wichtig, dass Tests stabil sind."
    out = summarize_turn(msgs, resp)
    assert isinstance(out.get("summary"), str)
    assert isinstance(out.get("keyfacts"), list)


def test_summarize_turn_llm_path() -> None:
    msgs = [{"role": "user", "content": "Sage mir etwas"}]
    resp = "Antwort"

    calls: list[tuple[list[dict[str, str]], str]] = []

    def fake_llm(messages, response):
        calls.append((messages, response))
        return {"summary": "LLM", "keyfacts": ["KF"]}

    out = summarize_turn(msgs, resp, use_llm=True, llm_function=fake_llm)
    assert out == {"summary": "LLM", "keyfacts": ["KF"]}
    assert calls and calls[0][1] == resp


def test_llm_summarize_calls_helpers() -> None:
    msgs = [{"role": "user", "content": "Hallo"}]
    resp = "Zusammenfassend wichtig: Tests."
    out = llm_summarize(msgs, resp)
    assert "summary" in out and "keyfacts" in out
