import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
import os 
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado a: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios {ctx.author.name}')

@bot.command()
async def coin(ctx):
    await ctx.send(f'La moneda cayo a: {flip_coin()}')

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

@bot.command()
async def mem(ctx):
    lista = os.listdir("images")
    img_name = random.choice(lista)
    with open(f'images/{img_name}','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)


def get_fox_image_link():    
    link = 'https://randomfox.ca/floof/'
    res = requests.get(link)
    data = res.json()
    return data['link']

@bot.command('fox')
async def fox(ctx):
    image_link = get_fox_image_link()
    await ctx.send(image_link)


def get_capy_image_url():    
    url = 'https://api.capy.lol/v1/capybara?json=true'
    res = requests.get(url)
    data = res.json()
    return data["data"]["url"]

@bot.command('capy')
async def capy(ctx):
    image_url = get_capy_image_url()
    await ctx.send(image_url)


def get_cat_image_url():    
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    return data[0]["url"]

@bot.command('cat')
async def cat(ctx):
    image_url = get_cat_image_url()
    await ctx.send(image_url)


def get_poke_image_link():    
    link = 'https://pokeapi.co'
    res = requests.get(link)
    data = res.json()
    return data["link"]

@bot.command('poke')
async def poke(ctx):
    image_link = get_poke_image_link()
    await ctx.send(image_link)


def get_tokio_image_link():    
    link = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(link)
    data = res.json()
    return data["link"]

@bot.command('tokyo')
async def tokyo(ctx):
    image_link = get_tokio_image_link()
    await ctx.send(image_link)

bot.run('Token')
