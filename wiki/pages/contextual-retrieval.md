---
title: 情境式檢索（Contextual Retrieval）
sources: [S5]
updated: 2026-11-23
---

# 情境式檢索（Contextual Retrieval）

## 要解決的問題
片段被切出來後失去上下文。例：使用者問「ACME 公司 2023 年 Q2 營收成長多少？」，但相關片段只寫「公司營收比上一季成長 3%」，系統不知道這段是在講 ACME。[S5]

## 做法
1. 讓 LLM 讀整份文件和某個片段，替片段寫一小段說明（通常 50–100 tokens）。[S5]
   - 例：「這段出自 ACME 公司 2023 年 Q2 財報…」[S5]
2. 把說明加在片段前面，再做 embedding（Contextual Embeddings）和 BM25 索引（Contextual BM25）。[S5]

## 效果（前 20 個片段的檢索失敗率）[S5]
| 做法 | 失敗率 | 降幅 |
|---|---|---|
| 一般做法 | 5.7% | — [S5] |
| + Contextual Embeddings | 3.7% | 降低 35% [S5] |
| + Contextual BM25 | 2.9% | 降低 49% [S5] |
| + Reranking | 1.9% | 降低 67% [S5] |

⚠ 注意：35% / 49% / 67% 是「失敗率下降的比例」，**不是**準確率。[S5]

## 學到的事（整理）
RAG 的品質很大一部分取決於「找得準不準」，而不只是 LLM 本身強不強。

相關：[[retrieval-methods]]、[[chunking-and-embedding]]
