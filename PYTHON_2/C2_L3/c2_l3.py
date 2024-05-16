import requests
import json

from dotenv import load_dotenv
load_dotenv()

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util



URL = "https://api.openai.com/v1/embeddings"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = { "Authorization": "Bearer " + OPENAI_API_KEY }

model = "text-embedding-ada-002"

data = {
    "model": model,
    "input": "Hawaian Pizza"
}

response = requests.post(URL, json=data, headers=headers, verify=False)
print(response)

parsed_response = json.loads(response.text)
#print(parsed_response)
emb = parsed_response["data"][0]["embedding"]
print(emb)

the_task, task_token = task_util.get_task('embedding')
print(the_task, task_token)
task_util.submit_task(emb, task_token)