# the purpose of using API is to get data points and update the database.

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
# API request: HTTP request + API endpoint URL which server can understand the path to get the needs of data from database.
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# API response: server to client by json format. 
print(json.dumps(response.json(), indent=2))
for result in response.json()["results"]:
    print(result["trackName"])
