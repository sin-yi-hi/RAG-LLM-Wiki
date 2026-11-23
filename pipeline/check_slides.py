"""
節點 G：簡報檢查（Slide Check）
檢查 slides/index.html 的內容能不能追溯回 Wiki，以及是不是適合初學者的教學結構。

用法：python pipeline/check_slides.py [slides/index.html]
回傳碼：0 = 通過；1 = 有 ERROR（回到「產生簡報」節點重寫有問題的頁面）
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "wiki" / "pages"
SLIDES = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides" / "index.html"

MAX_CHARS = 250            # 每頁畫面上的字數上限（不含講者備註與出處列）
REQUIRED_TYPES = ["cover", "goals", "quiz", "summary", "refs"]
# 初學者不懂的術語：第一次出現的那一頁，必須用 <dfn> 解釋
TERMS = {
    "LLM": ["LLM", "大型語言模型"],
    "幻覺": ["幻覺", "hallucination"],
    "提示": ["提示", "prompt"],
    "切片": ["切片", "片段", "chunk"],
    "token": ["token"],
    "向量": ["向量", "embedding"],
    "BM25": ["BM25"],
    "重新排序": ["重新排序", "reranking"],
    "微調": ["微調"],
}
CN_NUM = {"一": "1", "二": "2", "兩": "2", "三": "3", "四": "4", "五": "5",
          "六": "6", "七": "7", "八": "8", "九": "9", "十": "10"}

errors, warnings = [], []


def page_info(name):
    if name == "index":
        p = ROOT / "wiki" / "index.md"
    else:
        p = PAGES / f"{name}.md"
    if not p.exists():
        return None, set()
    t = p.read_text(encoding="utf-8")
    m = re.search(r"^sources:\s*\[(.*?)\]", t, re.M)
    srcs = set(re.findall(r"S\d", m.group(1))) if m else set(re.findall(r"\bS\d\b", t))
    t = re.sub(r"\[S\d\]|\bS\d\b", " ", t)
    t = "".join(CN_NUM.get(c, c) for c in t)   # 「三步」也能對到「3 步」
    return t, srcs


def text_of(fragment):
    fragment = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment))


NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*%?")


def numbers(t):
    t = re.sub(r"\d️?⃣", " ", t)          # 1️⃣ 這類 emoji 序號
    t = re.sub(r"\bQ\d\b", " ", t)                   # 測驗題號 Q1
    t = re.sub(r"\bS\d\b", " ", t)
    return [n.rstrip("%") for n in NUM.findall(t)]


def main():
    src = SLIDES.read_text(encoding="utf-8")
    sections = re.findall(r'<section class="slide"([^>]*)>(.*?)</section>', src, re.S)
    types_seen = []
    term_first = {}

    for idx, (attrs, body) in enumerate(sections, 1):
        stype = (re.search(r'data-type="([^"]+)"', attrs) or [None, "?"])[1]
        types_seen.append(stype)
        wiki_attr = re.search(r'data-wiki="([^"]*)"', attrs)
        tag = f"[第{idx}頁/{stype}]"
        if not wiki_attr or not wiki_attr.group(1).strip():
            errors.append(f"{tag} 沒有標 data-wiki（不知道內容根據哪個 Wiki 頁面）")
            continue
        wiki_names = [w.strip() for w in wiki_attr.group(1).split(",")]
        wiki_text, wiki_srcs = "", set()
        for w in wiki_names:
            t, s = page_info(w)
            if t is None:
                errors.append(f"{tag} data-wiki 指向不存在的 Wiki 頁面：{w}")
                continue
            wiki_text += t
            wiki_srcs |= s

        cite = re.search(r'<div class="cite">(.*?)</div>', body, re.S)
        notes = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
        visible = body
        if cite:
            visible = visible.replace(cite.group(0), "")
        if notes:
            visible = visible.replace(notes.group(0), "")
        vis_text = text_of(visible)
        all_text = vis_text + " " + (text_of(notes.group(1)) if notes else "")

        if stype == "refs":
            continue

        # 檢查 1：出處列的 S# 必須是這些 Wiki 頁面有用到的來源
        if stype not in ("cover", "goals"):
            if not cite:
                errors.append(f"{tag} 沒有出處列（Wiki 頁面 + 來源編號）")
            else:
                chips = set(re.findall(r'<span class="src">(S\d)</span>', cite.group(1)))
                for s in sorted(chips - wiki_srcs):
                    errors.append(f"{tag} 出處標了 {s}，但引用的 Wiki 頁面 {wiki_names} 沒有這個來源")
                wiki_part = text_of(cite.group(1)).split("｜")[0].replace("Wiki：", "")
                listed = set(re.findall(r"[a-z][a-z0-9-]+", wiki_part))
                if listed != set(wiki_names):
                    errors.append(f"{tag} 出處列寫的 Wiki 頁面 {sorted(listed)} 和 data-wiki {wiki_names} 不一致")

        # 檢查 2：簡報（含講者備註）出現的每個數字，都要能在引用的 Wiki 頁面找到
        for n in numbers(all_text):
            if not re.search(rf"(?<![\d.]){re.escape(n)}(?![\d])", wiki_text):
                errors.append(f"{tag} 數字「{n}」在 Wiki 頁面 {wiki_names} 找不到 → 可能是 AI 自己加的")

        # 檢查 3：字數（初學者一頁不要塞太多字）
        n_chars = len(re.sub(r"\s", "", vis_text))
        if n_chars > MAX_CHARS:
            errors.append(f"{tag} 畫面字數 {n_chars} 超過 {MAX_CHARS}，請拆頁或刪減")

        # 檢查 4：術語第一次出現時要有 <dfn> 解釋
        if stype not in ("cover", "goals"):
            dfns = " ".join(text_of(d) for d in re.findall(r"<dfn>(.*?)</dfn>", body, re.S))
            for term, aliases in TERMS.items():
                if term in term_first:
                    continue
                if any(a.lower() in all_text.lower() for a in aliases):
                    term_first[term] = idx
                    if not any(a.lower() in dfns.lower() for a in aliases):
                        errors.append(f"{tag} 術語「{term}」第一次出現，但沒有用 <dfn> 解釋")

    # 檢查 5：教學結構
    for t in REQUIRED_TYPES:
        if t not in types_seen:
            errors.append(f"[結構] 缺少 {t} 類型的頁面")
    if types_seen and types_seen[0] != "cover":
        errors.append("[結構] 第一頁應該是封面")

    print(f"== Slide Check：{SLIDES.name}，共 {len(sections)} 頁 ==")
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    print(f"結果：{len(errors)} 個錯誤、{len(warnings)} 個警告 → {'PASS' if not errors else 'FAIL'}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
