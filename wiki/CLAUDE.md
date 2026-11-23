# LLM Wiki 規則書（Schema）— 主題：RAG 檢索增強生成

> 這份檔案是給 AI 看的「Wiki 維護規則」。每次請 AI ingest、查詢或檢查 Wiki 時，都先把這份規則給它。

## 1. 資料夾結構

```
wiki/
├── CLAUDE.md          ← 本規則書
├── raw/               ← 原始來源筆記（S1~S7），ingest 後「不再修改」
├── discussions/       ← 「先討論、後生成」的討論紀錄
├── pages/             ← AI 維護的 Wiki 頁面（概念頁）
├── index.md           ← 目錄：所有頁面 + 一句話摘要
└── log.md             ← 時間軸：每次 ingest / query / lint 都記一筆
```

## 2. 三種操作

| 操作 | 做什麼 | 產出 |
|---|---|---|
| **Ingest** | 讀一篇新來源 → 先寫討論紀錄 → 決定要更新哪些頁面 → 更新頁面 | raw/Sx.md、discussions/、pages/ 更新、log.md 一筆 |
| **Query** | 依問題查 index.md → 讀相關頁面 → 回答並標出處；好的回答可回存成新頁面 | 回答（附 [[頁面]] 與 [S#]） |
| **Lint** | 跑 `pipeline/lint_wiki.py` 檢查出處、連結、孤兒頁、待查證項目 | runs/ 內的檢查紀錄 |

## 3. 寫作規則（硬性）

1. **每個頁面開頭要有 frontmatter**：`title`、`sources`（例如 `[S1, S3]`）、`updated`。
2. **有數字的句子，同一行一定要附來源 `[S#]`**。數字必須在 raw 筆記裡被標為「✅ 逐字確認」才可以寫進 pages。
3. 只寫來源裡有的內容。自己的整理或比喻要標 `（整理）`。
4. 頁面之間用 `[[頁面檔名]]` 互相連結；新頁面一定要加進 `index.md`。
5. 來源沒查證完的內容，用 `⚠待查證` 標起來，**不可以**被簡報引用。
6. 用語統一：Retrieval-Augmented Generation → 「檢索增強生成（RAG）」；embedding → 「向量嵌入（embedding）」；chunk → 「文件片段（chunk）」。

## 4. 來源編號

| ID | 來源 | 類型 |
|---|---|---|
| S1 | Lewis et al. (2020) RAG 原始論文，NeurIPS 2020 | 學術論文 |
| S2 | AWS — What is RAG? | 雲端廠商官方說明 |
| S3 | IBM Research Blog — What is RAG? (2023) | 研究機構部落格 |
| S4 | NVIDIA Blog — What Is RAG, aka RAG? (2023, 2025 更新) | 業界官方部落格 |
| S5 | Anthropic — Introducing Contextual Retrieval (2024) | AI 公司技術文章 |
| S6 | Gao et al. (2023/2024) RAG for LLMs: A Survey | 學術綜述論文 |
| S7 | Microsoft Learn — RAG in Azure AI Search | 官方技術文件 |
