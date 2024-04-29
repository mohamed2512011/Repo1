# !/bin/var python

import subprocess

network = input("Enter your network >>> ")

subprocess.call(f"netdiscover -r {network}", shell=True)
