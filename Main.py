# Bot de discord para pasar mi materia de interfaces. Adair
# Permission Integer = 1145153371925568; Valor integral que determina los permisos del bot en el servidor.
import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import aiohttp
import json

# Token de acceso al bot de Discord
load_dotenv()
TOKEN = os.getenv("DISCORD")
ORS_API_KEY = os.getenv("ORS")

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
                        await ctx.send("Chuck se ha cansado de compartir chistes. Intenta más tarde. \n Tampoco podras traducir jaja!")
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
async def meme(ctx):
    url_meme = "https://meme-api.com/gimme"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url_meme) as resp_meme:
            if resp_meme.status == 200:
                data = await resp_meme.json()
                meme_url = data["url"]
                meme_title = data["title"]
                if data["nsfw"] == False:
                    await ctx.send(f"Aqui tienes un meme: \n"
                                   f"Title: {meme_title}\n"
                                   f"{meme_url}")
                else:
                    await ctx.send("Este meme es NSFW, no puedo enviarlo aquí.")

@bot.command()
async def insulto(ctx):
    url = "https://insult.mattbas.org/api/insult"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                insult = await resp.text()

                # Traducción con MyMemory
                url_trad = f"https://api.mymemory.translated.net/get?q={insult}&langpair=en|es"
                async with session.get(url_trad) as resp_trad:
                    if resp_trad.status == 200:
                        trad_data = await resp_trad.json()
                        insulto = trad_data["responseData"]["translatedText"]
                        await ctx.send(f"{insulto}")
                    else:
                        await ctx.send("Chuck se ha cansado de compartir insultos. Intenta más tarde. \n Tampoco podras traducir jaja!")

@bot.command()
async def consejo(ctx):
    url = "https://api.adviceslip.com/advice"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                texto = await resp.text()
                try:
                    data = json.loads(texto)
                    consejo = data["slip"]["advice"]
                except Exception as e:
                    await ctx.send("Ocurrió un error procesando el consejo.")
                consejo = data["slip"]["advice"]

                # Traducción con MyMemory
                url_trad = f"https://api.mymemory.translated.net/get?q={consejo}&langpair=en|es"
                async with session.get(url_trad) as resp_trad:
                    if resp_trad.status == 200:
                        trad_data = await resp_trad.json()
                        consejo_es = trad_data["responseData"]["translatedText"]
                        await ctx.send(f"Aqui tienes un consejo: {consejo_es}")
                    else:
                        await ctx.send("Chuck se ha cansado de compartir consejos. Intenta más tarde. \n Tampoco podras traducir jaja!")
            else:
                await ctx.send("No se pudo obtener un consejo en este momento.")

@bot.command()
async def siono(ctx):
    async with aiohttp.ClientSession() as session:
        url = "https://yesno.wtf/api"
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                respuesta = data["answer"]
                imagen = data["image"]
                await ctx.send(f"Respuesta: {respuesta}\n{imagen}")
            else:
                await ctx.send("No se pudo obtener una respuesta en este momento.")

@bot.command()
async def darkjoke(ctx):
    url = "https://v2.jokeapi.dev/joke/Dark"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                if data["type"] == "single":
                    joke = data["joke"]
                else:  # type == "twopart"
                    joke = f'{data["setup"]}\n{data["delivery"]}'
                await ctx.send(f"Aqui tienes un chiste oscuro: \n{joke}")
   
@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos disponibles", color=0x00ff30)
    embed.add_field(name="$ayuda", value="Muestra esta lista de comandos.", inline=False)
    embed.add_field(name="$hola", value="Saluda al servidor.", inline=False)
    embed.add_field(name="$ruleta", value="Juega a la ruleta rusa.", inline=False)
    embed.add_field(name="$joke", value="Recibe un chiste de Chuck Norris.", inline=False)
    embed.add_field(name="$translate <texto>", value="Traduce el texto de inglés a español.", inline=False)
    embed.add_field(name="$meme", value="Recibe un meme aleatorio.", inline=False)
    embed.add_field(name="$insulto", value="Recibe un insulto aleatorio.", inline=False)
    embed.add_field(name="$consejo", value="Recibe un consejo aleatorio.", inline=False)
    embed.add_field(name="$siono", value="Responde a una pregunta con 'Sí' o 'No'.", inline=False)
    embed.add_field(name="$darkjoke", value="Recibe un chiste oscuro.", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
