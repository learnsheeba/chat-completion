# Instructions
1. Assuming vscode and python installations are in place.
1. In command prompt `git init <folder-name>`
1. `cd <folder-name>`
1. `python -m pip install venv`
1. `python -m venv venv` creates virtual environment for this project folder
1. `venv\Scripts\activate` activates virtual environment
1. `pip install openai` installs OpenAI SDK
1. `pip install python-dotenv` installs python package to load .env contents to program
1. create a file name `.env` and add the contents from `.envSample`
1. Add OPENAI_API_KEY to .env file, after creating API Key from [Open AI](https://platform.openai.com/api-keys)
    + OPENAI_API_KEY = your-api-key
1. From [OpenAI Chat Completion API](https://developers.openai.com/api/docs/quickstart?desktop-os=windows&language=python) refer initial python code snippet to test.

**Example code**

```
from openai import OpenAI, api_key
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

```

1. `py exercise-01.py` run the command in terminal window to see the result
