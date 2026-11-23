"""
節點 C：Wiki 檢查（Lint）
檢查 wiki/pages/*.md 是否符合 wiki/CLAUDE.md 的寫作規則。

用法：python pipeline/lint_wiki.py
回傳碼：0 = 全部通過；1 = 有 ERROR（要回到「寫 Wiki 頁面」節點重寫）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PAGES = WIKI / "pages"
RAW = WIKI / "raw"

errors, warnings = [], []


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


raw_text = {}
for f in RAW.glob("S*.md"):
    sid = f.name.split("-")[0]
    raw_text[sid] = f.read_text(encoding="utf-8")

page_names = {p.stem for p in PAGES.glob("*.md")} | {"index", "log"}
NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*%?")


def numbers_in(line):
    line = re.sub(r"\[S\d\]", "", line)          # 引用標記
    line = re.sub(r"\bS\d\b", "", line)           # 文中提到來源編號
    line = re.sub(r"^\s*(#+\s*)?\d+\.\s", "", line)  # 條列 / 標題序號
    line = re.sub(r"^\s*[-*]\s*\d+\.\s", "", line)
    return [n.rstrip("%") for n in NUM.findall(line)]


checked_pages = 0
for page in sorted(PAGES.glob("*.md")):
    checked_pages += 1
    name = page.stem
    fm, body = parse(page)
    # 規則 1：frontmatter
    if fm is None or not all(k in fm for k in ("title", "sources", "updated")):
        errors.append(f"[{name}] 缺少 frontmatter（title / sources / updated）")
        continue
    declared = set(re.findall(r"S\d", fm["sources"]))
    cited_all = set()
    for i, line in enumerate(body.splitlines(), 1):
        cites = set(re.findall(r"\[(S\d)\]", line))
        cited_all |= cites
        nums = numbers_in(line)
        # 規則 2：有數字的句子同一行要有 [S#]
        if nums and not cites:
            errors.append(f"[{name}:{i}] 有數字 {nums} 但沒有附來源 [S#] → {line.strip()[:60]}")
            continue
        # 規則 2b：數字必須出現在所引用來源的 raw 筆記裡（防止 AI 自己編數字）
        for n in nums:
            pat = re.compile(rf"(?<![\d.]){re.escape(n)}(?![\d])")
            if not any(pat.search(raw_text.get(s, "")) for s in cites):
                errors.append(f"[{name}:{i}] 數字「{n}」在引用的來源 {sorted(cites)} 筆記裡找不到")
        # 規則 5：待查證不可留在頁面
        if "⚠待查證" in line:
            warnings.append(f"[{name}:{i}] 仍有 ⚠待查證 內容")
    # 來源一致性
    for s in cited_all - declared:
        errors.append(f"[{name}] 內文引用 {s}，但 frontmatter sources 沒列")
    for s in declared - cited_all:
        warnings.append(f"[{name}] frontmatter 列了 {s}，但內文沒有引用")
    for s in cited_all:
        if s not in raw_text:
            errors.append(f"[{name}] 引用 {s}，但 raw/ 找不到這個來源")
    # 規則 4：連結要存在
    for link in re.findall(r"\[\[([^\]]+)\]\]", body):
        if link not in page_names:
            errors.append(f"[{name}] 連結 [[{link}]] 指向不存在的頁面")

# 規則 4b：孤兒頁（沒被 index 連到）
index_links = set(re.findall(r"\[\[([^\]]+)\]\]", (WIKI / "index.md").read_text(encoding="utf-8")))
for p in PAGES.glob("*.md"):
    if p.stem not in index_links:
        errors.append(f"[index] 頁面 {p.stem} 沒有出現在 index.md（孤兒頁）")

print(f"== Wiki Lint：檢查 {checked_pages} 頁、{len(raw_text)} 個來源 ==")
for e in errors:
    print("ERROR  ", e)
for w in warnings:
    print("WARN   ", w)
print(f"結果：{len(errors)} 個錯誤、{len(warnings)} 個警告 → {'PASS' if not errors else 'FAIL'}")
sys.exit(1 if errors else 0)
