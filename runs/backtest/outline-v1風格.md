# 簡報大綱（v2 新增節點：先寫大綱、先檢查，才產生 HTML）

> 每頁格式：`## 頁碼 | 類型 | 標題`，下面固定四欄：
> - **wiki**：這頁根據哪些 Wiki 頁面
> - **數字**：這頁會出現的所有數字（必須在 Wiki 找得到）
> - **新術語**：這頁「第一次」介紹的術語＝白話解釋（之後的頁面才能直接用）
> - **重點**：要講的內容
>
> 學習目標：G1 說得出 RAG 是什麼 / G2 畫得出四步驟 / G3 判斷限制與何時不用

## 1 | cover | RAG 是什麼？讓 AI 先查資料、再回答
- wiki：index, rag-definition
- 數字：無
- 新術語：無
- 重點：主題、操作說明

## 2 | goals | 今天的學習目標
- wiki：index
- 數字：無
- 新術語：無
- 重點：G1、G2、G3

## 3 | content | 先想一想：AI 這樣回答，對嗎？
- wiki：llm-limitations
- 數字：無
- 新術語：無
- 重點：產假反例（IBM），AI 很有自信地答錯

## 4 | content | 沒有 RAG 的 LLM，有三個大問題
- wiki：llm-limitations
- 數字：無
- 新術語：幻覺＝看似合理但錯誤的內容
- 重點：知識過期、幻覺、說不出依據；也不懂內部文件、更新要重新訓練

## 5 | content | 用比喻理解 RAG
- wiki：analogies
- 數字：無
- 新術語：無
- 重點：開書考（IBM）、法官與書記官（NVIDIA）

## 6 | content | 所以，RAG 是什麼？
- wiki：rag-definition, history-and-name
- 數字：2020、2100 萬
- 新術語：RAG＝先檢索再生成（封面已出現名稱，這頁正式定義）
- 重點：定義、參數記憶 vs 非參數記憶、名稱小故事（G1）

## 7 | content | RAG 的四個步驟
- wiki：rag-pipeline
- 數字：4、3、2（不同來源的步驟數）
- 新術語：無
- 重點：建索引（切片、轉成向量）→ 檢索 → 增強（組成新的提示）→ 生成；資料要更新（G2）

## 8 | content | 步驟①：為什麼要切片？什麼是向量？
- wiki：chunking-and-embedding
- 數字：100
- 新術語：token＝模型處理文字的基本單位；切片＝把長文件切成小段；向量＝把文字轉成一串數字
- 重點：輸入長度有限所以切片；意思相近→向量接近；同一個模型轉換

## 9 | content | 步驟②：怎麼「找」資料？
- wiki：retrieval-methods
- 數字：150、20
- 新術語：BM25＝比對完全相同字詞的關鍵字搜尋方法；重新排序＝先多撈再精挑
- 重點：關鍵字 vs 向量 vs 混合；reranking

## 10 | content | 走一遍：Alice 想請半天假
- wiki：rag-pipeline, use-cases
- 數字：無
- 新術語：無
- 重點：檢索人事資料＋請假規定 → 增強 → 生成附來源（G2）

## 11 | content | 進階：切片會「失去上下文」
- wiki：contextual-retrieval
- 數字：3、2023、35、49、67
- 新術語：無
- 重點：ACME 例子；情境式檢索；失敗率下降（不是準確率）

## 12 | content | RAG 的三代演進
- wiki：rag-paradigms
- 數字：無
- 新術語：無
- 重點：Naive / Advanced / Modular；代理式檢索

## 13 | content | RAG、微調、提示工程，怎麼選？
- wiki：rag-vs-finetuning
- 數字：無
- 新術語：微調＝用新資料再訓練模型
- 重點：比較表；RAG 與微調不互斥（G3）

## 14 | content | 換掉資料庫，就能更新知識？
- wiki：limitations-and-when-not
- 數字：82、2016、2018、70、68、12、4、20 萬、500
- 新術語：無
- 重點：換索引實驗；RAG 的限制；小知識庫不需要 RAG（G3）

## 15 | content | 怎麼知道 RAG 做得好不好？
- wiki：evaluation
- 數字：3、4
- 新術語：無
- 重點：3 個品質分數、4 種能力

## 16 | content | RAG 用在哪裡？
- wiki：use-cases
- 數字：無
- 新術語：無
- 重點：人資客服、醫療、金融；共通點

## 17 | quiz | 小測驗
- wiki：rag-definition, rag-pipeline, limitations-and-when-not
- 數字：50
- 新術語：無
- 重點：Q1 四步驟（G2）、Q2 規章更新要不要重新訓練（G1）、Q3 很短的規章要不要 RAG（G3）

## 18 | summary | 總結：三句話帶走
- wiki：rag-definition, rag-pipeline, limitations-and-when-not
- 數字：無
- 新術語：無
- 重點：G1、G2、G3 各一句

## 19 | refs | 參考資料
- wiki：index
- 數字：無
- 新術語：無
- 重點：S1–S7 完整書目
