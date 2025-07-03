# mass-translate

## 工具用途

`mass-translate` 是一個以 Python 實作的自動翻譯工具，可批次將指定資料夾內的檔案（如 Markdown、純文字等）透過 OpenAI 相容 LLM API 翻譯為繁體中文（zh-tw）。

## 安裝方式

1. 複製本專案原始碼。
2. 安裝相依套件：
   ```sh
   pip install -r requirements.txt
   ```
3. 參考 `.env.example` 建立 `.env`，填入您的 API 端點、模型名稱與金鑰。

## 使用方式

```sh
python translate.py <來源資料夾> [--pattern <檔名比對模式>] [--concurrency <同時 API 呼叫數>]
```

- `<來源資料夾>`：要翻譯的資料夾路徑（必填）
- `--pattern`：檔名比對模式（如 `*.md`，預設為全部檔案）
- `--concurrency`：同時 API 呼叫數量，預設為 1

### 範例

假設有一個名為 `sample` 的資料夾，內含多個檔案，執行：

```sh
python translate.py sample --pattern *.md --concurrency 2
```

翻譯結果將輸出至與 `sample` 同層級的 `sample_zh-tw` 資料夾，結構與原始資料夾相同。

## 授權

MIT License
