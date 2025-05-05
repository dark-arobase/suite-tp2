# piege.py
import tkinter as tk
from tkinter import messagebox
import pygame
import os

def refuser_de_partir():
    messagebox.showwarning("Trop tard 😈", "Tu ne peux pas fermer cette fenêtre si facilement !")

def quitter_vraiment():
    pygame.mixer.music.stop()
    root.destroy()

# Vérifier si le fichier audio existe
audio_file = "yokoso.mp3"  # Remplace par ton fichier
if os.path.exists(audio_file):
    print(f"Le fichier {audio_file} existe. Initialisation de pygame...")
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(loops=-1)  # Boucle infinie
else:
    print(f"Erreur : Le fichier {audio_file} n'existe pas.")
    
# Interface
root = tk.Tk()
root.title("Piège activé")
root.geometry("300x200")
tk.Label(root, text="Trop tard, le piège est lancé 😈", font=("Arial", 12)).pack(pady=20)

# Boutons
tk.Button(root, text="Essaye de quitter", command=refuser_de_partir).pack(pady=5)
tk.Button(root, text="Quitter vraiment", command=quitter_vraiment).pack(pady=5)

# Bloquer la fermeture par la croix rouge
root.protocol("WM_DELETE_WINDOW", refuser_de_partir)

root.mainloop()
