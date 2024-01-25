import requests
import json

url = 'http://localhost:5000/message'
body = {'message': 'test message'}

r = requests.post(url, json = body)

print(r.text)
