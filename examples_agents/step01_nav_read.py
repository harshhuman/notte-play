from dotenv import load_dotenv; load_dotenv()
import notte

TASK = """
Go to https://genai.owasp.org
Return JSON: {"title":"<page title>","links_count":<int>}
Stay on genai.owasp.org; no forms; max steps: 5.
"""

if __name__ == "__main__":
    with notte.Session(headless=False) as s:
        a = notte.Agent(session=s, reasoning_model="openai/gpt-4o-mini", max_steps=5)
        r = a.run(task=TASK)
        print("\n=== ANSWER ==="); print(r.answer)
        input("\nPress Enter to close...")
