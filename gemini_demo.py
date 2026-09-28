import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found.")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Artificial Intelligence in simple words."
)

# Display response
print("\n===== Google Gemini Response =====")
print(response.text)