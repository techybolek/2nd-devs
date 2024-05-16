import json
import re

from dotenv import load_dotenv
load_dotenv()

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util


def parse_answer(text):
    # Regular expression to find JSON objects
    json_objects = re.findall(r'\{.*?\}', text, flags=re.S)
    json_parsed = []

    # Try to parse each JSON object
    for obj in json_objects:
        try:
            json_parsed.append(json.loads(obj))
        except json.JSONDecodeError:
            print(f"Failed to parse: {obj}")
            raise
    
    answer = json_parsed[0]['person']
    return(answer)

system_prompt = """
Your job is to identify the person based on a hint.
If the hint is insufficient to pin-point a person beyond any doubt, you answer "I don't know".
After you have identified the person, take a deep breath and re-examine your train of thought and the conclusion. 
If you are not 100% sure that someone else might also fit the criteria, you answer "I don't know". If there is even the slightest chance there might be someone else out there who could also fith the criteria, you answer "I don't know" 
Important: only return the person's name if there is absolutely no way anyone else might qualify.  It's better to say "I don't know" than to jump to conclusions! If you guess incorrectly, you will be punished! On the other hand, if you say "I don't know", you will be given additional hint that will help you identify the person. Therefore there is absolutely no need for rush. Just relax and say "I don't know", unless you are 100% sure you've got the correct answer.
Explain your reasoning step-by-step.
Return the answer in JSON: { "person": <name>|"I don't know" }
"""

compound_hint = ''
while True:
  the_task, task_token = task_util.get_task('whoami')
  print(the_task, task_token)

  hint = the_task['hint']
  print('Hint:', hint)
  compound_hint = compound_hint + hint
  resp = task_util.get_oai_answer(compound_hint, system_prompt)
  print(resp)
  the_answer = parse_answer(resp)
  print("Parsed Answer:", the_answer)
  if the_answer != "I don't know":
    task_util.submit_task(the_answer, task_token)
    break
