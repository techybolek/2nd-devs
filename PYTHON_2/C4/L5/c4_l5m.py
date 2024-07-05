import json
import os
import sys


# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util

tools = [
    {
        "type": "function",
        "function": {
            "name": "add_to_knowledge_base",
            "description": "Add information to knowledge base",
            "parameters": {
                "type": "object",
                "properties": {
                    "info": {
                        "type": "string",
                        "description": "The information to be added to the knowledge base",
                    },
                },
                "required": ["info"],
            },
        }
    }
]

knowledge_base = '\n## Knowledge Base:##'

def add_to_knowledge_base(info):
    print('Adding to knowledge base: ', info)
    global knowledge_base
    knowledge_base += "\n" + info
    #print("Updated knowledge base: ", knowledge_base)
   
def oai_answer_api(user_prompt):
   global knowledge_base
   system_prompt =  """You are a helpful assistant with a custom knowledge base. If the user explicitely asks a question, answer it truthfully and concisely. If the user appears to be sharing information and not explicitely asking a question, add it to your knowledge base.""" + knowledge_base
   print('System Prompt:\n', system_prompt, '\n')
   resp = task_util.get_oai_answer(user_prompt, system_prompt, tools)
   #print('Response: ', resp)
   if 'tool_calls' in resp:
       func = resp['tool_calls'][0]['function']
       #print('Function: ', func)
       if func['name'] == 'add_to_knowledge_base':
          info = json.loads(func['arguments'])['info']
          #print('Info:', info)
          add_to_knowledge_base(info)
          resp = "Ok, got it"
   else:
       resp = resp['content']
   return resp

if __name__ == '__main__':
  while True:
    user_prompt = input("Enter a prompt: ")
    if user_prompt == "":
      break
    resp = oai_answer_api(user_prompt)
    print("Response: ", resp)