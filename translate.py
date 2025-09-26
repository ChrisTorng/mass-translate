import os
import shutil
import fnmatch
import argparse
import concurrent.futures
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 載入 .env 設定
load_dotenv()
ENDPOINT = os.getenv('ENDPOINT')
MODEL = os.getenv('MODEL')
API_KEY = os.getenv('API_KEY')

# 設定 openai 參數
client = OpenAI(
    base_url=ENDPOINT,
    api_key=API_KEY,
)
# 讀取 system.md 作為系統提示
SCRIPT_DIR = Path(__file__).resolve().parent
SYSTEM_PROMPT_PATH = SCRIPT_DIR / 'system.md'
if not SYSTEM_PROMPT_PATH.is_file():
    raise FileNotFoundError(f"找不到系統提示檔案: {SYSTEM_PROMPT_PATH}")

with SYSTEM_PROMPT_PATH.open('r', encoding='utf-8') as f:
    SYSTEM_PROMPT = f.read()

USER_PROMPT_TEMPLATE = "Your task is to translate the following text into zh-tw:\n{text}"


def get_file_list(folder, pattern):
    matched_files = []
    for root, _, files in os.walk(folder):
        for fname in files:
            if pattern is None or fnmatch.fnmatch(fname, pattern):
                matched_files.append(os.path.join(root, fname))
    return matched_files


def translate_text(text):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)}
        ]
    )
    return response.choices[0].message.content


def process_file(filepath, src_folder, out_folder):
    rel_path = os.path.relpath(filepath, src_folder)
    out_path = os.path.join(out_folder, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    translated = translate_text(content)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    print(f"已翻譯: {filepath} -> {out_path}")


def main():
    import fnmatch
    parser = argparse.ArgumentParser(description='自動翻譯工具')
    parser.add_argument('folder', help='來源資料夾路徑')
    parser.add_argument('--pattern', type=str, default=None, help='檔名比對模式 (如 *.md)，預設全部檔案')
    parser.add_argument('--concurrency', type=int, default=1, help='同時 API 呼叫數量，預設為 1')
    args, unknown = parser.parse_known_args()

    if unknown:
        parser.error(
            '偵測到額外參數: {}\n如果你要使用萬用字元，請在 shell 中以引號包住，例如 --pattern "*.md"'.format(' '.join(unknown))
        )

    src_folder = os.path.abspath(args.folder)
    if not os.path.isdir(src_folder):
        print('來源資料夾不存在')
        return

    out_folder = src_folder.rstrip(os.sep) + '_zh-tw'
    out_folder = os.path.join(os.path.dirname(src_folder), os.path.basename(out_folder))
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.makedirs(out_folder, exist_ok=True)

    file_list = [f for f in get_file_list(src_folder, args.pattern) if os.path.isfile(f)]
    if not file_list:
        print('找不到任何檔案')
        return

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = [executor.submit(process_file, f, src_folder, out_folder) for f in file_list]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == '__main__':
    main()
