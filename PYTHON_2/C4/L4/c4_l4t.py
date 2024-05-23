import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to the SHARED directory
shared_dir = os.path.abspath(os.path.join(script_dir, '../../SHARED'))

# Add the SHARED directory to the system path
sys.path.append(shared_dir)

import task_util


the_task, task_token = task_util.get_task('ownapi')
the_url = "https://ba6c-70-241-108-123.ngrok-free.app/api/post"
task_util.submit_task(the_url, task_token)
