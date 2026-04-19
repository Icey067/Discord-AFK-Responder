# discord-afk-responder

just a simple python script to auto-reply to DMs when you're away from your keyboard. uses `discord.py-self` since regular user bots are against ToS (use this at your own risk btw).

## Features
- **DM only:** ignores servers completely so it doesn't spam channels
- **Cooldowns:** won't reply to the same person more than once every 25 minutes
- **Toggle via chat:** type `!afk on` or `!afk off` from anywhere (using your own account) to toggle the bot without having to stop the script. it tries to auto-delete the trigger message too.

## Setup
1. Clone the repo
2. Setup a venv and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Create a `.env` file (you can copy `.env.example`) and drop your discord token in there. 

## Running
```bash
python main.py
```

## License
MIT License. Do whatever you want with it.
