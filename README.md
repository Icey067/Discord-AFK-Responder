# 🤖 Discord AFK Auto-Responder

A lightweight, automated script that sends custom AFK replies to Direct Messages when you are away from your keyboard. Built using Python and `discord.py-self`.

> **⚠️ Disclaimer:** Automating user accounts (self-botting) is technically against Discord's Terms of Service. This script includes built-in safety measures (like cooldowns) to minimize risk, but you use this software strictly at your own risk.

## ✨ Features
- 🛡️ **DM Only:** Automatically filters out server messages to prevent spamming and save resources.
- ⏱️ **Intelligent Cooldown:** Avoids spamming users who send multiple messages. (Default: Auto-replies once every 25 minutes per user).
- 🎚️ **Remote Toggle:** Turn the bot on or off from *anywhere* across Discord by typing `!afk on` or `!afk off` using your own account.
- 🧹 **Self-Cleaning:** Attempts to automatically delete your `!afk on/off` trigger messages to keep your chat history clean.

## 🚀 Setup & Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/discord-afk-responder.git
cd discord-afk-responder
```

**2. Create a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configuration:**
Rename `.env.example` to `.env` (or create a new `.env` file) and add your Discord user token:
```ini
DISCORD_TOKEN=your_token_here
AFK_MESSAGE="Hey! I'm currently AFK. I'll get back to you soon. (Automated Message)"
```
*(To find your token, open Discord in your browser, press F12, go to the Network tab, send a message, and look for the `Authorization` header in the request).*

## 💻 Running the Bot
Make sure your virtual environment is activated, then run:

```bash
python main.py
```
*(Depending on your system, you may need to use `python3 main.py`)*

## 🛠️ Usage
* When the script first starts, AFK Mode is instantly **ON**.
* If you sit back down at your keyboard, type `!afk off` in any DM or server to stop auto-replying.
* When you leave again, type `!afk on`.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
