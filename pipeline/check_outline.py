"""
節點 E2（v2 新增）：大綱檢查（Outline Check）
在產生 HTML 之前，先檢查 slides/outline.md：
  1. 每頁引用的 Wiki 頁面存在
  2. 每頁「數字」欄的數字都能在引用的 Wiki 頁面找到
  3. 每個術語都有被「介紹一次」，而且介紹的頁面不晚於第一次在重點裡用到的頁面
  4. 三個學習目標 G1~G3 都有對應的內容頁、測驗題與總結

用法：python pipeline/check_outline.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_slides import TERMS, page_info  # 共用同一份術語表與 Wiki 讀取方式（import 時不會執行檢查）

ROOT = Path(__file__).resolve().parent.parent
OUTLINE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides" / "outline.md"
errors = []

blocks = re.split(r"^## ", OUTLINE.read_text(encoding="utf-8"), flags=re.M)[1:]
slides = []
for b in blocks:
    head, *lines = b.splitlines()
    no, stype, title = [x.strip() for x in head.split("|", 2)]
    fields = {}
    for ln in lines:
        m = re.match(r"- (wiki|數字|新術語|重點)：(.*)", ln.strip())
        if m:
            fields[m.group(1)] = m.group(2).strip()
    slides.append((int(no), stype, title, fields))

introduced = {}
for no, stype, title, f in slides:
    tag = f"[大綱第{no}頁]"
    for k in ("wiki", "數字", "新術語", "重點"):
        if k not in f:
            errors.append(f"{tag} 缺少「{k}」欄位")
    names = [w.strip() for w in f.get("wiki", "").split(",") if w.strip()]
    wiki_text = ""
    for w in names:
        t, _ = page_info(w)
        if t is None:
            errors.append(f"{tag} Wiki 頁面不存在：{w}")
        else:
            wiki_text += t
    nums = f.get("數字", "無")
    if nums != "無":
        for n in re.findall(r"\d+(?:\.\d+)?", nums):
            if not re.search(rf"(?<![\d.]){re.escape(n)}(?![\d])", wiki_text):
                errors.append(f"{tag} 數字「{n}」在 Wiki {names} 找不到")
    terms = f.get("新術語", "無")
    if terms != "無":
        for item in re.split(r"；", terms):
            if "＝" not in item:
                errors.append(f"{tag} 術語「{item}」沒有寫白話解釋（格式：術語＝解釋）")
                continue
            term = item.split("＝")[0].strip()
            introduced.setdefault(term, no)

# 規則 3：每個術語都要被介紹，且介紹不晚於第一次被使用
for term, aliases in TERMS.items():
    first_use = next((no for no, st, title, f in slides
                      if st not in ("cover", "goals", "refs")
                      and any(a.lower() in (title + f.get("重點", "")).lower() for a in aliases)), None)
    if term not in introduced:
        errors.append(f"[術語] 「{term}」整份簡報都沒有介紹")
    elif first_use and introduced[term] > first_use:
        errors.append(f"[術語] 「{term}」在第 {first_use} 頁就用到，但第 {introduced[term]} 頁才介紹")

# 規則 4：學習目標覆蓋
for g in ("G1", "G2", "G3"):
    kinds = {st for no, st, title, f in slides if g in f.get("重點", "")}
    for need in ("content", "quiz", "summary"):
        if need not in kinds:
            errors.append(f"[目標] {g} 沒有對應的 {need} 頁")

print(f"== Outline Check：共 {len(slides)} 頁、介紹 {len(introduced)} 個術語 ==")
for e in errors:
    print("ERROR  ", e)
print(f"結果：{len(errors)} 個錯誤 → {'PASS' if not errors else 'FAIL'}")
sys.exit(1 if errors else 0)
