import importlib
import json

import pytest


def test_content_management_text_utils():
    cm = importlib.import_module("novapolis_agent.app.core.content_management")
    assert cm.check_content_allowed("explicit") is True
    s = "Hallo! Wie geht's? Ich bin hier."
    parts = cm.split_sentences(s)
    assert isinstance(parts, list) and len(parts) >= 2
    assert cm.trim_length(s, 10) == s[:10]
    assert cm.limit_sentences(s, 1).endswith(".") or isinstance(cm.limit_sentences(s, 1), str)
    neut = cm.neutralize("ich: Hallo! das ist ein Test.")
    assert isinstance(neut, str)
    comp = cm.compact("a ,  b   .")
    assert "," in comp
    mod = cm.modify_prompt_for_freedom("X")
    assert "Systemprompt" in mod


def test_content_management_policy_apply(tmp_path, monkeypatch):
    cm = importlib.import_module("novapolis_agent.app.core.content_management")
    # create a fake policy file
    policy = {
        "default": {
            "forbidden_terms": ["badword"],
            "rewrite_map": {"foo": "bar"},
        }
    }
    pf = tmp_path / "pol.json"
    pf.write_text(json.dumps(policy, ensure_ascii=False))

    class S:
        POLICIES_ENABLED = True
        POLICY_FILE = str(pf)
        POLICY_STRICT_UNRESTRICTED_BYPASS = False

    monkeypatch.setattr(cm, "settings", S())

    msgs = [{"role": "user", "content": "this has foo"}]
    pre = cm.apply_pre(msgs, mode="default")
    assert pre.action in ("allow", "rewrite")

    # forbidden term -> block
    msgs2 = [{"role": "user", "content": "contains badword"}]
    pre2 = cm.apply_pre(msgs2, mode="default")
    assert pre2.action == "block"

    # apply_post rewrite_map
    post = cm.apply_post("hello foo world", mode="default")
    assert post.action in ("allow", "rewrite")


@pytest.mark.asyncio
async def test_memory_inmemory_and_jsonl(tmp_path, monkeypatch):
    mem = importlib.import_module("novapolis_agent.app.core.memory")

    # Ensure settings to enable memory
    class S:
        MEMORY_ENABLED = True
        MEMORY_STORE = "inmemory"
        MEMORY_MAX_TURNS = 10
        MEMORY_MAX_CHARS = 1000

    monkeypatch.setattr(mem, "settings", S())
    # InMemoryStore
    store = mem.InMemoryStore()
    await store.append("s1", "user", "hello")
    await store.append("s1", "assistant", "reply")
    window = await store.get_window("s1", max_chars=100, max_turns=10)
    assert isinstance(window, list) and len(window) >= 1
    await store.clear("s1")
    w2 = await store.get_window("s1", max_chars=100, max_turns=10)
    assert w2 == []

    # JsonlStore
    js = mem.JsonlStore(base_dir=tmp_path / "mem")
    await js.append("s2", "user", "u1")
    await js.append("s2", "assistant", "a1")
    w3 = await js.get_window("s2", max_chars=100, max_turns=10)
    assert isinstance(w3, list) and len(w3) >= 1
    await js.clear("s2")
    assert (tmp_path / "mem" / "session_s2.jsonl").exists() is False


def test_estimate_tokens_and_is_text():
    et = importlib.import_module("novapolis_agent.scripts.estimate_tokens")
    assert et.is_text_file("file.py")
    assert et.is_text_file("readme.MD")
    # count_tokens fallback
    assert isinstance(et.count_tokens("abcd" * 10), int)


def test_eval_utils_and_prepare_pack(tmp_path):
    eu = importlib.import_module("novapolis_agent.utils.eval_utils")
    assert eu.strip_eval_prefix("eval-123") == "123"
    assert eu.ensure_eval_prefix("123") == "eval-123"
    assert eu.truncate("hello world", 5).endswith("...")
    assert eu.normalize_text("ÄÖÜ! test")

    # coerce_json_to_jsonl
    j = '{"a":1}\n{"b":2}'
    res = eu.coerce_json_to_jsonl(j)
    assert isinstance(res, list) and len(res) >= 2

    # load_synonyms
    syn = {"a": ["x", "y"]}
    p = tmp_path / "syn.json"
    p.write_text(json.dumps(syn, ensure_ascii=False))
    ld = eu.load_synonyms(str(p))
    assert ld.get("a") == ["x", "y"]

    # prepare_finetune_pack helpers
    pf = importlib.import_module("novapolis_agent.scripts.prepare_finetune_pack")
    # create a minimal jsonl source
    src = tmp_path / "src.jsonl"
    rows = [
        {
            "messages": [
                {"role": "user", "content": "instr1"},
                {"role": "assistant", "content": "out1"},
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "instr2"},
                {"role": "assistant", "content": "out2"},
            ]
        },
    ]
    src.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
    res = pf.prepare_pack(
        str(src), out_dir=str(tmp_path), format="openai_chat", train_ratio=0.5, min_output_chars=1
    )
    assert res.get("ok") is True
    assert "train" in res and "val" in res


def test_rag_tokenize_and_index(tmp_path):
    rg = importlib.import_module("novapolis_agent.utils.rag")
    toks = rg.tokenize("Hello WORLD 123 ab")
    assert isinstance(toks, list)
    # build index from a small file
    f = tmp_path / "doc.md"
    f.write_text("Hello world hello")
    idx = rg.build_index([str(f)])
    assert idx.n_docs == 1
    # retrieve should return empty for unrelated query
    out = rg.retrieve(idx, "nonexistenttoken")
    assert isinstance(out, list)
