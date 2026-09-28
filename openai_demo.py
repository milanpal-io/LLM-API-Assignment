import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OpenAI API key not found.")
    exit()

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send prompt to GPT
response = client.responses.create(
    model="gpt-5",
    input="Explain Artificial Intelligence in simple words."
)

# Display response
print("\n===== OpenAI GPT Response =====")
print(response.output_text)