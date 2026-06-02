from openai import OpenAI
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the variables
openai_api_key = os.getenv("OPENAI_API_KEY")

print(openai_api_key)


client = OpenAI(
  api_key=openai_api_key
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
