# 討論 01：逐篇 ingest 討論（先討論、後生成）

> 做法：每讀完一篇來源，先跟 AI 討論「這篇的重點是什麼、跟其他來源有沒有衝突、要更新哪幾頁」，**確認後**才讓 AI 動手寫頁面。

---

## S1 Lewis et al. 2020（RAG 原始論文）
- **重點**：RAG = 參數記憶（BART 生成器）+ 非參數記憶（Wikipedia 向量索引，用 DPR 檢索器）。兩種版本 RAG-Sequence / RAG-Token。
- **討論**：論文數字很多（各資料集分數），對初學者太細 → Wiki 只留「Wikipedia 切成 100 字片段、共 2100 萬份文件」和「換索引就能更新知識」這個實驗。
- **查證問題** ⚠：第一次用網頁版讀取時被截斷，世界領袖實驗的 70% / 68% / 12% / 4% 只出現在 AI 摘要裡，沒讀到原文 → **先不寫進 Wiki**，回到「取得資料」重新抓 PDF。
- **重抓結果**：用 PDF 抽出文字後逐字確認：82 位世界領袖、2016 vs 2018 索引、70% / 68% / 12% / 4% 都正確 → 標為 ✅。
- **要更新的頁面**：rag-definition、history-and-name、limitations-and-when-not（知識更新）、glossary

## S2 AWS — What is RAG?
- **重點**：定義（生成前先參考訓練資料以外的權威知識庫）、LLM 的 4 個問題、4 個好處、運作 4 步驟。
- **討論**：AWS 的 4 步驟（建立外部資料 → 檢索 → 增強提示 → 更新外部資料）很適合當簡報的流程主軸。
- **衝突檢查**：AWS 把「更新外部資料」當成一個步驟，Gao 綜述則是「索引 → 檢索 → 生成」三步。→ 討論後決定：簡報用「建索引 → 檢索 → 增強 → 生成」四格，「更新資料」放在旁邊當補充。兩者不矛盾，只是切法不同。
- **要更新的頁面**：rag-definition、llm-limitations、rag-pipeline、analogies（新員工比喻）

## S3 IBM Research Blog
- **重點**：開書考 vs 閉卷考比喻；兩個階段（檢索、生成）；好處包括可引用來源、降低幻覺、減少敏感資料外洩、減少重新訓練成本；HR 請假的例子。
- **討論**：「Alice 請半天假」這個例子很生活化，適合當簡報裡「走一遍」的例子。產假例子適合當開場的反例（沒有 RAG 時亂回答）。
- **限制**：模型不知道自己不知道 → 放進 limitations 頁。
- **要更新的頁面**：analogies、rag-pipeline、llm-limitations、limitations-and-when-not、use-cases

## S4 NVIDIA Blog
- **重點**：法官與書記官比喻；名稱由來（Patrick Lewis 說如果早知道會取更好聽的名字）；可以像論文註腳一樣引用來源。
- **討論**：文章是 2023 年發表、2025 年更新，有提到 NVIDIA 自家產品 → 產品介紹不收，只收概念與比喻。
- **要更新的頁面**：analogies、history-and-name、rag-pipeline、use-cases

## S5 Anthropic — Contextual Retrieval
- **重點**：一般 RAG 的做法（切片、embedding、BM25、合併）；片段失去上下文的問題；Contextual Retrieval 讓檢索失敗率下降 35% / 49% / 67%；知識庫小於 20 萬 tokens 可以直接整份放進提示。
- **討論**：這是「進階」內容，但「片段看不出在講哪家公司」這個例子很好懂 → 簡報放一頁。「20 萬 tokens 以下不用 RAG」放進 limitations-and-when-not，讓聽眾知道 RAG 不是一定要用。
- **注意**：35% / 49% / 67% 是「檢索失敗率的降幅」，不是準確率 → Wiki 要寫清楚，避免簡報寫錯。
- **要更新的頁面**：chunking-and-embedding、retrieval-methods、contextual-retrieval、limitations-and-when-not

## S6 Gao et al. — RAG Survey
- **重點**：Naive / Advanced / Modular 三種 RAG；Naive RAG 的三類缺點；RAG vs 微調 vs 提示工程；評估：3 個品質分數 + 4 種能力。
- **查證問題** ⚠：網頁版只讀到前 30%，評估章節來自 AI 摘要 → 回頭從 PDF 抽文字，逐字確認 3 個品質分數與 4 種能力的名稱與定義 → 標為 ✅。
- **要更新的頁面**：rag-paradigms、rag-vs-finetuning、evaluation、rag-pipeline

## S7 Microsoft Learn
- **重點**：RAG 是把回答建立在自家內容上的模式；LLM 輸入長度有限，所以要切片；關鍵字、向量、混合搜尋、語意排序；「代理式檢索（agentic retrieval）」會把問題拆成多個子查詢。
- **討論**：文件標題已改成「Foundry IQ」，跟網址不同，ingest 時記下來以免之後找不到。代理式檢索屬於最新發展 → 放在 rag-paradigms 當延伸。
- **要更新的頁面**：retrieval-methods、chunking-and-embedding、rag-paradigms、use-cases
