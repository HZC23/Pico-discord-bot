# Pico - Bot Discord Multifonction

![Langage](https://img.shields.io/badge/langage-Python-blue.svg)
![Librairie](https://img.shields.io/badge/librairie-discord.py-7289DA.svg)

**Pico** est un bot Discord amical et polyvalent, conçu pour apporter des fonctionnalités utiles et divertissantes à votre serveur. Développé en Python avec la librairie `discord.py`, il intègre plusieurs API externes pour offrir une expérience riche.

## ✨ Fonctionnalités

Pico propose une variété de commandes préfixées par `!`:

### Commandes de Bien-être et Divertissement
*   `!hello`: Pico vous salue chaleureusement.
*   `!hug`: Envoie un câlin virtuel.
*   `!compliment`: Vous offre un compliment pour égayer votre journée.
*   `!joke`: Raconte une blague (sur le thème de l'informatique).
*   `!happy`: Partage un message positif.
*   `!inspire`: Donne une citation inspirante.

### Commandes Utilitaires
*   `!gif <terme>`: Recherche et envoie un GIF correspondant au terme recherché via l'API Giphy.
*   `!weather <ville>`: Affiche la météo actuelle pour une ville donnée en utilisant l'API OpenWeatherMap.
*   `!ask <question>`: Interroge une intelligence artificielle (Mistral-Nemo sur Hugging Face) pour répondre à votre question.

## 🛠️ Installation et Configuration

### Prérequis
*   [Python 3.8+](https://www.python.org/downloads/)
*   Un compte Discord et un serveur où vous avez les droits d'administrateur.
*   Des clés d'API pour :
    *   [Discord](https://discord.com/developers/applications)
    *   [Giphy](https://developers.giphy.com/)
    *   [OpenWeatherMap](https://openweathermap.org/api)
    *   [Hugging Face](https://huggingface.co/settings/tokens)

### Étapes d'installation

1.  **Clonez le dépôt :**
    ```bash
    git clone [URL_DU_DEPOT]
    cd Pico
    ```

2.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurez les informations sensibles :**

    Pour des raisons de sécurité, ne mettez jamais vos clés d'API et tokens directement dans le code. Utilisez plutôt un fichier `.env`.

    a. Créez un fichier nommé `.env` à la racine du projet.
    
    b. Ajoutez-y vos clés de la manière suivante :
    ```ini
    DISCORD_TOKEN=VOTRE_TOKEN_DISCORD
    GIPHY_API_KEY=VOTRE_CLE_GIPHY
    OPENWEATHERMAP_API_KEY=VOTRE_CLE_OPENWEATHERMAP
    HUGGINGFACE_API_KEY=VOTRE_CLE_HUGGINGFACE
    ```

    c. Le code de `Pico.py` est déjà configuré pour charger ces variables de manière sécurisée.

4.  **Lancez le bot :**
    ```bash
    python Pico.py
    ```

## 👨‍💻 Améliorations et Sécurité

Dans cette version, une modification cruciale a été apportée pour la sécurité et les bonnes pratiques de développement :

*   **Gestion des secrets** : Le code a été adapté pour charger les tokens et clés d'API depuis un fichier `.env` (via la librairie `python-dotenv`) plutôt que de les laisser en clair dans le code. C'est une pratique essentielle pour tout projet professionnel.

## 🤝 Contribution

Les contributions pour améliorer Pico sont les bienvenues. Vous pouvez par exemple :
*   Ajouter de nouvelles commandes.
*   Intégrer d'autres API.
*   Améliorer la gestion des erreurs.
*   Traduire le bot dans d'autres langues.
