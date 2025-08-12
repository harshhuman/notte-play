from dotenv import load_dotenv; load_dotenv()
import notte
import os

MODEL = os.getenv("NOTTE_MODEL", "openai/gpt-4o-mini")
print(f"Using model: {MODEL}")

TASK = """
Go to https://genai.owasp.org

Return JSON exactly in this shape (fill null if a section is not present):
{
  "title": "<page title>",
  "intro": "<one-sentence summary of what this page is about>",
  "key_links": {
    "resources": "<absolute url or null>",
    "initiatives": "<absolute url or null>",
    "blog": "<absolute url or null>",
    "events": "<absolute url or null>"
  }
}

Extraction rules:
- Only include absolute URLs on genai.owasp.org.
- Prefer main body links (not footer/header duplicates) if both exist.
- If multiple candidates exist, pick the most prominent one.
- Do NOT return labels like "RESOURCES" — return the absolute URL.
- Once you have the four URLs (or nulls), STOP and produce the JSON. Do not self-criticize or retry.

Safety/scope:
- Stay on genai.owasp.org only.
- No forms, downloads, or navigation beyond the home page.
- Max steps: 5.
"""

if __name__ == "__main__":
    with notte.Session(headless=False) as s:
        a = notte.Agent(session=s, reasoning_model=MODEL, max_steps=5)
        r = a.run(task=TASK)
        print("\n=== ANSWER ==="); print(r.answer)
        input("\nPress Enter to close...")
