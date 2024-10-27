# CSV、JSON可視化分析API

這是一個用於CSV和JSON數據可視化分析的API專案,包含了一個基於Streamlit的Boston房價預測應用。本專案提供了強大的工具,可以輕鬆地處理、分析和可視化CSV和JSON格式的數據。

## 專案功能

- 支持CSV和JSON格式數據的讀取和解析
- 提供數據清理和預處理功能
- 實現多種數據分析方法
- 生成各種類型的數據可視化圖表
- RESTful API接口,方便與其他應用程序集成
- 包含一個基於Streamlit的Boston房價預測應用

## 快速開始

要快速開啟並運行這個專案，請按照以下步驟操作：

1. 克隆存儲庫（如果您還沒有這樣做）：
   ```
   git clone [您的存儲庫URL]
   cd [專案目錄名稱]
   ```

2. 創建並激活虛擬環境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安裝所需的依賴包：
   ```
   pip install -r requirements.txt
   ```

4. 運行Streamlit應用：
   ```
   streamlit run boston_housing_app.py
   ```

   注意：如果遇到 `StreamlitSetPageConfigMustBeFirstCommandError` 錯誤，請參考下方的"故障排除"部分。

5. 在瀏覽器中打開顯示的URL（通常是 http://localhost:8501）。

現在您應該可以看到Boston房價預測應用的界面，並可以開始使用了。

## 如何使用

### 1. 設置環境

1. 克隆此存儲庫到您的本地機器：
   ```
   git clone [您的存儲庫URL]
   cd [專案目錄名稱]
   ```

2. 創建並激活虛擬環境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安裝所需的依賴包：
   ```
   pip install -r requirements.txt
   ```

### 2. 運行Streamlit應用（Boston房價預測）

1. 在專案根目錄下，運行以下命令：
   ```
   streamlit run boston_housing_app.py
   ```

2. 打開瀏覽器，訪問顯示的URL（通常是 http://localhost:8501）。

3. 在應用界面中，您可以：
   - 調整各種房屋特徵的參數
   - 查看預測的房價結果
   - 探索數據可視化圖表

### 3. 使用API功能

1. 啟動API服務器（如果與Streamlit應用分開）：
   ```
   python api_server.py  # 假設您的API服務器文件名為api_server.py
   ```

2. 使用API端點：

   a. 上傳CSV或JSON文件：
   ```
   curl -X POST -F "file=@your_file.csv" http://localhost:5000/upload
   ```

   b. 獲取數據分析結果：
   ```
   curl "http://localhost:5000/analyze?file=your_file_name&type=analysis_type"
   ```

   c. 生成可視化圖表：
   ```
   curl "http://localhost:5000/visualize?file=your_file_name&type=chart_type"
   ```

3. 查看API響應，您將收到JSON格式的數據或圖表URL。

### 4. 數據分析和可視化

1. 準備您的CSV或JSON數據文件。

2. 使用API上傳您的數據文件。

3. 利用分析端點進行數據分析。

4. 使用可視化端點生成圖表。

5. 在Streamlit應用中探索預處理後的數據和生成的圖表。

### 5. 自定義和擴展

- 修改 `boston_housing_app.py` 以添加新的特徵或改變預測模型。
- 在API中添加新的分析方法或可視化類型。
- 根據您的需求自定義數據預處理步驟。

## 運行專案

運行Streamlit應用：
```
streamlit run boston_housing_app.py
```

具體的運行命令可能會根據專案的實際結構和使用的框架而有所不同。請參考專案中的具體說明或文檔。

## 退出虛擬環境

當您完成工作後,可以通過以下命令退出虛擬環境:
```
deactivate
```

##注意事項

- 請始終在啟動虛擬環境的情況下進行開發和運行專案。
- 定期更新 requirements.txt 文件以保持依賴列表的最新狀態。
- 不要將 venv 目錄添加到版本控制系統中。
- 在使用API之前,請確保您已經正確配置了所有必要的設置和參數。

## 故障排除

如果您在運行 `boston_housing_app.py` 時遇到 `StreamlitSetPageConfigMustBeFirstCommandError` 錯誤，請按照以下步驟修改文件：

1. 打開 `boston_housing_app.py` 文件。

2. 確保 `st.set_page_config()` 是文件中的第一個 Streamlit 命令。將文件的開頭部分修改為如下所示：

   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np
   # 其他必要的導入

   # 確保這是第一個 Streamlit 命令
   st.set_page_config(page_title="波士頓房價分析與預測", layout="wide")

   # 其他代碼...
   ```

3. 保存文件並重新運行應用程序：

   ```
   streamlit run boston_housing_app.py
   ```

如果您仍然遇到問題，請檢查是否有其他 Streamlit 命令（如 `st.write()`, `st.title()` 等）在 `st.set_page_config()` 之前，或者是否有任何條件語句或函數定義包裹著 `st.set_page_config()`。它應該在全局範圍內直接調用。

## 貢獻

歡迎提交問題報告和改進建議。如果您想為這個專案做出貢獻,請遵循標準的Git工作流程提交拉取請求。

## 授權

本專案採用 MIT 授權協議。詳情請參閱 [LICENSE](LICENSE) 文件。
