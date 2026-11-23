---
id: S7
title: "RAG and Generative AI - Foundry IQ (Azure AI Search)"
org: Microsoft Learn
url: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
dates: 最後更新 2026-11-17
accessed: 2026-11-23
type: 官方技術文件
---

# S7 擷取筆記：Microsoft Learn — RAG in Azure AI Search

## 讀取紀錄
- 一次讀取完整 ✅。注意：頁面標題已改名為「Foundry IQ」，網址仍是 retrieval-augmented-generation-overview。

## 重點
1. **定義**：RAG 是一種模式（pattern），把 LLM 的回答建立在「你自己的專有內容」上，以擴充 LLM 的能力。
2. **企業為什麼用**：資料分散在多個地方（SharePoint、資料庫、雲端儲存）；私有資料需要權限控管（例如只讓有權限的人查到特定文件）。
3. **為什麼要切片**：LLM 能接收的輸入長度（tokens）有限，所以要把大文件切成小片段，讓每個片段可以被單獨比對。
4. **搜尋方式**：
   - 關鍵字 / 全文搜尋。
   - 向量搜尋：比對 embedding 的相似度。
   - 混合搜尋（hybrid）：關鍵字和向量同時查，合併結果，提高召回率。
   - 語意排序（semantic ranking）：依「意思」對結果重新評分排序。
5. **提高檢索品質的方法**：混合搜尋提高召回、語意排序提高相關性；限制回傳筆數（top-k）與最低分數門檻；只回傳需要的欄位。
6. **代理式檢索（agentic retrieval）**：用 LLM 做「查詢規劃」，把一個複雜問題拆成多個子查詢，平行到不同來源查，再合併結果。Microsoft 建議新專案優先採用；簡單需求可用傳統 RAG。
