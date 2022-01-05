# Imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from dotenv import find_dotenv
import subprocess

# Credentials
load_dotenv(find_dotenv('bot.env'))
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command(pass_context=True)
async def wissa(ctx, eins, zwei, drei):
    if ctx.channel.name == "Channelname": #Channelname mit dem gewünschten Channel ersetzen oder die Zeile löschen, wenn der bot auf dem gesamten Server arbeiten soll
      subprocess.Popen(["./file.exe", eins, zwei, drei]) 
      await ctx.send("danke!"+" "+format(ctx.message.author))

client.run(TOKEN)
