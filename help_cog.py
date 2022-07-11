import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.help_message = """
```
General commands
/help - displays all the available commands
/play <keywords> - plays the selected song from YouTube
/pause - pauses the current song being played
/resume - resumes playing the current song
/skip - skips the currently played song
/clear - stops the current song and clears the queue
/queue - displays all the songs currently in the queue
/leave - kicks the bot from the voice channel
```
"""
        
# send message to all text channels        
    #     self.text_channel_text = []
    
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     for guild in self.bot.guilds:
    #         for channel in guild.text_channels:
    #             self.text_channel_text.append(channel)
            
    #     await self.send_to_all(self.help_message)

    @commands.command(name="help", help="Displays all available commands")
    async def help(self,ctx):
        await ctx.send(self.help_message)

    # async def send_to_all(self,msg):
    #     for text_channel in self.text_channel_text:
    #         await text_channel.send(msg)