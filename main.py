import os
import discord
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AFKClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track whether the bot should auto-reply or not
        self.is_afk = True
        
        # A dictionary to store the last time we replied to a user
        # Key: User ID, Value: Timestamp of last reply
        self.replied_users = {}
        
        # Cooldown time in seconds (25 minutes)
        self.cooldown_seconds = 25 * 60

    async def on_ready(self):
        print(f'{self.user.name} is ready and listening for DMs!')

    async def on_message(self, message):
        # If the message is from us, check if it's a command to toggle AFK
        if message.author.id == self.user.id:
            content = message.content.lower()
            if content == '!afk on':
                self.is_afk = True
                print(f"[{time.strftime('%X')}] System: AFK Mode turned ON")
                try:
                    await message.delete()
                except discord.HTTPException:
                    pass
                return
            elif content == '!afk off':
                self.is_afk = False
                print(f"[{time.strftime('%X')}] System: AFK Mode turned OFF")
                try:
                    await message.delete()
                except discord.HTTPException:
                    pass
                return
            
            # Ignore all other messages we send
            return

        # If we are not currently AFK, don't do anything
        if not self.is_afk:
            return

        # Ignore messages in servers (guilds), we only want DMs
        if message.guild is not None:
            return

        # Ignore bots just to be safe
        if message.author.bot:
            return

        user_id = message.author.id
        now = time.time()

        # Check if we've already replied to this user recently
        if user_id in self.replied_users:
            last_reply_time = self.replied_users[user_id]
            if now - last_reply_time < self.cooldown_seconds:
                # Still in cooldown, don't reply again
                return

        try:
            # Send the custom AFK message
            afk_msg = os.getenv('AFK_MESSAGE', 'I am currently AFK.')
            await message.reply(afk_msg)
            
            # Log it
            print(f"[{time.strftime('%X')}] Replied to DM from {message.author.name}")
            
            # Update the cooldown timestamp
            self.replied_users[user_id] = now
        except discord.HTTPException as e:
            print(f"Failed to send DM to {message.author.name}: {e}")

client = AFKClient()
token = os.getenv('DISCORD_TOKEN')

if not token or token == 'your_token_here':
    print("Please add your Discord token to the .env file!")
    exit(1)

client.run(token)
