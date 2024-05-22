import requests
import json
url = "http://localhost:11434/api/generate -d" 

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data returned by the API
else:
    print("Error:", response.status_code)