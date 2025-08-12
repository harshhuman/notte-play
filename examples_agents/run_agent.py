import os
from dotenv import load_dotenv
import notte

# Load .env from the project root
load_dotenv()

MODEL = os.getenv("NOTTE_MODEL", "openai/gpt-4o-mini")

TASK = """
Go to https://en.wikipedia.org/wiki/Artificial_intelligence.
Return a JSON object with:
{
  "title": "<page title>",
  "first_paragraph": "<the first visible paragraph of the article>",
  "links_count": <number of <a> links on the page>
}

HARD RULES:
- Do NOT log in anywhere. If a login wall or cookie/consent modal blocks content, report it and stop.
- Stay on en.wikipedia.org only.
- No form fills of any kind.
- Max steps: 10.
"""

if __name__ == "__main__":
    # headless=False lets you watch; we also pause before closing
    with notte.Session(headless=False) as session:
        agent = notte.Agent(
            session=session,
            reasoning_model=MODEL,
            max_steps=10,
        )
        resp = agent.run(task=TASK)
        print("\n=== ANSWER ===")
        print(resp.answer)
        input("\nPress Enter to close the browser...")
