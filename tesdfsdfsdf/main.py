import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from ui.utilisateur_ui import creer_utilisateur, se_connecter, modifier_utilisateur, supprimer_utilisateur
from ui.forum_ui import creer_forum, rejoindre_forum
from ui.publication_ui import creer_publication
from ui.commentaire_ui import ajouter_commentaire
from models.utilisateur import Utilisateur
from models.forum import Forum
from models.publication import Publication
from models.commentaire import Commentaire

# Données en mémoire
utilisateurs = []
forums = []
utilisateur_actif = None

# Fenêtre principale
fen = tk.Tk()
fen.geometry("500x300")
fen.title("Forum Tkinter")

etat = tk.Label(fen, text="Non connecté", font=("Arial", 12))
etat.pack(pady=10)

# --- Fonctions pour le menu ---
def wrapper_creer_utilisateur():
    creer_utilisateur(utilisateurs)

def wrapper_se_connecter():
    global utilisateur_actif
    utilisateur_actif = se_connecter(utilisateurs)
    if utilisateur_actif:
        etat.config(text=f"Connecté : {utilisateur_actif.nom}")

def wrapper_modifier_utilisateur():
    modifier_utilisateur(utilisateur_actif)

def wrapper_supprimer_utilisateur():
    global utilisateur_actif
    utilisateur_actif = supprimer_utilisateur(utilisateurs, utilisateur_actif)
    if not utilisateur_actif:
        etat.config(text="Non connecté")

def wrapper_creer_forum():
    creer_forum(forums)

def wrapper_rejoindre_forum():
    rejoindre_forum(utilisateur_actif, forums)

def wrapper_creer_publication():
    if utilisateur_actif and utilisateur_actif.forums:
        options = [f.nom for f in utilisateur_actif.forums]
        forum_name = simpledialog.askstring("Choix forum", f"Dans quel forum ?\nOptions : {', '.join(options)}")
        forum = next((f for f in utilisateur_actif.forums if f.nom == forum_name), None)
        if forum:
            creer_publication(utilisateur_actif, forum)
        else:
            messagebox.showerror("Erreur", "Forum introuvable.")
    else:
        messagebox.showwarning("Erreur", "Vous n'avez rejoint aucun forum.")

def wrapper_ajouter_commentaire():
    if utilisateur_actif and utilisateur_actif.forums:
        forum = utilisateur_actif.forums[0]  # simplification : on prend le premier
        if forum.publications:
            publication = forum.publications[0]  # simplification : on commente la 1ère
            ajouter_commentaire(utilisateur_actif, publication)
        else:
            messagebox.showwarning("Erreur", "Pas de publication.")
    else:
        messagebox.showwarning("Erreur", "Pas de forum ou publication.")

# --- Menu principal ---
menu_bar = tk.Menu(fen)

menu_utilisateur = tk.Menu(menu_bar, tearoff=0)
menu_utilisateur.add_command(label="Créer", command=wrapper_creer_utilisateur)
menu_utilisateur.add_command(label="Se connecter", command=wrapper_se_connecter)
menu_utilisateur.add_command(label="Modifier", command=wrapper_modifier_utilisateur)
menu_utilisateur.add_command(label="Supprimer", command=wrapper_supprimer_utilisateur)
menu_bar.add_cascade(label="Utilisateur", menu=menu_utilisateur)

menu_forum = tk.Menu(menu_bar, tearoff=0)
menu_forum.add_command(label="Créer forum", command=wrapper_creer_forum)
menu_forum.add_command(label="Rejoindre forum", command=wrapper_rejoindre_forum)
menu_bar.add_cascade(label="Forum", menu=menu_forum)

menu_publication = tk.Menu(menu_bar, tearoff=0)
menu_publication.add_command(label="Créer publication", command=wrapper_creer_publication)
menu_bar.add_cascade(label="Publication", menu=menu_publication)

menu_commentaire = tk.Menu(menu_bar, tearoff=0)
menu_commentaire.add_command(label="Ajouter commentaire", command=wrapper_ajouter_commentaire)
menu_bar.add_cascade(label="Commentaire", menu=menu_commentaire)

fen.config(menu=menu_bar)
fen.mainloop()