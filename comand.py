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

bot.run('Token')
