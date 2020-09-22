# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '.')

audio_source = discord.AudioSource()
# voice_channel = discord.VoiceChannel()

# @voice_channel.event
# async def on_ready():
#     print("yeehaw")

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    print(ctx)
    print(ctx.message)
    print(ctx.message.author)
    print(ctx.message.author.voice)

    await client.join_voice_channel(channel)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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

    shakespeare_quotes = [
        "The time is out of joint: O cursed spite / That ever I was born to set it right!* -- Hamlet",
        "Forty thousand brothers / Could not with all their quantity of love / \
Make up my sum.* -- Hamlet"
    ]

    if message.content == 'aika!':
        response = random.choice(aika_quotes)
        await message.channel.send(response)
    if message.content == "shake!":
        response = "*" + random.choice(shakespeare_quotes)
        await message.channel.send(response)

client.run(TOKEN)