---
id: S5
title: "Introducing Contextual Retrieval"
org: Anthropic
url: https://www.anthropic.com/engineering/contextual-retrieval
dates: 2024-09-19
accessed: 2026-11-23
type: AI 公司技術文章
---

# S5 擷取筆記：Anthropic — Contextual Retrieval

## 讀取紀錄
- 一次讀取完整 ✅（/news/ 網址會導向 /engineering/）

## 重點
1. **一般 RAG 的做法**：
   - 把知識庫切成片段（chunk），通常不超過幾百個 tokens。
   - 用 embedding 模型把片段轉成向量，存進向量資料庫，做語意搜尋。
   - 另外用 BM25（關鍵字比對的排序方法）找「完全相同的字」，適合錯誤代碼、專有名詞。例：查「Error code TS-999」，語意搜尋可能找不到，BM25 可以。
   - 兩種結果合併、去重複，取前 K 個片段放進提示。
2. **上下文問題**：片段被切出來後會失去上下文。例：問 ACME 公司 2023 年 Q2 營收，但片段只寫「公司營收比上一季成長 3%」，看不出是哪家公司、哪一季。
3. **Contextual Retrieval（情境式檢索）**：先讓 LLM 為每個片段寫一小段說明（通常 50–100 tokens，例如「這段出自 ACME 公司 2023 年 Q2 財報」），加在片段前面，再做 embedding（Contextual Embeddings）和 BM25 索引（Contextual BM25）。
4. **實驗結果**（前 20 個片段的「檢索失敗率」降幅）✅：
   - 只用 Contextual Embeddings：失敗率降低 35%（5.7% → 3.7%）
   - Contextual Embeddings + Contextual BM25：降低 49%（5.7% → 2.9%）
   - 再加上重新排序（reranking）：降低 67%（5.7% → 1.9%）
5. **重新排序（reranking）**：先撈比較多的候選片段（文章用 150 個），再用排序模型評分，只留最相關的 20 個。會增加一點延遲與成本。
6. **小知識庫不需要 RAG** ✅：知識庫小於 20 萬 tokens（約 500 頁）時，可以直接把整個知識庫放進提示。
7. 作者建議：用自己的資料做評估測試，再決定設定。
