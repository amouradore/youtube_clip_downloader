# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import os

def download_youtube_clip(url, start_time, end_time, output_filename):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Meilleure qualité vidéo + audio
        'outtmpl': output_filename,
        'download_ranges': lambda info, ctx: [{
            'start_time': start_time,
            'end_time': end_time,
        }],
        'force_generic_extractor': True,
        'merge_output_format': 'mp4'  # Assure que la sortie est en MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
def on_submit():
    url = url_entry.get()
    start_time = int(start_time_entry.get())
    end_time = int(end_time_entry.get())
    output_filename = output_filename_entry.get()

    if not output_filename.endswith('.mp4'):
        output_filename += '.mp4'

    try:
        download_youtube_clip(url, start_time, end_time, output_filename)
        messagebox.showinfo("Succes", "Telechargement termine !\nFichier sauvegarde : {}".format(output_filename))
    except Exception as e:
        messagebox.showerror("Erreur", "Une erreur s'est produite : {}".format(str(e)))

def browse_output_location():
    filename = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Fichiers MP4", "*.mp4")])
    if filename:
        output_filename_entry.delete(0, tk.END)
        output_filename_entry.insert(0, filename)

# Creer la fenetre principale
root = tk.Tk()
root.title("Telechargeur d'extrait YouTube")

# Creer et placer les widgets
tk.Label(root, text="URL de la video:").grid(row=0, column=0, sticky="e")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Temps de debut (secondes):").grid(row=1, column=0, sticky="e")
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Temps de fin (secondes):").grid(row=2, column=0, sticky="e")
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Nom du fichier de sortie:").grid(row=3, column=0, sticky="e")
output_filename_entry = tk.Entry(root)
output_filename_entry.grid(row=3, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Parcourir", command=browse_output_location)
browse_button.grid(row=3, column=2, padx=5, pady=5)

submit_button = tk.Button(root, text="Telecharger", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Lancer la boucle principale
root.mainloop()

print("Programme termine")