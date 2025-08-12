# Step 02 — Page Extract (OWASP GenAI)

## 📌 Overview
This program uses a **Notte browser agent** to visit [https://genai.owasp.org](https://genai.owasp.org) and extract structured metadata:

- `title` — Page title
- `intro` — One-sentence summary of the page
- `key_links` — Absolute URLs for:
  - `resources`
  - `initiatives`
  - `blog`
  - `events`

### Key Constraints
- Navigation restricted to `genai.owasp.org`
- No form submissions or file downloads
- Maximum 5 agent steps per run
- JSON schema is strictly defined in the prompt
- Read-only navigation (no tool execution enabled)

---

## ⚙️ Setup

### 1. Prerequisites
- Python **3.11+**
- [Notte](https://github.com/nottelabs/notte) installed
- Virtual environment configured

### 2. Installation
```bash
# Create and activate virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install notte python-dotenv patchright

# Install Chromium for Playwright/Notte
patchright install --with-deps chromium
````

### 3. Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...
NOTTE_MODEL=openai/gpt-4o-mini
```

> **Security Note:**
> Do not commit `.env` to version control.
> Keep your API keys secret and rotate them if compromised.

---

## ▶️ Running the Agent

```bash
source .venv/bin/activate
python step02_page_extract.py
```

The browser will:

1. Open `https://genai.owasp.org`
2. Extract `title`, `intro`, and `key_links`
3. Print the JSON output to the console
4. Wait for you to press **Enter** before closing

---

## 📄 Example Output

```json
{
  "title": "Home - OWASP Gen AI Security Project",
  "intro": "The OWASP GenAI Security Project aims to provide guidance and resources for understanding and mitigating security concerns related to Generative AI applications.",
  "key_links": {
    "resources": "https://genai.owasp.org/resources/",
    "initiatives": "https://genai.owasp.org/initiatives/",
    "blog": "https://genai.owasp.org/blog/",
    "events": "https://genai.owasp.org/events/"
  }
}
```

---

## 🔐 Security Documentation

A detailed **threat model** for this step is available in [THREAT\_MODEL.md](./step02_article_ectract-ThreatModel.md), following the OWASP Agentic AI Threat Taxonomy (TIDs).