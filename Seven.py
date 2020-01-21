import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import re


from cleverwrap import CleverWrap
cw = CleverWrap("CC74d-BTvojAsdOPDst7CX3tkiA")

key = 'NTkxODEyNDc3NzA1MTI1ODg4.XQ2Okw.Fc9cVad3deDnyGzToBxToxTgoLQ'


Client = discord.Client()  # Initialise Client
client = commands.Bot(command_prefix = "!")  # Initialise client bot


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # This will be called when the bot connects to the server


@client.event
async def on_message(message):
    if message.content == "!Seven":
        output = 'Seven   V1.0 \n\n'
        await client.send(message.channel, output)
    if message.content.startswith('!s'):
        if message.content[2] == "\"" and message.content[-1] == "\"":
            input_conversation = message.content[3:-1]
            output = cw.say(input_conversation)
            # await message.channel.send(message.channel, output)
            await message.channel.send(output)


client.run(key)
