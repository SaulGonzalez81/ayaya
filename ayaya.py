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
        await client.send_message(message.channel, message.author.top_role.name)
        await client.send_message(message.channel, "Cookie!")
        await client.send_message(message.channel, ":cookie:")


client.run("NTExMjYwODQwNjgzNTAzNjE2.DspB7Q.ygmroqzlXwW-0R0WjyKmbE6gEak")
