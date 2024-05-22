import requests
import json

import os
from dotenv import load_dotenv
load_dotenv()

import sys

BASE_URL = "https://tasks.aidevs.pl/"
HEADERS = {'Content-Type': 'application/json'}
TASK_MODERATION = "moderation"
TASK_HELLO = "helloapi"

def submit_task(answer, token):
  url = BASE_URL + "/answer/" + token
  data = {"answer": answer }
  res = requests.post(url, data = json.dumps(data), headers = HEADERS )
  print("submit result:", res)
  response = json.loads(res.text)
  print('submit response:', response)


def get_task(task_name):
  url = BASE_URL+ "token/" + task_name
  data = {"apikey": os.getenv("AIDEVS_API_KEY")}

  response = requests.post(url, data=json.dumps(data), headers=HEADERS)
  parsed_response = json.loads(response.text)
  
  token = parsed_response['token']

  url = BASE_URL + "/task/" + token
  response = requests.post(url)
  parsed_response = json.loads(response.text)
  return parsed_response, token

if __name__ == "__main__":
  load_dotenv()
  
  if len(sys.argv) > 1:
    task_name = sys.argv[1]
  else:
    task_name = TASK_HELLO
    
  get_task(task_name)


def get_oai_answer(user_prompt, system_prompt = None):
  
  BASE_URL = "https://api.openai.com/v1/chat/completions"
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
  url = BASE_URL 
  headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
  
  messages = []
  if system_prompt != None:
    messages = [{"role": "system", "content": system_prompt}]
  messages.append({"role": "user", "content": user_prompt})
  
  data = { "model": "gpt-4", "messages": messages }
  
  #response = requests.post(url, data=json.dumps(data), headers=headers)
  response = requests.post(url, json=data, headers=headers)#,verify=false
  
  # Parse JSON response
  parsed_response = json.loads(response.text)
  resp = parsed_response['choices'][0]['message']['content']
  
  return resp

def get_oai_answer_from_image(user_prompt, image_url):
  
  OAI_URL = "https://api.openai.com/v1/chat/completions"
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
  headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
  
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": user_prompt},
        {
          "type": "image_url",
          "image_url": {
            "url": image_url
          },
        },
      ],
    }
  ]
  
  data = { "model": "gpt-4o", "messages": messages }
  
  response = requests.post(OAI_URL, json=data, headers=headers)
  
  parsed_response = json.loads(response.text)
  #print(parsed_response)
  resp = parsed_response['choices'][0]['message']['content']
  print(resp)
  return resp
