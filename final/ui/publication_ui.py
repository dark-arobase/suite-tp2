import tkinter as tk
from tkinter import simpledialog, messagebox
from models.publication import Publication

def creer_publication(utilisateur, forum):
    if not utilisateur:
        messagebox.showwarning("Erreur", "Connectez-vous d'abord.")
        return
    titre = simpledialog.askstring("Titre", "Titre de la publication")
    contenu = simpledialog.askstring("Contenu", "Contenu de la publication")
    if titre and contenu:
        publication = Publication(titre, contenu, utilisateur)
        forum.publications.append(publication)
        messagebox.showinfo("Publication", "Publication ajoutée !")
