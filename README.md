# T�l�chargeur d'extraits YouTube

Ce projet propose une application Python avec une interface graphique (Tkinter) qui vous permet de t�l�charger un extrait (d�fini par un intervalle de temps) d'une vid�o YouTube en utilisant [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Fonctionnalit�s

- **T�l�chargement d'un extrait vid�o :** Sp�cifiez l'URL de la vid�o, le temps de d�but et le temps de fin (en secondes) pour extraire la portion souhait�e.
- **Interface Graphique :** Utilisation de Tkinter pour une prise en main simple et intuitive.
- **S�lection du r�pertoire de sortie :** Un bouton "Parcourir" permet de d�finir l'emplacement du fichier de sortie.

## Pr�requis

- Python 3.6 ou sup�rieur.
- [yt-dlp](https://pypi.org/project/yt-dlp/) (install� via le fichier [requirements.txt](./requirements.txt))  
  Tkinter est inclus avec Python sur de nombreuses distributions.

## Installation

1. **Cloner le d�p�t :**

   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-depot.git
   cd nom-du-depot
   ```

2. **(Optionnel) Cr�er et activer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Windows : venv\Scripts\activate
   ```

3. **Installer les d�pendances :**

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Ex�cutez le script principal : 

python youtube_clip_downloader.py
