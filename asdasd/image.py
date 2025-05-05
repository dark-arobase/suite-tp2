import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
import cv2

# Changer le répertoire de travail
os.chdir(r"C:\Users\mchir\Downloads\suite-tp2")

# Initialiser pygame pour la musique
pygame.mixer.init()

# Variable globale pour la vidéo
cap = None

# Fonction pour animer le déplacement du personnage
def animer_deplacement():
    x = personnage_label.winfo_x() + 10
    if x < 350:
        personnage_label.place(x=x, y=150)
        root.after(50, animer_deplacement)
    else:
        personnage_label.place(x=50, y=150)

# Fonction pour jouer la musique
def jouer_musique():
    try:
        pygame.mixer.music.load("yokoso.mp3")
        pygame.mixer.music.play(loops=-1)
    except pygame.error:
        dialogue_label.config(text="Erreur de musique : Fichier non trouvé.")
        print("Erreur : Le fichier 'yokoso.mp3' n'a pas été trouvé.")

# Fonction pour afficher la vidéo immédiatement
def afficher_video():
    global cap
    cap = cv2.VideoCapture("alw.mp4")
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

            root.after(20, lire_frame)
        else:
            cap.release()

    lire_frame()

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Piège vidéo")
root.geometry("800x600")
root.configure(bg="black")  # Fond noir

# Charger l'image du personnage
personnage_image = Image.open("die.jpg")
personnage_image = personnage_image.resize((150, 150), Image.Resampling.LANCZOS)
personnage_photo = ImageTk.PhotoImage(personnage_image)

# Label personnage
personnage_label = tk.Label(root, image=personnage_photo, bg="black")
personnage_label.place(x=50, y=150)

# Label vidéo
video_label = tk.Label(root, bg="black")
video_label.place(x=250, y=50)

# Label de dialogue
dialogue_label = tk.Label(root, text="Trop tard, tu es pris au piège ! 😈", font=("Arial", 14),
                          fg="white", bg="black")
dialogue_label.pack(pady=10)

# Lancer automatiquement l'animation et la vidéo
animer_deplacement()
jouer_musique()
afficher_video()

# Lancer l'interface
root.mainloop()

# Nettoyage
pygame.mixer.quit()
if cap:
    cap.release()
