from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

# Initialize client
client = OpenAI(api_key=api_key)

# Send a simple test request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

# Print the result
print("✅ API call succeeded.")
print("Model response:", response.choices[0].message.content)
