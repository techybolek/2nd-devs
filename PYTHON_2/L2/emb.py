import requests
import os

EMB_URL="https://api.openai.com/v1/embeddings"

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
oai_headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
data = { "model": "text-embedding-3-small", "input": "Jesteś Bolek" }

res = requests.post(EMB_URL, json=data, headers=oai_headers)
print(res)
print(res.json())
