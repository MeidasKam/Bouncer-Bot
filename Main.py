import nextcord
from nextcord.ext import commands
import Config as BotC

servers = [1126935737087037520]

TOKEN = BotC.MainBot["Token"]

bot = commands.Bot(command_prefix="###", intents=nextcord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("The bot is online.")

bot.run(TOKEN)