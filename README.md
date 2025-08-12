# Notte Agent Example

This is a simple example of using the Notte agent to automate web browsing tasks.

## Setup

1. **Install dependencies** (if not already done):
   ```bash
   pip install notte
   ```

2. **For basic browser automation (no API key needed)**:
   ```bash
   python run_agent_simple.py
   ```

3. **For advanced features (requires OpenAI API key)**:
   - Go to https://platform.openai.com/api-keys
   - Create a new API key
   - Set your API key:
     ```bash
     # Temporary (for this session only)
     export OPENAI_API_KEY="your-api-key-here"
     
     # Permanent (add to your shell profile)
     echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
     source ~/.zshrc
     ```
   - Run the setup check: `python setup.py`
   - Run the full agent: `python run_agent.py`

## Usage

**Simple mode (no API key required)**:
```bash
python run_agent_simple.py
```

**Full mode (requires OpenAI API key)**:
```bash
python run_agent.py
```

## What it does

The agent will:
1. Open a browser window
2. Navigate to https://example.com
3. Extract the page title and count the number of links
4. Return the results as JSON

## Troubleshooting

### "Invalid API key" error
- Make sure your API key is correct
- Check that the environment variable is set: `echo $OPENAI_API_KEY`
- Get a new key from https://platform.openai.com/api-keys

### "No module named 'notte'" error
- Activate your virtual environment: `source .venv/bin/activate`
- Install notte: `pip install notte`

### Browser issues
- The agent runs in non-headless mode by default so you can see what's happening
- Make sure you have a modern browser installed (Chrome/Chromium recommended)
