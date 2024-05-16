import json
import re

from dotenv import load_dotenv
load_dotenv()

import os
shared_dir = os.path.abspath('./SHARED')

import sys
sys.path.append(shared_dir)

import task_util


the_task, task_token = task_util.get_task('search')
print(the_task)
#task_util.submit_task(the_answer, task_token)
