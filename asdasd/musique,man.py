import tkinter as tk
import pygame
import os

# Changer le répertoire de travail
os.chdir(r"C:\Users\mchir\Downloads\suite-tp2")

# Initialiser pygame pour la musique
pygame.mixer.init()

# Fonction pour jouer la musique
def jouer_musique():
    #pygame.mixer.music.load("yokoso.mp3")
    pygame.mixer.music.load("yokoso.mp3")  # Utilise le fichier dans le même répertoire
    pygame.mixer.music.play(loops=-1)  # Boucle infinie

# Fonction pour mettre en pause la musique
def pause_musique():
    pygame.mixer.music.pause()

# Fonction pour reprendre la musique
def reprendre_musique():
    pygame.mixer.music.unpause()

# Fonction pour arrêter la musique
def arreter_musique():
    pygame.mixer.music.stop()

# Interface Tkinter
root = tk.Tk()
root.title("Contrôle de la musique")
root.geometry("300x200")

# Ajouter des boutons pour contrôler la musique
tk.Button(root, text="Jouer", command=jouer_musique).pack(pady=10)
tk.Button(root, text="Pause", command=pause_musique).pack(pady=10)
tk.Button(root, text="Reprendre", command=reprendre_musique).pack(pady=10)
tk.Button(root, text="Arrêter", command=arreter_musique).pack(pady=10)

# Lancer l'interface Tkinter
root.mainloop()
