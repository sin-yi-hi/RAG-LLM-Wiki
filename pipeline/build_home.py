"""
把「繳交內容.md」轉成作業首頁 index.html（GitHub Pages 的首頁）。
用法：python pipeline/build_home.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
md = (ROOT / "繳交內容.md").read_text(encoding="utf-8")
tpl = (ROOT / "pipeline" / "home_template.html").read_text(encoding="utf-8")
(ROOT / "index.html").write_text(
    tpl.replace("/*__MD__*/", json.dumps(md, ensure_ascii=False).replace("</", "<\\/")),
    encoding="utf-8")
print("index.html 產生完成")
