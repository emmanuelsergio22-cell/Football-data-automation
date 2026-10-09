import os
import anthropic
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("FOOTBALL_API_KEY")
client = anthropic.Anthropic()
from datetime import date
today = str(date.today())
import sqlite3
conn = sqlite3.connect("football_data.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS standings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_pulled TEXT,
        position INTEGER,
        team_name TEXT,
        points INTEGER,
        goal_difference INTEGER,
        form TEXT
    )
""")
conn.commit()

import requests
url = "https://api.football-data.org/v4/competitions/DED/standings"
headers = {"X-Auth-Token": api_key}
api_requests = requests.get(url, headers=headers)
data = api_requests.json()

for team in data["standings"][0]["table"]:
    print(f"{team['position']} : {team['team']['name']} : {team['points']}")
    cursor.execute(
    "INSERT INTO standings (date_pulled, position, team_name, points, goal_difference, form) VALUES (?, ?, ?, ?, ?, ?)",
    (today, team['position'], team['team']['name'], team['points'], team['goalDifference'], team['form'])
)
conn.commit()

top_team = data["standings"][0]["table"][0]
prompt = f"write a short, punchy one-sentence football caption about {top_team['team']['name']}, who are top of the table with {top_team['points']}points. Make it sound like something a player would post, not a news headline."

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    messages=[{"role": "user", "content" : prompt}]
)
print(response.content[0].text) 

cursor.execute("SELECT * FROM standings")
rows = cursor.fetchall()
for row in rows:
    print(row)




