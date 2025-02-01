import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios {ctx.author.name}')

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def gen(ctx):
    await ctx.send(gen_pass(10))

bot.run('Token')
