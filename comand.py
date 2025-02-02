import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
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
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def gen(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def eat(ctx):
    await ctx.send(f'Pizza de peperoni y un frappe')

@bot.command()
async def dis_information(ctx):
    await ctx.send(f'Discord es una aplicación gratuita que permite a los usuarios comunicarse a través de chats de voz, video y texto. Es una de las formas más populares de conectarse con personas en línea.')

@bot.command()
async def que_tal(ctx):
    await ctx.send(f'Todo excelente y ¿cómo estas tu?')

@bot.command()
async def question(ctx):
    await ctx.send(f'¿Te gustaría ver "Batman", {ctx.author.name}?')

bot.run('Token')
