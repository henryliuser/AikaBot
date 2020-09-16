# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

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
really any meaningless misfortune."]

    tempest_quotes = [""]

    if message.content == 'aika!':
        response = random.choice(aika_quotes)
        await message.channel.send(response)
    if message.content == "tempest!":
        response = random.choice(tempest_quotes)
        await message.channel.send(response)
client.run(TOKEN)