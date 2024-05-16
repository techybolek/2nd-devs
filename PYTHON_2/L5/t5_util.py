import requests
import json

import os

from urllib3 import encode_multipart_formdata
from dotenv import load_dotenv
import sys

BASE_URL = "https://tasks.aidevs.pl/"
HEADERS = {'Content-Type': 'application/json'}
TASK_MODERATION = "moderation"
TASK_HELLO = "helloapi"
TASK_LIAR = "liar"

def submit_task(answer, token):
  url = BASE_URL + "/answer/" + token
  data = {"answer": answer }
  res = requests.post(url, data = json.dumps(data), headers = HEADERS, verify=False )
  print("submit result:", res)
  response = json.loads(res.text)
  print('submit response:', response)


def get_answer(question):
  task_name = 'liar'
  url = BASE_URL+ "token/" + task_name
  data = {"apikey": os.getenv("AIDEVS_API_KEY")}

  response = requests.post(url, data=json.dumps(data), headers=HEADERS, verify=False)
  parsed_response = json.loads(response.text)
  
  token = parsed_response['token']

  url = BASE_URL + "/task/" + token
  
  fields = {
    "question": question
  }
  body, header = encode_multipart_formdata(fields)
  print(body)
  print(header)
  
  response = requests.post(url, data = body, headers = { 'content-type': header }, verify=False)
  parsed_response = json.loads(response.text)
  return parsed_response['answer'], token
