---
title: 怎麼評估 RAG 做得好不好？
sources: [S5, S6]
updated: 2026-11-23
---

# 怎麼評估 RAG？（Gao 綜述，PDF 逐字確認 ✅）

## 3 個品質分數 [S6]
| 名稱 | 問的問題 |
|---|---|
| 上下文相關性 Context Relevance | 找到的資料跟問題有關嗎？ |
| 答案忠實度 Answer Faithfulness | 答案有沒有忠於找到的資料、不自己亂編？ |
| 答案相關性 Answer Relevance | 答案有沒有直接回答問題？ |

## 4 種能力 [S6]
| 能力 | 意思 |
|---|---|
| 抗雜訊 Noise Robustness | 遇到看似相關但沒有實質內容的文件，還能答對 |
| 拒答 Negative Rejection | 資料裡沒有答案時，不要硬答 |
| 資訊整合 Information Integration | 能整合多份文件回答複雜問題 |
| 反事實穩健性 Counterfactual Robustness | 文件中有錯誤資訊時，能辨認並忽略 |

- 這些評估指標目前還沒有成熟、統一的標準。[S6]
- 實務建議：用自己的資料做評估測試，再決定設定。[S5]

## 跟我的 Wiki 有什麼關係？（整理）
「答案忠實度」正好就是我在簡報檢查節點做的事：簡報每一頁的內容，都要能在 Wiki 裡找到依據。

相關：[[rag-paradigms]]、[[limitations-and-when-not]]
