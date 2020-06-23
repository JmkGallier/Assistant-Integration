#!/usr/bin/python3

# import serial
# import time
import os
import sys

project_id = sys.argv[1]
model_id = sys.argv[2]

# Declares absolute path
pressSense_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.dirname(pressSense_dir)
AsstIntegration_script_dir = os.path.join(pressSense_dir + "/AsstIntegration")
bash_prefix = "/bin/bash"
expect_prefix = "/usr/bin/expect"

# Create command to trigger expect script
bash_Assistant = f"{expect_prefix} {pressSense_dir}/GA_calendar_trigger.sh {repo_dir} {project_id} {model_id}"

# Trigger expect shell script
os.system(bash_Assistant)