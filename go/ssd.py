import os
import json
import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Créer les classes Utilisateur, Forum, Publication et Commentaire

class Utilisateur:
    def __init__(self, id, username, courriel, mot_de_passe, forums=None):
        self.id = id
        self.username = username
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe
        self.forums = forums if forums is not None else []

class Forum:
    def __init__(self, id, nom, description):
        self.id = id
        self.nom = nom
        self.description = description
        self.publications = []

class Publication:
    def __init__(self, id, titre, contenu, date_creation, id_auteur, id_forum):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation
        self.id_auteur = id_auteur
        self.id_forum = id_forum
        self.commentaires = []

class Commentaire:
    def __init__(self, id, contenu, date_creation, id_auteur, id_publication):
        self.id = id
        self.contenu = contenu
        self.date_creation = date_creation
        self.id_auteur = id_auteur
        self.id_publication = id_publication

# Créer le dossier 'data' s'il n'existe pas
if not os.path.exists("data"):
    os.makedirs("data")

# Classe BD pour gérer les données
class BD:
    def __init__(self):
        self.utilisateurs = []
        self.forums = []
        self.publications = []
        self.commentaires = []

        try:
            with open("data/rejoindre_forum.csv", "r", encoding="utf-8") as f:
                pass
        except FileNotFoundError:
            with open("data/rejoindre_forum.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id_utilisateur", "nom_utilisateur", "id_forum", "nom_forum"])

        self.charger_donnees()

    def charger_donnees(self):
        try:
            with open("data/forum.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.forums = []
                for row in reader:
                    forum = Forum(int(row["id"]), row["nom"], row["description"])
                    if "publications" in row and row["publications"]:
                        forum.publications = list(map(int, row["publications"].split(";")))
                    self.forums.append(forum)
        except:
            self.forums = []

        try:
            with open("data/utilisateur.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.utilisateurs = []
                for row in reader:
                    forums_ids = []
                    if row["forums"]:
                        noms_forums = row["forums"].split(";")
                        for nom in noms_forums:
                            forum = self.obtenir_forum_par_nom(nom.strip())
                            if forum:
                                forums_ids.append(forum.id)
                    utilisateur = Utilisateur(
                        int(row["id"]),
                        row["username"],
                        row["courriel"],
                        row["mot_de_passe"],
                        forums_ids
                    )
                    self.utilisateurs.append(utilisateur)
        except:
            self.utilisateurs = []

        try:
            with open("data/publications.json", "r", encoding="utf-8") as f:
                publications_data = json.load(f)
                self.publications = []
                for pub_data in publications_data:
                    p = Publication(
                        pub_data["id"],
                        pub_data["titre"],
                        pub_data["contenu"],
                        pub_data["date_creation"],
                        pub_data["id_auteur"],
                        pub_data["id_forum"]
                    )
                    p.commentaires = pub_data.get("commentaires", [])
                    self.publications.append(p)
        except:
            self.publications = []

        try:
            with open("data/commentaires.json", "r", encoding="utf-8") as f:
                self.commentaires = [Commentaire(**x) for x in json.load(f)]
        except:
            self.commentaires = []

    def sauvegarder_utilisateurs(self):
        with open("data/utilisateur.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "courriel", "mot_de_passe", "forums"])
            for u in self.utilisateurs:
                noms_forums = [f.nom for f in self.forums if f.id in u.forums]
                writer.writerow([u.id, u.username, u.courriel, u.mot_de_passe, ";".join(noms_forums)])

    def sauvegarder_forums(self):
        with open("data/forum.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nom", "description", "publications"])
            for forum in self.forums:
                publications_str = ";".join(str(pub_id) for pub_id in forum.publications)
                writer.writerow([forum.id, forum.nom, forum.description, publications_str])

    def sauvegarder(self):
        self.sauvegarder_utilisateurs()
        self.sauvegarder_forums()

        publications_a_sauver = []
        for p in self.publications:
            pub_data = {
                "id": p.id,
                "titre": p.titre,
                "contenu": p.contenu,
                "date_creation": p.date_creation,
                "id_auteur": p.id_auteur,
                "id_forum": p.id_forum,
                "commentaires": p.commentaires
            }
            publications_a_sauver.append(pub_data)

        with open("data/publications.json", "w", encoding="utf-8") as f:
            json.dump(publications_a_sauver, f, ensure_ascii=False, indent=2)

        with open("data/commentaires.json", "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in self.commentaires], f, ensure_ascii=False, indent=2)

    def obtenir_utilisateur_par_nom(self, nom):
        return next((u for u in self.utilisateurs if u.username == nom), None)

    def obtenir_forum_par_nom(self, nom):
        return next((f for f in self.forums if f.nom == nom), None)

    def creer_utilisateur(self, username, courriel, mot_de_passe):
        id_utilisateur = len(self.utilisateurs) + 1
        utilisateur = Utilisateur(id_utilisateur, username, courriel, mot_de_passe)
        self.utilisateurs.append(utilisateur)
        self.sauvegarder()

    def creer_forum(self, nom, description=""):
        id_forum = len(self.forums) + 1
        forum = Forum(id_forum, nom, description)
        self.forums.append(forum)
        self.sauvegarder()

    def creer_publication(self, titre, contenu, id_auteur, id_forum):
        id_pub = len(self.publications) + 1
        publication = Publication(id_pub, titre, contenu, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_auteur, id_forum)
        self.publications.append(publication)
        self.sauvegarder()

    def creer_commentaire(self, contenu, id_auteur, id_publication):
        id_com = len(self.commentaires) + 1
        commentaire = Commentaire(id_com, contenu, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_auteur, id_publication)
        self.commentaires.append(commentaire)
        self.sauvegarder()

    def joindre_forum(self, utilisateur, forum):
        u = self.obtenir_utilisateur_par_nom(utilisateur)
        f = self.obtenir_forum_par_nom(forum)
        if u and f:
            u.forums.append(f.id)
            self.sauvegarder()

# Interface utilisateur avec Tkinter

bd = BD()

def ouvrir_fenetre_utilisateur():
    f = tk.Toplevel(root)
    f.title("Créer un utilisateur")
    f.geometry("300x250")
    tk.Label(f, text="Nom d'utilisateur").pack()
    entry_nom = tk.Entry(f)
    entry_nom.pack()
    tk.Label(f, text="Courriel").pack()
    entry_mail = tk.Entry(f)
    entry_mail.pack()
    tk.Label(f, text="Mot de passe").pack()
    entry_mdp = tk.Entry(f, show="*")
    entry_mdp.pack()

    def valider():
        nom = entry_nom.get()
        mail = entry_mail.get()
        mdp = entry_mdp.get()
        bd.creer_utilisateur(nom, mail, mdp)
        messagebox.showinfo("Succès", "Utilisateur créé avec succès.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_forum():
    f = tk.Toplevel(root)
    f.title("Créer un forum")
    f.geometry("300x250")
    tk.Label(f, text="Nom du forum").pack()
    entry_nom = tk.Entry(f)
    entry_nom.pack()
    tk.Label(f, text="Description").pack()
    entry_desc = tk.Entry(f)
    entry_desc.pack()

    def valider():
        nom = entry_nom.get()
        desc = entry_desc.get()
        bd.creer_forum(nom, desc)
        messagebox.showinfo("Succès", "Forum créé avec succès.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_publication():
    f = tk.Toplevel(root)
    f.title("Créer une publication")
    f.geometry("300x300")
    tk.Label(f, text="Titre de la publication").pack()
    entry_titre = tk.Entry(f)
    entry_titre.pack()
    tk.Label(f, text="Contenu de la publication").pack()
    entry_contenu = tk.Entry(f)
    entry_contenu.pack()

    def valider():
        titre = entry_titre.get()
        contenu = entry_contenu.get()
        # Utiliser des valeurs d'exemple pour les utilisateurs et forums
        bd.creer_publication(titre, contenu, 1, 1)
        messagebox.showinfo("Succès", "Publication créée avec succès.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_commentaire():
    f = tk.Toplevel(root)
    f.title("Ajouter un commentaire")
    f.geometry("300x250")
    tk.Label(f, text="Contenu du commentaire").pack()
    entry_commentaire = tk.Entry(f)
    entry_commentaire.pack()

    def valider():
        commentaire = entry_commentaire.get()
        # Utiliser des valeurs d'exemple pour les utilisateurs et publications
        bd.creer_commentaire(commentaire, 1, 1)
        messagebox.showinfo("Succès", "Commentaire ajouté avec succès.")
        f.destroy()

    tk.Button(f, text="Ajouter", command=valider).pack(pady=10)

def joindre_forum():
    f = tk.Toplevel(root)
    f.title("Joindre un forum")
    f.geometry("300x250")
    tk.Label(f, text="Nom d'utilisateur").pack()
    entry_utilisateur = tk.Entry(f)
    entry_utilisateur.pack()
    tk.Label(f, text="Nom du forum").pack()
    entry_forum = tk.Entry(f)
    entry_forum.pack()

    def valider():
        utilisateur = entry_utilisateur.get()
        forum = entry_forum.get()
        bd.joindre_forum(utilisateur, forum)
        messagebox.showinfo("Succès", "Utilisateur a rejoint le forum.")
        f.destroy()

    tk.Button(f, text="Joindre", command=valider).pack(pady=10)

def quitter():
    bd.sauvegarder()
    root.quit()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion Forum")
root.geometry("400x400")

# Ajouter les boutons pour chaque action
tk.Button(root, text="Créer un utilisateur", command=ouvrir_fenetre_utilisateur).pack(pady=10)
tk.Button(root, text="Créer un forum", command=ouvrir_fenetre_forum).pack(pady=10)
tk.Button(root, text="Créer une publication", command=ouvrir_fenetre_publication).pack(pady=10)
tk.Button(root, text="Ajouter un commentaire", command=ouvrir_fenetre_commentaire).pack(pady=10)
tk.Button(root, text="Joindre un forum", command=joindre_forum).pack(pady=10)
tk.Button(root, text="Quitter", command=quitter).pack(pady=10)

# Lancer l'application
root.mainloop()
