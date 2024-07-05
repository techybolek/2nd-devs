import json
import os
import sys
from datetime import datetime

import requests


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
            "name": "search",
            "description": "search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_string": {
                        "type": "string",
                        "description": "The search string",
                    },
                },
                "required": ["search_string"],
            },
        }
    }
]

def search_web(info):
    print('Searching the web for: ', info)
    search_url = "https://serpapi.com/search"
    api_key = os.getenv('SERP_API_KEY')
    print('API Key:', api_key)
    search_url += "?q=" + info + '&api_key=' + api_key
    headers = {'Accept': 'application/json'}  # Set Accept header if needed
    response = requests.get(search_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            json_resp = response.json()
            return json_resp['organic_results'][0]['link']
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print("Error decoding JSON")
            print("Response content:", response.text)  # Print raw response text for debugging
            return None
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.text)  # Print raw response text for debugging
        return None
   
def oai_answer_api(user_prompt):
   global knowledge_base
   system_prompt =  """You are a helpful assistant capable for searching the web for the most up-to-date information.
   Answer truthfully and ultra-concisely.
   Fact: today is: """ + datetime.now().strftime('%Y-%m-%d')
   
   
   print('System Prompt:\n', system_prompt, '\n')
   resp = task_util.get_oai_answer(user_prompt, system_prompt, tools)
   #print('Response: ', resp)
   if 'tool_calls' in resp:
       func = resp['tool_calls'][0]['function']
       #print('Function: ', func)
       if func['name'] == 'search':
          search_string = json.loads(func['arguments'])['search_string']
          #print('Info:', info)
          resp = search_web(search_string)
          print('response from web:', resp) ##summarize
   else:
       resp = resp['content']
   return resp

if __name__ == '__main__':
  from dotenv import load_dotenv
  load_dotenv()
  
  while True:
    user_prompt = input("Enter a prompt: ")
    if user_prompt == "":
      break
    resp = oai_answer_api(user_prompt)
    print("Response: ", resp)