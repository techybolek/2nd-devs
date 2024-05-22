from PIL import Image
import requests
from io import BytesIO

import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util


the_prompt =  """I will give you a drawing of a gnome with a hat on his head. Tell me what is the color of the
hat in POLISH. Be ultra-concise, just return the color. If the picture show something other than a gnome, return "ERROR" as answer."""

#the_prompt =  """What's in this picture?"""


the_task, task_token = task_util.get_task('gnome')
print(the_task, task_token)
image_url = the_task['url']
print('Image URL:', image_url)

response = requests.get(image_url)
resp = task_util.get_oai_answer_from_image(the_prompt, image_url)
print(resp)
img = Image.open(BytesIO(response.content))
img.show()
print('Done')
task_util.submit_task(resp, task_token)
