import requests
import json

from dotenv import load_dotenv
load_dotenv()

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util
from openai import OpenAI

the_task, task_token = task_util.get_task('whisper')
print(task_token)

client = OpenAI()

audio_file = open("/mnt/c/temp/mateusz.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
print(transcription)
task_util.submit_task(transcription, task_token)


#response = requests.post(URL, json=data, headers=headers, verify=False)
#print(response)

#parsed_response = json.loads(response.text)
#print(parsed_response)
#emb = parsed_response["data"][0]["embedding"]
#print(emb)
