import tkinter as tk
from tkinter import simpledialog, messagebox
from models.commentaire import Commentaire

def ajouter_commentaire(utilisateur, publication):
    if not utilisateur:
        messagebox.showwarning("Erreur", "Connectez-vous d'abord.")
        return
    contenu = simpledialog.askstring("Commentaire", "Votre commentaire")
    if contenu:
        commentaire = Commentaire(contenu, utilisateur)
        publication.commentaires.append(commentaire)
        messagebox.showinfo("Commentaire", "Commentaire ajouté !")
