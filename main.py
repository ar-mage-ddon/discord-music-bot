import discord
from discord.ext import commands
import os
import config

from help_cog import help_cog
from music_cog import music_cog

# what you use to summon the bot
bot = commands.Bot(command_prefix="/")

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

TOKEN = config.bot_token
bot.run(TOKEN)
