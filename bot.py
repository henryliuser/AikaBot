# bot.py
import os
import random
import discord
import speech_recognition as sr
import pyttsx3 as tts
import importlib  # hack around tts bugs

from discord.ext import commands
from dotenv import load_dotenv

import speech_input
import voice_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '!')

audio_source = discord.AudioSource()
current_vc = None

# tts_engine = tts.init()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    # await guild.channels[1].send("I'm in.")
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.command()
async def join(ctx):
    global current_vc
    v = ctx.message.author.voice
    if v == None:
        await ctx.channel.send("You gotta be in a voice channel")
    channel = ctx.message.author.voice.channel

    current_vc = await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def dbug(ctx):
    print("debugging")

@client.command()
async def quote(ctx):
    await ctx.channel.send(voice_commands.quote())

@client.command()
async def shake(ctx):
    shakespeare_quotes = [
        "The time is out of joint: O cursed spite / That ever I was born to set it right!* -- Hamlet",
        "Forty thousand brothers / Could not with all their quantity of love / \
Make up my sum.* -- Hamlet"]
    await ctx.channel.send(random.choice(shakespeare_quotes))

def play(filename):
    global current_vc
    current_vc.stop()
    current_vc.play(discord.FFmpegPCMAudio(source=filename))
    # await ctx.channel.send("done playing")

@client.command()
async def listen(ctx):
    global current_vc
    with sr.Microphone() as source:
        await ctx.channel.send("i'm listening")
        while True:
            result = speech_input.take_voice_command(ctx, source)
            print(ctx.author, result)
            if not result: pass
            elif result.find("farewell") != -1:
                await ctx.channel.send("goodbye!")
                await leave(ctx)
                return
            elif result.find("stop") != -1:
                await ctx.channel.send("no longer listening")
                return
            else: speak(result)

def speak(words):
    fname = 'temp.wav'
    importlib.reload(tts)
    tts_engine = tts.Engine()
    tts_engine.save_to_file(words, fname)
    tts_engine.runAndWait()
    play(fname)
    # time.sleep(0.2)
    # os.remove(fname)



client.run(TOKEN)
