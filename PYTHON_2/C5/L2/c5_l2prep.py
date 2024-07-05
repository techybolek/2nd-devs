import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util

the_task, task_token = task_util.get_task('optimaldb')
print(the_task, task_token)

#url = "https://tasks.aidevs.pl/data/3friends.json"
url = the_task['database']
print('url:', url)

#read the entire JSON content at the above url using the request module
import requests
response = requests.get(url)
data = response.json()

import json
with open('3friends.json', 'w') as f:
    json.dump(data, f)

system_prompt = """Below you have information about three people.
Without losing any details, transform it to make it more compact,
so that the total content size shrinks at least by three times.
Important: do not lose any details, not a single piece of information!
"""

#stringify the data
data = json.dumps(data)
resp = task_util.get_oai_answer(data, system_prompt)
print(resp)

with open('3friends_compact.txt', 'w') as f:
    json.dump(data, f)

task_util.submit_task(resp, task_token)