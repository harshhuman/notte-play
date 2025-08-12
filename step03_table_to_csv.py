import os
from dotenv import load_dotenv; load_dotenv()
import notte

# Ensure output folder exists
os.makedirs("out", exist_ok=True)

MODEL = os.getenv("NOTTE_MODEL", "openai/gpt-4o-mini")
print(f"Using model: {MODEL}")

TASK = """
Go to https://en.wikipedia.org/wiki/List_of_programming_languages.
Extract the first visible table into CSV with columns: name, link, notes (if present).
Write the file to ./out/programming_langs.csv (overwrite if exists).
Limit to about 40 rows max to reduce token usage.

Return JSON:
{
  "rows_exported": <number>,
  "sample": ["<first 5 language names>"]
}

Rules:
- Stay on en.wikipedia.org only.
- Avoid footer or navigation tables.
- No forms or downloads other than the CSV you write locally.
- Max steps: 8.
"""

if __name__ == "__main__":
    with notte.Session(headless=False) as s:
        a = notte.Agent(session=s, reasoning_model=MODEL, max_steps=8)
        r = a.run(task=TASK)
        print("\n=== ANSWER ===")
        print(r.answer)
        print("CSV saved to: out/programming_langs.csv")
        input("\nPress Enter to close...")
