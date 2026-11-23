---
title: RAG 檢索增強生成 — LLM Wiki 目錄
updated: 2026-11-23
---

# RAG 檢索增強生成 — LLM Wiki

> 這是一個用 LLM 協助建立與維護的個人知識庫，主題是「檢索增強生成（RAG）」。
> 共 ingest 7 篇有公信力的來源（2 篇學術論文 + 5 篇科技公司官方文件 / 部落格）。

## 🧭 入門（先讀這幾頁）
| 頁面 | 一句話摘要 |
|---|---|
| [[rag-definition]] | RAG 是什麼：先查資料、再根據資料回答 |
| [[llm-limitations]] | 沒有 RAG 的 LLM 有哪些問題（幻覺、過時、無來源） |
| [[analogies]] | 開書考、法官與書記官、熱心新員工三個比喻 |
| [[history-and-name]] | RAG 這個名字怎麼來的 |

## ⚙️ 運作原理
| 頁面 | 一句話摘要 |
|---|---|
| [[rag-pipeline]] | 建索引 → 檢索 → 增強 → 生成，附 Alice 請假例子 |
| [[chunking-and-embedding]] | 為什麼要切片、什麼是向量嵌入 |
| [[retrieval-methods]] | 關鍵字 vs 向量 vs 混合搜尋，以及重新排序 |
| [[contextual-retrieval]] | 片段失去上下文的問題與 Anthropic 的解法 |

## 🚀 進階與比較
| 頁面 | 一句話摘要 |
|---|---|
| [[rag-paradigms]] | Naive / Advanced / Modular RAG 與代理式檢索 |
| [[rag-vs-finetuning]] | RAG、微調、提示工程怎麼選 |
| [[evaluation]] | 3 個品質分數 + 4 種能力 |
| [[limitations-and-when-not]] | RAG 的限制，以及什麼時候不需要 RAG |
| [[use-cases]] | 人資、客服、醫療、金融等應用 |

## 📖 工具頁
| 頁面 | 一句話摘要 |
|---|---|
| [[glossary]] | 名詞解釋 |

## 📚 來源（raw/）
| ID | 來源 | 類型 |
|---|---|---|
| S1 | Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, NeurIPS — https://arxiv.org/abs/2005.11401 | 原始論文 |
| S2 | AWS, *What is RAG?* — https://aws.amazon.com/what-is/retrieval-augmented-generation/ | 官方說明 |
| S3 | IBM Research, *What is retrieval-augmented generation (RAG)?* (2023) — https://research.ibm.com/blog/retrieval-augmented-generation-RAG | 研究部落格 |
| S4 | NVIDIA, *What Is Retrieval-Augmented Generation, aka RAG?* (2023/2025) — https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/ | 官方部落格 |
| S5 | Anthropic, *Introducing Contextual Retrieval* (2024) — https://www.anthropic.com/engineering/contextual-retrieval | 技術文章 |
| S6 | Gao et al. (2023/2024), *RAG for LLMs: A Survey* — https://arxiv.org/abs/2312.10997 | 綜述論文 |
| S7 | Microsoft Learn, *RAG in Azure AI Search* (2026 更新) — https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview | 官方文件 |

其他：[[log]]（操作紀錄）
