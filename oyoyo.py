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
    if message.content.startswith("?cookie:"):
        await client.send_message(message.channel, ":cookie:")


client.run("NTExMzI4ODA2NDA2MTkzMTYy.DspT0w.c5h2uB2xl2fGjq6OKITfQFXJ2vw")
