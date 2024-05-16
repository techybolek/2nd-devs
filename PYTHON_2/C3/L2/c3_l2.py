import requests
import json

from dotenv import load_dotenv
load_dotenv()

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util

the_task, task_token = task_util.get_task('scraper')
print(the_task, task_token)
import requests
from bs4 import BeautifulSoup

the_url = the_task['input']
print('URL:', the_url)
the_question = the_task['question']
print('Question:', the_question)

response = requests.get(the_url,  headers={"User-Agent": "Chrome"})
#response = requests.get(the_url,  headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
system_prompt = the_task['msg'] + '\n###Article:' + soup.prettify() + '\n###'
user_prompt = the_task['question']
the_answer = task_util.get_oai_answer(user_prompt, system_prompt)
print('Answer:', the_answer)
task_util.submit_task(the_answer, task_token)
