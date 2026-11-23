---
id: S6
title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
authors: Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, Haofen Wang
org: 同濟大學、復旦大學
url: https://arxiv.org/abs/2312.10997
dates: v1 2023-12-18，v5 2024-03-27
accessed: 2026-11-23
type: 學術綜述論文
---

# S6 擷取筆記：Gao et al. RAG Survey

## 讀取紀錄
- 第 1 次：arXiv HTML 版只讀到前約 30%（到第三章），評估章節來自 AI 摘要（⚠ 不可直接採用）。
- 第 2 次：改用 PDF 抽文字（PyMuPDF），逐字核對第七章 C 節 Evaluation Aspects → ✅

## 重點
1. **三種 RAG 典範**：
   - **Naive RAG（樸素 RAG）**：最早的形式，「索引 → 檢索 → 生成」，又稱 Retrieve-Read。
   - **Advanced RAG（進階 RAG）**：在檢索前、後加入優化策略，提高檢索品質。
   - **Modular RAG（模組化 RAG）**：加入新模組（搜尋、記憶、路由等），流程可以重組，例如反覆檢索、視情況才檢索。
2. **Naive RAG 流程**：
   - 索引：清理資料 → 切成片段 → 轉成向量 → 存進向量資料庫。
   - 檢索：用同一個 embedding 模型把問題轉成向量，取最相似的前 K 個片段。
   - 生成：把問題和片段組成提示，交給 LLM 回答。
3. **Naive RAG 的三類缺點**：
   - 檢索：精確度與召回率不足，找到不相關的片段或漏掉重要資訊。
   - 生成：仍可能產生沒有根據的內容（幻覺），或答非所問、有偏見。
   - 增強：多個來源的資訊整合不順、重複；只檢索一次可能不夠回答複雜問題。
4. **Advanced RAG 的優化**：
   - 檢索前：改善索引（較細的切法、加 metadata）、改寫或擴充使用者問題。
   - 檢索後：重新排序（rerank）、壓縮上下文，避免資訊過載。
5. **RAG vs 微調 vs 提示工程**：
   - 提示工程：最不需要外部知識，也不用改模型。
   - RAG：適合需要精確、可即時更新、可解釋來源的情境，但延遲較高。
   - 微調：可深度客製模型的行為與風格，但知識是靜態的，更新要重新訓練。
   - RAG 與微調「不互斥」，可以互補、一起用。
6. **評估：3 個品質分數** ✅：
   - 上下文相關性（Context Relevance）：檢索到的內容是否精確、相關。
   - 答案忠實度（Answer Faithfulness）：答案是否忠於檢索到的內容、沒有矛盾。
   - 答案相關性（Answer Relevance）：答案是否直接回應問題。
7. **評估：4 種能力** ✅：
   - 抗雜訊（Noise Robustness）：遇到「看似相關但沒有實質內容」的文件時能否處理。
   - 拒答能力（Negative Rejection）：資料裡沒有答案時，能否不亂回答。
   - 資訊整合（Information Integration）：能否整合多份文件回答複雜問題。
   - 反事實穩健性（Counterfactual Robustness）：文件裡有錯誤資訊時，能否辨認並忽略。
8. 論文指出這些評估指標還沒有成熟、統一的標準。
