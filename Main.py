# Bot de discord para pasar mi materia de interfaces. Atte: Adair, el mejor alumno que ha tenido.
# Permission Integer = 1145153371925568; Valor integral que determina los permisos del bot en el servidor.
import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import aiohttp

# Token de acceso al bot de Discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents son necesairios para comunicarse con los eventos de Discord
# https://discordpy.readthedocs.io/en/stable/intents.html
intents = discord.Intents.default() # Instancia de Intents
intents.message_content = True # Permitir el acceso al contenido de los mensajes

#Instanciar bot con prefijo, el prefijo es necesario para llamar los comandos
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot
bot = commands.Bot(command_prefix="$", intents=intents)

# Seccion de variables globales
bala = 6

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola Server!")

@bot.command()
async def ruleta(ctx):
    global bala
    numero = random.randint(1, bala)
    bala = bala - 1
    if numero == 1:
        await ctx.send("Has muerto :skull:, \nPistola Recargada! :gun:")
        bala = 6
    else:
        await ctx.send("Has sobrevivido :clown: \nBalas Restantes: " + str(bala))
    if bala == 0:
        bala = 6

@bot.command()
async def joke(ctx):
    url_chiste = "https://api.chucknorris.io/jokes/random"

    async with aiohttp.ClientSession() as session:
        async with session.get(url_chiste) as resp_chiste:
            if resp_chiste.status == 200:
                data = await resp_chiste.json()
                chiste_en = data["value"]

                # Traducción con MyMemory
                url_trad = f"https://api.mymemory.translated.net/get?q={chiste_en}&langpair=en|es"
                async with session.get(url_trad) as resp_trad:
                    if resp_trad.status == 200:
                        trad_data = await resp_trad.json()
                        chiste_es = trad_data["responseData"]["translatedText"]
                        await ctx.send(f"Aqui te va un chiste 😂: {chiste_es}")
                    else:
                        await ctx.send("❌ Chuck se ha cansado de compartir chistes. Intenta más tarde. \n Tampoco podras traducir jaja!")
            else:
                await ctx.send("Chuck Norris no quiere compartir chistes ahora 😤.")

@bot.command()
async def translate(ctx, *, text):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|es"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                translated_text = data["responseData"]["translatedText"]
                await ctx.send(f"Traducción: {translated_text}")
            else:
                await ctx.send("Error al traducir el texto. O Tokens acabados por hoy (Chuck Norris se canso de traducir).")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles", color=0x00ff00)
    embed.add_field(name="$hola", value="Saluda al servidor.", inline=False)
    embed.add_field(name="$ruleta", value="Juega a la ruleta rusa.", inline=False)
    embed.add_field(name="$joke", value="Recibe un chiste de Chuck Norris.", inline=False)
    embed.add_field(name="$translate <texto>", value="Traduce el texto de inglés a español.", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
