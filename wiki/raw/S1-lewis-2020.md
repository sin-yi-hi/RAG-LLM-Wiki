---
id: S1
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
authors: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
org: Facebook AI Research、University College London、New York University
venue: NeurIPS 2020
url: https://arxiv.org/abs/2005.11401
dates: v1 2020-05-22，v4 2021-04-12
accessed: 2026-11-23
type: 學術論文（原始論文）
---

# S1 擷取筆記：Lewis et al. (2020)

## 讀取紀錄
- 第 1 次：arXiv HTML 版 → 只讀到前約 4 萬字元，後半為 AI 摘要（⚠ 不可直接採用）。PDF 回傳為二進位。
- 第 2 次：改用 PDF 抽文字（PyMuPDF），逐字核對第 4.5 節 → ✅

## 重點（改寫成中文，非原文照抄）
1. **要解決的問題**：只靠參數（模型權重）儲存知識的模型，很難擴充或修改記憶，也無法說明答案從哪來，還可能產生「幻覺」。
2. **RAG 的定義**：結合兩種記憶 —
   - 參數記憶（parametric memory）：預訓練的 seq2seq 生成模型（BART）。
   - 非參數記憶（non-parametric memory）：Wikipedia 的稠密向量索引，用 DPR 檢索器來查。
3. **知識庫規模** ✅：使用 2018 年 12 月的 Wikipedia，每篇文章切成不重疊的 100 字片段，共 2100 萬（21M）份文件。
4. **兩種版本**：
   - RAG-Sequence：整段答案都根據同一份檢索到的文件。
   - RAG-Token：每個字都可以參考不同文件。
5. **結果**：在三個開放領域問答資料集（Natural Questions、WebQuestions、CuratedTrec）達到當時最佳；人工評估顯示 RAG 產生的內容比純 BART 更符合事實、更具體。
   - 人工評估（Jeopardy 出題任務）✅：認為 RAG 較符合事實的比例 42.7%，認為 BART 較好的只有 7.1%。
6. **換索引就能更新知識（Index hot-swapping）** ✅：
   - 作者用 2016 年 12 月和 2018 年 12 月兩個版本的 Wikipedia 索引，準備 82 位在這段期間換人的世界領袖，問「誰是某某職位？」
   - 索引與年份相符：答對 70%（2016）、68%（2018）。
   - 索引與年份不符：只答對 12% 與 4%。
   - 作者結論：只要換掉非參數記憶，就能更新 RAG 的世界知識，不必重新訓練。
