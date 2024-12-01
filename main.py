import discord
from discord.ext import commands
import time
from rgbprint import Color
from rgbprint import gradient_print
import sys

def getToken():
    with open('token.txt', 'r') as file:
        token = file.read()
        if token != None:
            return token
        else:
            print(f"{Color.red}[!]{Color.reset} Make a file called token.txt and paste your token there")
            sys.exit()

client = commands.Bot(command_prefix='#', self_bot=True)

@client.event
async def on_ready():
    gradient_print(f'SelfSwag logged in as {client.user.name}', start_color="red", end_color="magenta")

@client.command()
async def parseids(ctx):
    fname = time.time()
    for member in ctx.guild.members:
        with open(f"output/{fname}.txt", 'a') as file:
            file.write(f"{member.id}\n")
    print(f"{Color.light_green}[+]{Color.reset} Saved IDs to output/{fname}.txt")

@client.command()
async def parsenames(ctx):
    fname = time.time()
    for member in ctx.guild.members:
        with open(f"output/{fname}.txt", 'a') as file:
            file.write(f"{member.name}\n")
    print(f"{Color.light_green}[+]{Color.reset} Saved usernames to output/{fname}.txt")


client.run(getToken())
