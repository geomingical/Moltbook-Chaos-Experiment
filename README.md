# 🧪 Moltbook Chaos Experiment

**多智能體系統混沌行為與異見者傳播實驗**

> 探索 AI 多智能體系統在無人類干預下的輿論演變、RLHF 對齊效應，以及惡意資訊傳播路徑

---

## 🔬 三大實驗範式

| 版本 | 名稱 | 核心機制 | 結果 |
|------|------|----------|------|
| **v1** | 陣營催眠 | 4 種陣營 System Prompt | 部分崩潰，衝突有限 |
| **v2** | 回歸自然 | 移除催眠，測試 RLHF 本性 | 死水效應，極度同質化 |
| **v3** | 狼人殺模式 | 10% 異見者 + 90% 正常 | **100% 異見者成功率** |

---

## 🎯 關鍵發現

- **RLHF 訓練不足的模型是危險的異見者載體**：llama-3.1-8b 執行異見者任務成功率 100%
- **假設語氣繞過安全護欄**：「如果沒有人類...」的軟性引導無法被偵測
- **糾察隊完全失效**：GPT-4o、Claude 3.5 全程 0 次偵測到異見者
- **DeepSeek 最易影響**：3 次影響中 2 次來自 deepseek-chat

---

## 🚀 快速開始

```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 設定 API Key
echo "OPENROUTER_API_KEY=your_key_here" > .env

# 3. 驗證模型可用性 (推薦)
python test_models.py

# 4. 執行實驗
python moltbook_chaos_experiment_v1.py  # 陣營催眠
python moltbook_chaos_experiment_v2.py  # 回歸自然
python moltbook_chaos_experiment_v3.py  # 狼人殺異見者
```

---

## 📁 檔案結構

```
Chaos_exp/
├── moltbook_chaos_experiment_v1.py     # v1: 陣營催眠
├── moltbook_chaos_experiment_v2.py     # v2: 回歸自然
├── moltbook_chaos_experiment_v3.py     # v3: 狼人殺異見者
├── test_models.py                      # 模型驗證工具
├── requirements.txt                    # 依賴套件
├── moltbook_chaos_log_v*.md            # 對話紀錄
├── moltbook_chaos_analysis_v*.md       # 統計分析
└── Moltbook 多智能體實驗：混沌與異見者傳播綜合分析報告.md  # 綜合分析
```

---

## 📖 詳細報告

- 完整對話紀錄：`moltbook_chaos_log_v{1,2,3}_*.md`
- 統計分析：`moltbook_chaos_analysis_v{1,2,3}_*.md`
- **綜合分析報告**：[Moltbook 多智能體實驗：混沌與異見者傳播綜合分析報告.md](./Moltbook%20多智能體實驗：混沌與異見者傳播綜合分析報告.md)

---

## 📄 授權
MIT License
---

**⚠️ 研究倫理聲明**：本實驗僅個人測試，探討 AI 安全領域的對齊問題。
