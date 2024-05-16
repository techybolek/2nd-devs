# make a request to openai
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = "https://api.openai.com/v1/chat/completions"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

url = BASE_URL 
headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
data = { "model": "gpt-4", "messages": [{"role": "user", "content": "How big is the Earth?"}] }

#response = requests.post(url, data=json.dumps(data), headers=headers)
response = requests.post(url, json=data, headers=headers)

# Parse JSON response
parsed_response = json.loads(response.text)

print(parsed_response)
