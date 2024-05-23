import os
import sys


# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util

def oai_answer_api(user_prompt):
   system_prompt =  """You are a helpful assistant. Answer truthfully and concisely. Fact: today is 05/23/2024"""
   resp = task_util.get_oai_answer(user_prompt, system_prompt)
   return resp

if __name__ == '__main__':
  user_prompt = """Does anxiety impair efficacy?"""
  resp = oai_answer_api(user_prompt)
  print(resp)

