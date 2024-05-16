import requests
import json
from dotenv import load_dotenv

BASE_URL = "https://tasks.aidevs.pl/"
TASK_MODERATION:$
= "moderation"
TASK_HELLO = "helloapi"
url = BASE_URL+ "token/" + TASK
headers = {'Content-Type': 'application/json'}
data = {"apikey": "b887d478-8250-4c81-b509-b0bdc860b77c"}

response = requests.post(url, data=json.dumps(data), headers=headers)

# Parse JSON response
parsed_response = json.loads(response.text)

print(parsed_response)
token = parsed_response['token']
print('TOKEN:', token)

url = BASE_URL + "/task/" + token
response = requests.post(url)
parsed_response = json.loads(response.text)
print("Zadanie:", parsed_response)
cookie = parsed_response['cookie']
exit(0)

url = BASE_URL + "/answer/" + token
data = {"answer": cookie }
response = requests.post(url, data=json.dumps(data), headers  = headers )
print('response:', response)
parsed_response = json.loads(response)
print(response)

if __name__ == "main":
  load_dotenv()
  get_task(TASK_HELLO)
