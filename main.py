from email.mime import message
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "abusive_word" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Don't use such words!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)


