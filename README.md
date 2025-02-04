# Téléchargeur d'extraits YouTube

Ce projet propose une application Python avec une interface graphique (Tkinter) qui vous permet de télécharger un extrait (défini par un intervalle de temps) d'une vidéo YouTube en utilisant [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Fonctionnalités

- **Téléchargement d'un extrait vidéo :** Spécifiez l'URL de la vidéo, le temps de début et le temps de fin (en secondes) pour extraire la portion souhaitée.
- **Interface Graphique :** Utilisation de Tkinter pour une prise en main simple et intuitive.
- **Sélection du répertoire de sortie :** Un bouton "Parcourir" permet de définir l'emplacement du fichier de sortie.

## Prérequis

- Python 3.6 ou supérieur.
- [yt-dlp](https://pypi.org/project/yt-dlp/) (installé via le fichier [requirements.txt](./requirements.txt))  
  Tkinter est inclus avec Python sur de nombreuses distributions.

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-depot.git
   cd nom-du-depot
   ```

2. **(Optionnel) Créer et activer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Exécutez le script principal : 

python youtube_clip_downloader.py
