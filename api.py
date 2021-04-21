import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())