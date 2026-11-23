# RAG LLM Wiki — 用 LLM Wiki 做教學 HTML 簡報

- 作業首頁：`index.html`（內容同 `繳交內容.md`）
- LLM Wiki：`wiki.html`（原始檔在 `wiki/`）
- 教學簡報：`slides/index.html`

## 重新執行整個檢查流程
```bash
python pipeline/lint_wiki.py        # 節點 E：Wiki 檢查
python pipeline/check_outline.py    # 節點 H：大綱檢查（v2 新增）
python pipeline/check_slides.py     # 節點 J：簡報檢查
python pipeline/build_wiki_html.py  # 重新產生 wiki.html
python pipeline/build_home.py       # 重新產生 index.html
```
（Windows 若出現中文亂碼，先執行 `set PYTHONIOENCODING=utf-8`）

## 上傳到 GitHub Pages
1. 在 GitHub 建立一個 public repository，名稱 `RAG-LLM-Wiki`
2. 把這個資料夾裡的所有檔案上傳（Add file → Upload files，整個資料夾拖進去）
3. Settings → Pages → Source 選 `Deploy from a branch`，Branch 選 `main`、資料夾 `/ (root)` → Save
4. 等 1–2 分鐘，網址會是 `https://<你的帳號>.github.io/RAG-LLM-Wiki/`
5. 把 `繳交內容.md` 裡的 `<你的GitHub帳號>` 換成自己的帳號，再執行 `python pipeline/build_home.py` 重新產生首頁
