import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util


the_task, task_token = task_util.get_task('ownapipro')
ngrok_url = "https://2348-136-62-55-246.ngrok-free.app"
the_url = ngrok_url + "/api/post"
task_util.submit_task(the_url, task_token)
