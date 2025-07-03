VSCode Insiders/GitHub Copilot/GPT-4.1/PlanFirst:

1. 我要以 Python 建立自動翻譯工具，滿足以下要求:

- 需要輸入一個路徑，若僅是資料夾名稱，則需要翻譯全部檔案，也可使用 glob 模式指定檔名比對樣式。
- 它會呼叫 OpenAI 相容的 LLM 進行翻譯。
- 可以輸入一個選擇性參數，指定同時 API 呼叫數量，若未指定則設為 1。
- 請使用預先提供的 #file:system.md 當系統提示。
- 使用者提示使用 "Your task is to translate the following text into zh-tw:\n{text}"。
- 請先為我提供預設為 GitHub Model 的 endpoint "https://models.github.ai/inference"，LLM 模型名稱用 "openai/gpt-4.1-mini"，及 API 金鑰範例，放在 .env.example 檔案中，我會自行撰寫 .env 填寫正確的模型及金鑰。

2. 改用 OpenAI SDK 的 Responses API 實作。
3. 我不要支援 glob 模式了，我僅要指定資料夾方法。另外可增加選擇性參數，指定檔名比對模式。輸出檔請放在與目標資料夾同層級的 {folder}_zh-tw 資料夾中，若不存在則建立。若存在則清空資料夾後再寫入。
4. 我要再修改為 OpenAI SDK 的 Chat Completions API 實作。
5. 請更新 README.md，說明這個工具的用途，如何使用這個工具，並以 sample 為輸入資料夾，提供範例。授權為 MIT。