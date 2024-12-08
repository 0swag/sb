import discord
from discord.ext import commands
import time
from rgbprint import Color
from rgbprint import gradient_print
import sys
import random
from openai import OpenAI

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
    fname = f"{ctx.guild.name}-{time.time()}"
    for member in ctx.guild.members:
        with open(f"output/{fname}.txt", 'a') as file:
            file.write(f"<@{member.id}>\n")
    print(f"{Color.light_green}[+]{Color.reset} Saved IDs to output/{fname}.txt")

@client.command()
async def parsenames(ctx):
    fname = time.time()
    for member in ctx.guild.members:
        with open(f"output/{fname}.txt", 'a') as file:
            file.write(f"{member.name}\n")
    print(f"{Color.light_green}[+]{Color.reset} Saved usernames to output/{fname}.txt")

@client.command()
async def mystats(ctx):
    guildsIn = 0
    friends = 0
    msgCount = 0
    for friend in client.friends:
        friends+=1
    for guild in client.guilds:
        guildsIn+=1
    async for message in ctx.channel.history(limit=None):
        if message.author.id == client.user.id:
            msgCount+=1
    await ctx.reply(f"```🫂 Friends: {friends}\n🌐 Servers: {guildsIn}\n💬 Messages in this channel: {msgCount}```")

@client.command()
async def coinflip(ctx):
    result = random.randint(0,1)
    message = await ctx.reply("🪙 Flipping..")
    time.sleep(1)
    if result == 1:
        await message.edit("🪙 It's tails!")
    else:
        await message.edit("🪙 It's heads!")

@client.command()
async def diceroll(ctx):
    message = await ctx.reply('🎲 Rolling..')
    time.sleep(1)
    await message.edit(f'🎲 Rolled {random.randint(0,6)}')

@client.command()
async def ask(ctx):
    aiclient = OpenAI()
    prompt = ctx.message.content
    response = aiclient.chat.completions.create(model="o1-preview", messages=[{'role': 'user', 'content': prompt}])
    response = response.choices[0].message.content
    await ctx.reply(response)

#@client.command()
#async def bumpsetup(ctx):


client.run(getToken())
