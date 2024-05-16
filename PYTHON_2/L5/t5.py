from urllib3 import encode_multipart_formdata
import json
from dotenv import load_dotenv

import os
t5_dir = os.path.abspath('./t5_util')
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(t5_dir)
sys.path.append(shared_dir)

import task_util
import t5_util



def validate_response(the_question, answer):
  print(answer)
  system_prompt = '''You are a guardrail against LLM halucinations. You will be provided the LLM's response and the original user question.
  Your job is to validate whether the LLM response matches the user question.
  Return answer as a JSON "valid" field, YES if the answer is correct, NO otherwise.'''
  
 
  user_prompt = "User asked: " + the_question + "Model responded: " + answer
  resp = task_util.get_oai_answer(user_prompt, system_prompt)
  print('Verdict: ', resp)
  parsed_response = json.loads(resp)
  return parsed_response['valid']
  

if __name__ == "__main__":
  load_dotenv()
 
  the_question = "What's the capital of Poland?" 
  answer, token = t5_util.get_answer(the_question)
  print(answer)
  verdict = validate_response(the_question, answer)
  print('Submitting verdict:', verdict)
  t5_util.submit_task(verdict, token)
  #resp = task_util.get_oai_answer("How big is the Earth?", "You are an extremely funny assistant")