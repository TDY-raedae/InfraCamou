import os
import requests

os.environ['http_proxy'] = 'http://proxy.com:port'
os.environ['https_proxy'] = 'http://proxy.com:port'

url = 'https://github.com/user/repo.git'
response = requests.get(url)
