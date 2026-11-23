---
title: Wiki 操作紀錄（log）
updated: 2026-11-23
---

# Wiki 操作紀錄

> 格式：`## [日期] 操作 | 內容`，最新的在最下面。

## [2026-11-23] discuss | 主題與範圍
- 決定主題 RAG、目標聽眾（非技術背景大學生）、頁面清單、來源篩選標準 → discussions/00

## [2026-11-23] fetch | 取得 7 篇來源
- S1 Lewis 2020、S2 AWS、S3 IBM、S4 NVIDIA、S5 Anthropic、S6 Gao 綜述、S7 Microsoft Learn
- ⚠ 問題：S1、S6 的 arXiv 網頁版只讀到前 30–45%，後半是 AI 自動摘要；PDF 直接讀是亂碼

## [2026-11-23] verify | 回到取得資料節點重抓
- 改用 PyMuPDF 從 PDF 抽文字，逐字核對：
  - S1 第 4.5 節：82 位世界領袖、70% / 68% / 12% / 4% ✅
  - S1：100 字片段、21M 份文件 ✅
  - S6 第七章 C 節：3 個品質分數、4 種能力 ✅
- 發現：AI 摘要曾錯誤地說論文「沒有寫領袖人數」，原文其實有寫 82 位 → 證明摘要不能直接當來源

## [2026-11-23] ingest | S1–S7 討論後寫入
- 先寫 discussions/01（每篇的重點、衝突、要更新哪些頁）再生成頁面
- 新增 14 個頁面：rag-definition、llm-limitations、analogies、history-and-name、rag-pipeline、chunking-and-embedding、retrieval-methods、contextual-retrieval、rag-paradigms、rag-vs-finetuning、evaluation、limitations-and-when-not、use-cases、glossary

## [2026-11-23] lint | 第 1 次 → FAIL（8 個錯誤）
- 6 個：有數字的句子沒附 [S#]（contextual-retrieval 3 處、limitations-and-when-not 3 處）
- 2 個：llm-limitations 內文引用 S4、S7，frontmatter 沒列
- 修正後第 2 次 → PASS（0 錯誤）

## [2026-11-23] query | 為簡報查詢 Wiki
- 依 3 個學習目標查詢：「RAG 是什麼」「怎麼運作」「限制與何時不用」→ 讀取 index → 選出 14 個頁面
- 查詢心得：比喻分散在 analogies，例子分散在 rag-pipeline 和 use-cases，index 的一句話摘要幫助很大

## [2026-11-23] slides v1 | 直接產生 HTML → 檢查 FAIL
- 第 1 次：26 個錯誤，其中 16 個是檢查器 bug（把「Wiki：」的 iki 當成頁名）→ 修檢查器
- 第 2 次：10 個真正的錯誤：2 個 Wiki 沒有的數字（15 分鐘、50 頁）、8 個術語第一次出現沒解釋

## [2026-11-23] workflow v2 | 新增「大綱 + 大綱檢查」節點
- 在產生 HTML 之前先寫 slides/outline.md（每頁的 wiki、數字、新術語、重點）
- check_outline.py 第 1 次 → PASS；回測：把 v1 錯誤放回大綱 → 抓到 5 個錯誤，確認檢查有效
- 依大綱重新產生 HTML → check_slides.py → PASS（0 錯誤）
