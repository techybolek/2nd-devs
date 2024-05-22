import requests
import json
import os

OAI_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
headers = {"Authorization": "Bearer " + OPENAI_API_KEY}
  
messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
]
  
data = { "model": "gpt-4o", "messages": messages }
  
response = requests.post(OAI_URL, json=data, headers=headers)
  
parsed_response = json.loads(response.text)
#print(parsed_response)
resp = parsed_response['choices'][0]['message']['content']
print(resp)