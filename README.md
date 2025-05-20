# Bot de Discord – Proyecto de Interfaces

Bot de Discord desarrollado para la materia de Interfaces, con varios comandos divertidos y útiles para interactuar en un servidor.  
Programa realizado con fines educativos para la Universidad Autónoma de San Luis Potosí (UASLP).

## 🚀 Instalación

1. Clona el repositorio (si aún no lo has hecho):

   ```bash
   git clone https://github.com/tuusuario/tu-repo
   cd tu-repo

2. Crear y activar un entorno virtual recomendado (venv):
    
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    source venv/bin/activate # En Linux / macOS

3. Instalar las dependencias necesarias:

    ```bash
    pip install -r requirements.txt

4. Crea un archivo .env con tus variables de entorno (ejemplo):
    ```ini
    DISCORD=tu_token_de_discord
    ORS=tu_api_key_de_openrouteservice

🛠 Uso
Ejecuta el bot con:

    ```bash
    python bot.py

Luego, en tu servidor de Discord, usa el prefijo $ para llamar los comandos, por ejemplo:

$hola — Saluda al servidor.

$ruleta — Juega a la ruleta rusa.

$joke — Obtén un chiste de Chuck Norris traducido.

$translate <texto> — Traduce texto de inglés a español.

$meme — Recibe un meme aleatorio.

$insulto — Obtén un insulto aleatorio traducido.

$consejo — Recibe un consejo traducido.

$siono — Responde con sí o no a una pregunta.

$darkjoke — Recibe un chiste oscuro.

$ayuda — Muestra la lista de comandos disponibles.

📦 Dependencias
discord.py para la interacción con Discord.

aiohttp para hacer peticiones HTTP asíncronas.

python-dotenv para cargar variables de entorno desde .env.

🔐 Variables de entorno
DISCORD — Token de acceso para el bot de Discord.

ORS — API key para OpenRouteService (si usas funcionalidades de mapas).

📚 Recursos
Documentación de discord.py

API de Chuck Norris Jokes

MyMemory Translation API

Advice Slip JSON API

YesNo WTF API

JokeAPI