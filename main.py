import os
import discord
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AFKClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_afk = True
        self.replied_users = {}
        self.cooldown = 25 * 60

    async def on_ready(self):
        print(f'{self.user.name} is ready and listening for DMs!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            content = message.content.lower()
            if content == '!afk on':
                self.is_afk = True
                print(f"[{time.strftime('%X')}] AFK ON")
                try: await message.delete()
                except discord.HTTPException: pass
                return
            elif content == '!afk off':
                self.is_afk = False
                print(f"[{time.strftime('%X')}] AFK OFF")
                try: await message.delete()
                except discord.HTTPException: pass
                return
            return

        if not self.is_afk or message.guild is not None or message.author.bot:
            return

        user_id = message.author.id
        now = time.time()

        if user_id in self.replied_users and (now - self.replied_users[user_id] < self.cooldown):
            return

        try:
            afk_msg = os.getenv('AFK_MESSAGE', 'I am currently AFK.')
            await message.reply(afk_msg)
            print(f"[{time.strftime('%X')}] replied to {message.author.name}")
            self.replied_users[user_id] = now
        except discord.HTTPException:
            pass

client = AFKClient()
token = os.getenv('DISCORD_TOKEN')

if not token or token == 'your_token_here':
    print("Please add your Discord token to the .env file!")
    exit(1)

client.run(token)
