import discord
import os
import random
from dotenv import load_dotenv

# Token
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)
token = os.getenv('TOKEN')

phrases = ['tesla', 'tesla\'s', 'fsd', 'musk', 'elon', 'hw4', 'hw14', 'automated', 'teslas', 'elon\'s', 'musk\'s']
jokes =     ["Yo I love sucking Elon\'s cock too",
            "It is hard to hear when you're swimming in Elon's semen.",
            "Shut up autistic Elon dickrider!!!"]

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if message.author == client.user:
        return

    if channel == "autistic-zaza-memes" and username == "zaza774":
        for word in user_message.lower().split(" "):
            if word in phrases:
                await message.reply(random.choice(jokes))
                return
            elif word == 'trump' or word == 'trump\'s':
                await message.reply("You are Trump\'s bitch!!!")
                return

    if channel == "autistic-zaza-memes" and username == "psa_inspector":
        for word in user_message.lower().split(" "):
            if word in ['money', 'net', 'figures', 'poorer', 'salary']:
                await message.reply("LOL I make your networth in an hour, broke ass smelly indian.")
                return

client.run(token)
