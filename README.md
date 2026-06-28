# 🐻 Master of GYM 健身大師

> 你的口袋裡的 AI 健身教練，由熊大大陪你練、吃、睡。

![PWA](https://img.shields.io/badge/PWA-Ready-orange?logo=pwa)
![React](https://img.shields.io/badge/React-18-blue?logo=react)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ 核心功能

### 🐻 熊大大 AI 教練
- 體能評測（性別、年齡、身高、體重、體脂、目標）
- 根據目標自動生成個人化週課表與飲食建議
- TDEE 計算（Harris-Benedict 公式），動態調整熱量目標
- 熊大大情緒系統：好感度影響表情（❤️ 😊 😠 🔥）
- 本週訓練報告、快速對話回覆

### 💪 訓練課表
20 套課表，涵蓋三個難度 × 兩種場景：

| | 入門 | 中級 | 進階 |
|---|---|---|---|
| 居家 | 上肢、下肢、核心、燃脂 | 上肢、下肢、核心、HIIT | 推力、全身爆發 |
| 健身房 | 推、拉、腿 | 胸、背、腿臀、肩 | 大三項、引體、爆發力 |

- 難度篩選（入門 / 中級 / 進階）
- 動作說明、組數、次數、休息時間、技巧提示
- 訓練完成記錄進度頁

### 🏋️ 器材百科
100 種器材完整資料：

| 分類 | 數量 |
|---|---|
| 固定軌道機器 | 多項 |
| 自由重量 | 多項 |
| 有氧器材 | 多項 |
| 複合器材 | 多項 |
| 輔助器材 | 多項 |
| 核心訓練器材 | 多項 |
| 爆發力訓練器材 | 多項 |
| 徒手器材 | 多項 |

每項器材包含：難度、強度、危險係數、目標肌群、詳細說明、使用方法、步驟、技巧。首次進入時可選擇下載快取（含進度百分比顯示）。

### 🥗 飲食記錄
- 139 筆食物資料庫（主食、蛋白質、蔬果、堅果、乳製品、補給品）
- 超商食物快捷入口（🏪 共 66 筆，涵蓋 7-11 / 全家 / 萊爾富常見品項）
- 份量調整（×0.5 / ×1 / ×1.5 / ×2 或自訂）
- 個人化 TDEE 熱量目標，即時顯示赤字 / 盈餘
- 七日飲食趨勢圖（熱量 + 蛋白質折線）
- 早餐 / 午餐 / 晚餐 / 點心分類記錄

### 😴 睡眠記錄
- 每天首次開啟 Coach 頁時出現晨間卡片
- 一秒完成：昨晚睡幾小時？`[5h] [6h] [7h] [8h] [9h] [略過]`
- 熊大大根據睡眠時數動態建議（＜6h 降強度，≥8h 全力衝）
- 本週平均睡眠顯示於週報告

### 📊 進度追蹤
- 體重趨勢圖（最近 30 筆）
- 訓練紀錄列表
- 熱力圖（365 天訓練頻率視覺化）
- 徽章系統（首次訓練、連續打卡、累積里程碑等）

---

## 🛠 技術架構

```
單一 HTML 檔案，零後端，零建置工具
```

| 技術 | 用途 |
|---|---|
| React 18（CDN） | UI 框架 |
| Babel Standalone | 瀏覽器即時 JSX 編譯 |
| Tailwind CSS（CDN） | 樣式 |
| Service Worker v3 | PWA 離線快取（Cache-First） |
| localStorage | 所有用戶資料本地持久化 |

### localStorage 資料結構

| Key | 內容 |
|---|---|
| `gym_coach` | 用戶體能資料與目標 |
| `gym_records` | 訓練、體重、睡眠紀錄 |
| `gym_diet` | 每日飲食日誌 |
| `gym_affection` | 熊大大好感度 |
| `gym_favorites` | 收藏的器材 |
| `gym_theme` | 主題（dark / light） |
| `gym_equip_cached` | 器材百科快取狀態 |

---

## 🚀 快速開始

```bash
# clone 專案
git clone https://github.com/blackbear007-maker/BearBigBig.git
cd BearBigBig

# 直接用瀏覽器開啟（需 HTTPS 才能啟用 Service Worker）
# 本地可用 Live Server 或任何靜態伺服器
npx serve .
```

或直接部署到 GitHub Pages：
**Settings → Pages → Source → main branch / root**

---

## 📱 安裝為 PWA

在手機瀏覽器開啟網址後：

- **iOS Safari**：點右下角分享 → 加入主畫面
- **Android Chrome**：點網址列右側選單 → 安裝應用程式

安裝後完全離線可用。

---

## 📁 檔案結構

```
BearBigBig/
├── index.html      # 完整應用（含所有 React 元件、資料、樣式）
├── manifest.json   # PWA manifest
├── sw.js           # Service Worker（Cache-First 策略）
└── README.md
```

---

## 🗺 應用地圖

```
App
├── 🐻 Coach（教練）
│   ├── 晨間睡眠記錄卡片
│   ├── 熊大大 Dashboard
│   ├── 個人化週課表
│   ├── 飲食重點建議
│   ├── 本週訓練報告
│   └── 快速對話
├── 💪 Train（訓練）
│   ├── 居家 / 健身房切換
│   ├── 難度篩選（入門 / 中級 / 進階）
│   ├── 課表列表
│   └── 訓練動作 Modal
├── 🏋️ Equip（器材百科）
│   ├── 分類篩選（9 類）
│   ├── 難度 / 強度 / 危險度標示
│   └── 器材詳細資料頁
├── 🥗 Diet（飲食）
│   ├── 新增飲食（搜尋 + 超商快捷）
│   ├── 份量調整 Modal
│   ├── 今日明細
│   └── 七日趨勢
└── 📊 Progress（進度）
    ├── 訓練紀錄
    ├── 體重追蹤
    ├── 熱力圖
    └── 徽章
```

---

## License

MIT © 2026 blackbear007-maker
