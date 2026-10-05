import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("FOOTBALL_API_KEY")

import requests
url = "https://api.football-data.org/v4/competitions/DED/standings"
headers = {"X-Auth-Token": api_key}
api_requests = requests.get(url, headers=headers)
data = api_requests.json()

for team in data["standings"][0]["table"]:
    print(f"{team['position']} : {team['team']['name']} : {team['points']}")