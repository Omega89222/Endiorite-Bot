import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
#dotenv c’est pour stocker le token dans un fichier .env 
#vous pouvez juste faire une variable DISCORD_TOKEN 
load_dotenv()
print("Bot start")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    try:
        await bot.load_extension("commands.Endiorite")
       ######Autres cmd
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisé ({len(synced)})")
    except Exception as e:
        print(f"Erreur lors de la sync : {e}")

bot.run(os.getenv("DISCORD_TOKEN"))