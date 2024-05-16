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

system_prompt = "You are an expert at Open AI API. You help the user dynamically generate function definitions for the gpt-4 and gpt-3.5 models."
user_prompt = """Create a function for gpt-4 addUser that require 3 params: name (string), surname (string) and year of birth in field named 'year'
(integer). Set type of function to 'object'"""

function_def = {
            "name": "addUser",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The first name of the user to be added"
                    },
                    "surname": {
                        "type": "string",
                        "description": "The surname of the user to be added"
                    },
                    "year": {
                        "type": "integer",
                        "description": "The year of birth"
                    }
                }
            }
        }

the_task, task_token = task_util.get_task('functions')
print(the_task, task_token)
task_util.submit_task(function_def, task_token)
