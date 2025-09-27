import discord
from discord.ext import commands
import random
import requests
import os
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()

# Crée une instance de bot
intents = discord.Intents.default()
intents.message_content = True  # Important pour que le bot puisse lire les messages

bot = commands.Bot(command_prefix="!", intents=intents)
gif_history = set()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

translator = Translator()

# Connecte le bot à ton serveur
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté !")

# Commande pour dire bonjour
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Coucou! 🐾 Comment vas-tu, petit chou ? 💖")

# Commande mignonne pour envoyer des câlins
@bot.command(name="hug")
async def hug(ctx):
    await ctx.send("Voici un câlin virtuel pour toi! 🤗💞")

# Commande pour envoyer un compliment
@bot.command(name="compliment")
async def compliment(ctx):
    compliments = [
        "Tu es incroyable, n'oublie jamais ça ! 🌟",
        "Tu es aussi mignon qu'un petit chaton ! 🐱",
        "Tu es une personne formidable et lumineuse ! 🌻"
    ]
    await ctx.send(random.choice(compliments))

# Commande pour une blague mignonne
@bot.command(name="joke")
async def joke(ctx):
    joke_blague = [ 
       "Pourquoi les informaticiens confondent-ils Halloween et Noël ? 🎃🎄 Parce que OCT 31 = DEC 25 !",
        "Quel est le comble pour un développeur ? 💻 De ne pas avoir d'exception !",
        "Pourquoi les ordinateurs n’aiment-ils pas les plages ? 🏖️ Parce qu’ils détestent les virus ! 🦠",
        "Que dit un logiciel à un autre logiciel ? 🤖 'Tu as besoin d’une mise à jour ?'",
        "Pourquoi les hackers sont-ils de mauvais jardiniers ? 🌿 Parce qu’ils ne peuvent pas garder les racines en place ! 🌱",
        "Pourquoi les ordinateurs n'aiment-ils pas le vent ? 🌬️ Parce qu'ils ont peur de perdre leurs fenêtres ! 🪟",
        "Quel est le comble pour un informaticien ? 🤔 De ne pas trouver de bug dans son code !",
        "Pourquoi les programmeurs aiment-ils la nature ? 🌳 Parce qu’il y a moins de bugs ! 🐛",
        "Que dit un réseau à un autre réseau ? 🌐 'On se fait une connexion ?'",
        "Pourquoi les ordinateurs vont-ils à la fête ? 🎉 Parce qu'ils ont entendu qu'il y aurait des disques ! 💿",
        "Quel est le comble pour un serveur ? 🍽️ D’être trop chargé ! 🖥️",
        "Pourquoi les informaticiens n'aiment-ils pas le camping ? ⛺ Parce qu'ils ne supportent pas les bugs ! 🐞",
        "Que dit un administrateur à un utilisateur ? 🛠️ 'C'est pas un problème, c'est une fonctionnalité !'",
        "Pourquoi les fichiers ne jouent-ils jamais à cache-cache ? 📁 Parce qu’ils se cachent dans des dossiers ! 🗂️",
        "Quel est le plat préféré des informaticiens ? 🍝 Les données à la sauce SQL !",
        "Pourquoi les programmes informatiques sont-ils souvent tristes ? 😢 Parce qu’ils ont trop de bugs à régler ! 🐞",
        "Que dit un code à un autre code ? 🧑‍💻 'On doit se réorganiser !'",
        "Pourquoi les ordinateurs ne vont-ils jamais au gymnase ? 🏋️‍♂️ Parce qu'ils ont peur des crashs ! 💥",
        "Quel est le comble pour un geek ? 🤓 D’oublier son mot de passe !",
        "Pourquoi les clés USB sont-elles de mauvaises mentrices ? 🔑 Parce qu’elles n’arrêtent pas de perdre leur mémoire ! 🧠"
]
    await ctx.send(random.choice(joke_blague))

@bot.command(name="happy")
async def happy(ctx):
    happy = [
        "Tu es si génial(e) ! 😊💖 Voici un petit cœur pour toi : 💝 et un petit chat pour te tenir compagnie : 🐱!"
        "Tu es incroyable, n'oublie jamais à quel point tu es unique ! 🌟",
        "Chaque jour est une nouvelle opportunité pour briller ! ✨",
        "Souris, la vie est belle et pleine de surprises ! 😊",
        "Tu es capable de tout accomplir, continue à avancer avec confiance ! 💪",
        "Prends un moment pour toi, tu mérites toute la douceur du monde. 🌸",
        "La persévérance est la clé du succès, ne lâche rien ! 🔑",
        "Aujourd'hui est un bon jour pour être heureux, profites-en ! 😄",
        "Rappelle-toi que chaque petit pas te rapproche de tes rêves. 🏃‍♂️💫",
        "Sois fier de tout ce que tu as accompli jusqu'ici. 👏",
        "Il y a toujours une raison de sourire, même dans les moments difficiles. 🌈",
        "Ton sourire peut illuminer la journée de quelqu'un. Partage-le ! 😁",
        "La vie est une aventure, sois prêt à en savourer chaque instant. 🛤️",
        "Crois en toi, tu es plus fort que tu ne le penses. 💪✨",
        "Les petites victoires comptent, célèbre-les avec enthousiasme ! 🎉",
        "Chaque matin est une nouvelle chance de créer des souvenirs inoubliables. 🌞",
        "Ton énergie positive est contagieuse, continue de la diffuser autour de toi. 🌟",
        "La gentillesse que tu offres aux autres revient toujours à toi. 💖",
        "Tu es une source d'inspiration pour ceux qui t'entourent. Continue d'avancer ! 🌟",
        "Prends soin de toi, tu es important. 🌼",
        "Tu as le pouvoir de transformer ta journée, une pensée positive à la fois. 🌈"
        "Tout ira bien, tu es fort(e) et capable ! 🌟",
        "N'oublie pas de prendre soin de toi aujourd'hui ! 💖",
        "Tu es une personne merveilleuse, continue à briller ! ✨",
        "Rappelle-toi que les nuages cachent parfois le soleil, mais il est toujours là derrière. ☀️",
        "Ne baisse jamais les bras, tu es incroyable ! 🦋"
]
    await ctx.send(random.choice(happy))

# Commande pour envoyer une citation inspirante
@bot.command(name="inspire")
async def inspire(ctx):
    inspiring_quotes = [
        "La vie est belle, n'oublie jamais ça ! 🌸",
        "Sois le changement que tu veux voir dans le monde. 🌍 - Gandhi",
        "Chaque jour est une nouvelle opportunité de devenir une meilleure version de toi-même. 🌱",
        "Le succès n'est pas final, l'échec n'est pas fatal. C'est le courage de continuer qui compte. 💪",
        "L'obscurité ne peut pas chasser l'obscurité, seule la lumière peut le faire. ✨ - Martin Luther King Jr."
    ]
    await ctx.send(random.choice(inspiring_quotes))

@bot.command(name="cute_hello")
async def cute_hello(ctx):
    await ctx.send("Salut toi! 🐾🌸 J'espère que tu passes une journée magnifique! 😄💖")


@bot.command(name="gif")
async def cute_gif(ctx, *, search_term: str):
    api_key = os.getenv("GIPHY_API_KEY")
     # Recherche des GIFs de "cute cat"
    
    # Appel à l'API Giphy
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=10")
    
    if response.status_code == 200:
        data = response.json()

        # Vérifie si "data" existe dans la réponse et contient des GIFs
        if "data" in data and data["data"]:
            new_gif = None

            # Boucle pour vérifier si le GIF a déjà été envoyé
            for gif in data["data"]:
                gif_url = gif["url"]  # URL du GIF
                if gif_url not in gif_history:
                    new_gif = gif_url
                    gif_history.add(gif_url)  # Ajoute le GIF à l'historique
                    break
            
            # Si tous les GIFs ont déjà été envoyés, réinitialise l'historique
            if not new_gif:
                gif_history.clear()
                new_gif = data["data"][0]["url"]  # Prend le premier GIF par défaut
                gif_history.add(new_gif)

            # Envoie le GIF
            await ctx.send(f"Voici un GIF mignon pour toi! 🐱💖 {new_gif}")
        else:
            await ctx.send("Oups ! Pas de GIFs trouvés pour cette recherche.")
    else:
        await ctx.send(f"Erreur lors de la récupération des GIFs. Status code: {response.status_code}")




@bot.command(name="weather")
async def weather(ctx, *, city: str):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    # Construire l'URL de l'API OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Faire la requête API
    response = requests.get(weather_url)
    
    if response.status_code == 200:  # Vérifie si l'appel API est un succès
        data = response.json()
        
        # Extraire les données nécessaires
        city_name = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        
        # Créer le message de réponse
        message = (f"La météo actuelle à **{city_name}** :\n"
                   f"🌡 Température : {temp}°C (ressentie {feels_like}°C)\n"
                   f"☁️ Conditions : {description.capitalize()}\n"
                   f"💨 Vent : {wind_speed} m/s")
        
        # Envoyer la réponse sur Discord
        await ctx.send(message)
    else:
        await ctx.send(f"Je n'ai pas pu obtenir les informations météo pour **{city}**.")


def query_huggingface(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        response.raise_for_status()
        return response.json()[0]['generated_text']
    except (requests.exceptions.HTTPError, KeyError) as err:
        return f"Erreur lors de l'appel de l'API : {err}"

# Commande Discord : $instruct suivi de l'instruction
@bot.command(name= "ask")
async def instruct(ctx, *, instruction: str):
    # Interagir avec l'API Hugging Face
    instruction_fr = translator.translate(instruction, dest='fr').text
    response = query_huggingface(instruction_fr)
    # Envoyer la réponse du modèle sur Discord
    
    # Envoyer la réponse traduite sur Discord
    await ctx.send(response)


# Token de ton bot (NE PAS PARTAGER CE TOKEN)
bot.run(os.getenv("DISCORD_TOKEN"))

