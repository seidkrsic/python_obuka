


# https://itunes.apple.com/search?entity=song&limit=1&term=love 
import json 
import requests 
import sys 

if len(sys.argv) != 2: 
    sys.exit() 

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}")
# print(json.dumps(response.json(), indent=2))    

response = response.json() 
for result in response["results"]: 
    print(result["trackName"])  