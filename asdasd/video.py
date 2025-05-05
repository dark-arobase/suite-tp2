import tkinter as tk
import pygame
import cv2
from PIL import Image, ImageTk

# Initialiser Pygame pour la musique
pygame.mixer.init()

# Fonction pour jouer la musique
def jouer_musique():
    try:
        pygame.mixer.music.load("wh.mp3")  # Remplace par ton fichier audio
        pygame.mixer.music.play(loops=-1)  # Boucle infinie
    except pygame.error:
        print("Erreur : Le fichier 'wh.mp3' n'a pas été trouvé.")

# Fonction pour afficher la vidéo
def afficher_video():
    global cap
    cap = cv2.VideoCapture("alw.mp4")  # Remplace par ton fichier vidéo
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir la vidéo")
        return

    def lire_frame():
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(img)
            video_label.config(image=img_tk)
            video_label.image = img_tk
            root.after(20, lire_frame)  # Affiche chaque frame avec un délai de 20ms
        else:
            cap.release()

    lire_frame()

# Fonction pour afficher des mots à intervalles
def afficher_mots():
    words = ["alors comme ça, tu veux partir?", "tu crois que je vais te laisser partir?", "tu es à moi", "il n'y a pas d'échappatoire?"]
    current_word = 0

    def changer_mot():
        nonlocal current_word
        if current_word < len(words):
            dialogue_label.config(text=words[current_word])
            current_word += 1
            root.after(5000, changer_mot)  # Met à jour le mot toutes les 5 secondes

    changer_mot()

# Fonction pour afficher "Je suis toujours là" après 5 secondes
def afficher_message():
    dialogue_label.config(text="créves....")

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Vidéo avec audio et messages")
root.geometry("800x600")
root.configure(bg="black")  # Fond noir

# Label pour afficher la vidéo
video_label = tk.Label(root, bg="black")
video_label.pack(fill="both", expand=True)  # Remplir toute la fenêtre

# Ajouter un label pour afficher les messages
dialogue_label = tk.Label(root, text="", font=("Arial", 20), fg="white", bg="black")
dialogue_label.pack(pady=10)

# Lancer la vidéo et la musique
afficher_video()
jouer_musique()

# Afficher les mots et le message après 5 secondes
afficher_mots()
root.after(5000, afficher_message)

# Lancer l'interface
root.mainloop()

# Nettoyage après la fin
pygame.mixer.quit()
if cap:
    cap.release()
