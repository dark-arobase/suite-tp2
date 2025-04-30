import tkinter as tk
from tkinter import simpledialog, messagebox
from models.forum import Forum

def creer_forum(forums):
    nom = simpledialog.askstring("Nom du forum", "Nom")
    desc = simpledialog.askstring("Description", "Description")
    if nom and desc:
        forums.append(Forum(nom, desc))
        messagebox.showinfo("Forum", "Forum créé !")

def rejoindre_forum(utilisateur, forums):
    if not utilisateur:
        messagebox.showwarning("Erreur", "Connectez-vous d'abord.")
        return
    options = "\n".join([f"{i+1}. {f.nom}" for i, f in enumerate(forums)])
    idx = simpledialog.askinteger("Rejoindre un forum", f"Choisir un forum:\n{options}")
    if idx and 1 <= idx <= len(forums):
        forum = forums[idx - 1]
        if forum not in utilisateur.forums:
            utilisateur.rejoindre_forum(forum)
            messagebox.showinfo("Succès", f"Rejoint le forum : {forum.nom}")
