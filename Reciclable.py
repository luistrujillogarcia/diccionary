import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)
intents.message_content = True

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

# 🌎 Hábitos sostenibles
@bot.command()
async def reciclable(ctx, *, item: str):
    """Verifica si un objeto es reciclable o no."""
    reciclables = {"papel", "carton", "vidrio", "plastico", "metal"}
    no_reciclables = {"pañales", "papel higienico", "ceramica", "espejos", "colillas de cigarro"}
    item = item.lower()
    if item in reciclables:
        await ctx.send(f'{item.capitalize()} es reciclable. Depositalo en el contenedor adecuado.')
    elif item in no_reciclables:
        await ctx.send(f'{item.capitalize()} no es reciclable. Busca alternativas para reducir su uso.')
    else:
        await ctx.send(f'No estoy seguro sobre {item}. Investiga antes de desecharlo.')

@bot.command()
async def clasificar(ctx, *, item: str):
    """Clasifica un objeto en organico, reciclable o basura."""
    organicos = {"cascaras", "restos de comida", "hojas", "cesped"} 
    reciclables = {"papel", "carton", "vidrio", "plastico", "metal"}
    if item.lower() in organicos:
        await ctx.send(f'{item.capitalize()} es organico y puedes compostarlo.')
    elif item.lower() in reciclables:
        await ctx.send(f'{item.capitalize()} es reciclable. Usa el contenedor adecuado.')
    else:
        await ctx.send(f'{item.capitalize()} es basura comun. Desechalo correctamente.')

bot.run("Token")
