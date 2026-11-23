"""
把 wiki/ 底下的 Markdown 打包成一個可以直接用瀏覽器開的 wiki.html（給老師/同學瀏覽用）。
用法：python pipeline/build_wiki_html.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "wiki"

docs = {}
order = []


def add(key, path, group):
    docs[key] = {"group": group, "md": path.read_text(encoding="utf-8")}
    order.append(key)


add("index", W / "index.md", "目錄")
for p in sorted((W / "pages").glob("*.md")):
    add(p.stem, p, "Wiki 頁面")
for p in sorted((W / "raw").glob("*.md")):
    add(p.stem, p, "原始來源 raw")
for p in sorted((W / "discussions").glob("*.md")):
    add(p.stem, p, "討論紀錄")
add("log", W / "log.md", "紀錄")
add("CLAUDE", W / "CLAUDE.md", "紀錄")

template = (ROOT / "pipeline" / "wiki_template.html").read_text(encoding="utf-8")
out = template.replace("/*__DOCS__*/", json.dumps({"order": order, "docs": docs}, ensure_ascii=False).replace("</", "<\\/"))
(ROOT / "wiki.html").write_text(out, encoding="utf-8")
print(f"wiki.html 產生完成：{len(order)} 份文件")
