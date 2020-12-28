# bot.py
import os
import random
import discord
import speech_recognition as sr
import pyttsx3 as tts
import time

from discord.ext import commands
from dotenv import load_dotenv

import voice_commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '!')

audio_source = discord.AudioSource()
current_vc = None

tts_engine = tts.init()
sp_recogizer = sr.Recognizer()

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
    aika_quotes = ["The beginning is the end, and the end is the beginning. \
Well then, let us begin again. And to each, their own tale.",
                   "The subtle light that is born when people's feelings come together. \
That light embraces felicity, evil, sin, and happiness. The light blazes forth... \
illuminating the whole truth.",
                   "Just because it's illogical, that doesn't make it wrong.",
                   "Summer stars are so unscrupulous. They shine without thought or care. \
They try so hard to display their radiance. Trying to let us know they exist before they disappear. \
I admire that simple, honest wish.",
                   "Everything happens for a reason. The daily tragedies and misfortunes are all \
meaningful events, leading toward an ideal conclusion. With that in mind, there probably isn't \
really any meaningless misfortune.",
                   "The actors on stage cannot ignore their scripts and do as they wish. If they \
make a beautiful exit, I feel they fulfill their role.",
                   "It might be for the better if there are amusing people around me. Because \
any tragedy may seem a comedy, as long as I am with them.",
                   "The beginning is the end, and the end is the beginning. Well then, \
let us begin again. And to each, their own tale."
                   ]
    await ctx.channel.send(random.choice(aika_quotes))

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
        wait_voice_command(ctx, source)
    # await ctx.channel.send("i'm listening")

def wait_voice_command(ctx, source):
        audio = sp_recogizer.listen(source)
        text = sp_recogizer.recognize_google(audio).lower()
        # with open("temp_speech.wav", "wb") as file:  # don't need yet
        #     file.write(audio.get_wav_data())
        print(ctx.message.author, text)
        aika = text.find("aika")  # deal with 'ico' later
        if aika == -1: return
        else: text = text[len('aika '):]
        for c in voice_commands.commands.keys():
            loc = text.find(c)
            if loc == -1: continue
            left_arg = text[:loc].strip()
            right_arg = text[loc+len(c):].strip()
            speak(voice_commands.commands[c](left_arg, right_arg))

def speak(words):
    fname = 'temp.wav'
    # fname = f'{"".join(words.split())}.wav'
    tts_engine.save_to_file(words, fname)
    tts_engine.runAndWait()
    time.sleep(2)
    play(fname)
    # current_vc.stop()
    # current_vc.play(discord.FFmpegPCMAudio(source='temp.wav'))
    time.sleep(0.1)
    os.remove(fname)


client.run(TOKEN)
