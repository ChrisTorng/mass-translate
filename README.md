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
python translate.py <來源資料夾> [--pattern <檔名比對模式>] [--concurrency <同時 API 呼叫數>] [--delay <等待秒數>] [--output-folder <輸出資料夾>]
```

- `<來源資料夾>`：要翻譯的資料夾路徑（必填）
- `--pattern`：檔名比對模式（如 `*.md`，預設為全部檔案）
- `--concurrency`：同時 API 呼叫數量，預設為 1
- `--delay`：每次 API 呼叫之間等待的秒數，預設為 1 秒，可設定為 0 或其他浮點數以微調限速
- `--output-folder`：輸出資料夾路徑，預設為 `<來源資料夾>_zh-tw`

> 小提醒：若在 shell 中使用萬用字元（如 `*.md`），請以引號包住，避免參數在進入程式前被展開。

### 範例

假設有一個名為 `sample` 的資料夾，內含多個檔案，執行：

```sh
python translate.py sample --pattern "*.md" --concurrency 2 --delay 1.5
```

翻譯結果預設輸出至與 `sample` 同層級的 `sample_zh-tw` 資料夾，結構與原始資料夾相同；如需指定其他目標，加入 `--output-folder /path/to/your/dir` 即可。

## 授權

MIT License
