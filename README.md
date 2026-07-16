# FastAPI Hello API for Render

這是一個實作了簡單 `/` 回傳 `"Hello"` 以及 `/health` 健康檢查端點的 FastAPI 應用程式，專為部署到 Render 平台而設計。

## 專案結構

- [main.py](file:///c:/Users/Yufang/Desktop/render_test/main.py): FastAPI 主程式
- [requirements.txt](file:///c:/Users/Yufang/Desktop/render_test/requirements.txt): Python 套件依賴清單
- [render.yaml](file:///c:/Users/Yufang/Desktop/render_test/render.yaml): Render Blueprint 設定檔（可用於自動建立服務）

---

## 本地端開發與測試

### 1. 建立虛擬環境並安裝依賴

```bash
# 建立虛擬環境
python -m venv venv

# 啟用虛擬環境
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt
```

### 2. 啟動本地伺服器

```bash
uvicorn main:app --reload
```

啟動後即可透過瀏覽器或 API 測試工具訪問：
- API 首頁（回傳 Hello）：`http://127.0.0.1:8000/`
- 健康檢查：`http://127.0.0.1:8000/health`
- 自動產生的 API 文件：`http://127.0.0.1:8000/docs`

---

## 部署到 Render

您可以選擇以下兩種方式之一來部署至 Render：

### 方法 A：使用 Render Blueprint (推薦，最快速)

1. 將此專案推送至您的 GitHub 或 GitLab 儲存庫。
2. 登入 [Render Dashboard](https://dashboard.render.com/)。
3. 點選 **Blueprints** -> **New Blueprint Instance**。
4. 連接您的專案儲存庫，Render 會自動讀取 `render.yaml` 並設定服務。
5. 點選 **Approve** 開始部署。

### 方法 B：手動建立 Web Service

1. 將此專案推送至您的 GitHub 或 GitLab 儲存庫。
2. 登入 [Render Dashboard](https://dashboard.render.com/)。
3. 點選 **New +** -> **Web Service**。
4. 連接您的專案儲存庫。
5. 填寫以下設定：
   - **Name**: `fastapi-hello-service` (或自訂名稱)
   - **Language**: `Python`
   - **Branch**: `main` (或您的主要分支)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. 點選 **Create Web Service** 開始部署。
