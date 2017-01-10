#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/xinyi3/404w17lab1/master/checkVersion.py")

print response.status_code

print response.text
