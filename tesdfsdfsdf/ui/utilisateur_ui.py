import tkinter as tk
from tkinter import simpledialog, messagebox
from models.utilisateur import Utilisateur

def creer_utilisateur(utilisateurs):
    nom = simpledialog.askstring("Nom", "Entrez le nom")
    email = simpledialog.askstring("Email", "Entrez l'email")
    mdp = simpledialog.askstring("Mot de passe", "Entrez le mot de passe", show="*")
    if nom and email and mdp:
        utilisateurs.append(Utilisateur(nom, email, mdp))
        messagebox.showinfo("Succès", "Utilisateur créé.")

def se_connecter(utilisateurs):
    email = simpledialog.askstring("Connexion", "Email :")
    mdp = simpledialog.askstring("Connexion", "Mot de passe :", show="*")
    for u in utilisateurs:
        if u.email == email and u.mot_de_passe == mdp:
            messagebox.showinfo("Bienvenue", f"Connecté en tant que {u.nom}")
            return u
    messagebox.showerror("Erreur", "Utilisateur non trouvé.")
    return None

def modifier_utilisateur(utilisateur):
    if utilisateur:
        utilisateur.nom = simpledialog.askstring("Modifier nom", "Nouveau nom :", initialvalue=utilisateur.nom)
        utilisateur.email = simpledialog.askstring("Modifier email", "Nouvel email :", initialvalue=utilisateur.email)
        utilisateur.mot_de_passe = simpledialog.askstring("Mot de passe", "Nouveau mot de passe :", show="*")
        messagebox.showinfo("Succès", "Modifié.")
    else:
        messagebox.showwarning("Erreur", "Pas connecté.")

def supprimer_utilisateur(utilisateurs, utilisateur):
    if utilisateur:
        utilisateurs.remove(utilisateur)
        messagebox.showinfo("Supprimé", "Compte supprimé.")
        return None
    else:
        messagebox.showwarning("Erreur", "Pas connecté.")
        return utilisateur

