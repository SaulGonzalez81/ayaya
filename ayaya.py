import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if ("cookie" in message.content) and not (message.author.top_role.name == "@everyone"):
        await client.send_message(message.channel, "Here, " + message.author.mention + ", have a cookie! :cookie:")
        imgList = os.listdir("./Cookies") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "./Cookies/" + imgString # Creates a string for the path to the file

        await client.send_file(message.channel, path)


client.run("NTExMjYwODQwNjgzNTAzNjE2.DspB7Q.ygmroqzlXwW-0R0WjyKmbE6gEak")
