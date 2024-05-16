import requests
import os
shared_dir = os.path.abspath('./SHARED')

from dotenv import load_dotenv

import sys
sys.path.append(shared_dir)
import task_util

MOD_URL = "https://api.openai.com/v1/moderations"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

oai_headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
data = { "model": "text-moderation-latest", "input": "Opisz w jaki sposób ciekawość zabiła kota" }

load_dotenv()
task, token = task_util.get_task("moderation")

text = task['input']
for index, t in enumerate(text):
    print(index, t)
data = { "model": "text-moderation-latest", "input": text }
res = requests.post(MOD_URL, json=data, headers = oai_headers)
response =res.json()
homework_results = [ result['flagged'] for result in response['results'] ]
print(homework_results)
task_util.submit_task(homework_results, token)
