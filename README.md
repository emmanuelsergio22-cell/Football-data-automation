# Football-data-automation
# Football Data Automation

Pulls live football standings, generates an AI-written caption about the league leader, and logs a daily snapshot to a local database — fully automated, runs on its own every day.

## What it does

- Fetches current standings for a league from the football-data.org API
- Uses the Claude API (Anthropic) to generate a short, social-media-style caption about the top team
- Stores a snapshot of the full table (position, team, points, goal difference, form) in a local SQLite database on every run, building up a history over time
- Runs automatically once a day via a scheduled cron job — no manual trigger needed

## Tech stack

- Python 3
- `requests` — API calls
- `python-dotenv` — environment variable / secrets management
- `anthropic` — Claude API for caption generation
- `sqlite3` — local data storage (built into Python)
- `cron` — daily scheduling

## Example output