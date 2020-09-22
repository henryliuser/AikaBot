# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("I'm in.")

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    print(ctx)
    print(ctx.message)
    print(ctx.message.author)
    print(ctx.message.author.voice)
    print(ctx.message.author.voice.channel)

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run(TOKEN)
