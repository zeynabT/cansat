import requests
import json
url = "http://192.168.137.115:7418"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(json.loads(response.text)['temp'])
