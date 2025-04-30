import os
import json
import csv
from utilisateur import Utilisateur
from forum import Forum
from publication import Publication
from commentaire import Commentaire
from datetime import datetime

# Créer le dossier 'data' s'il n'existe pas
if not os.path.exists("data"):
    os.makedirs("data")

class BD:
    def __init__(self):
        # Initialisation des listes d'objets
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
       
        self.charger_donnees()  # Charger les données depuis les fichiers

    def charger_donnees(self):
        # 1. Charger d'abord les forums
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

        # 2. Charger ensuite les utilisateurs
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

        # 3. Charger les publications
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

        # 4. Charger les commentaires
        try:
            with open("data/commentaires.json", "r", encoding="utf-8") as f:
                self.commentaires = [Commentaire(**x) for x in json.load(f)]
        except:
            self.commentaires = []

    def sauvegarder_utilisateurs(self):
        # Sauvegarde des utilisateurs avec la liste de forums rejoints
        with open("data/utilisateur.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "courriel", "mot_de_passe", "forums"])
            for u in self.utilisateurs:
                noms_forums = [f.nom for f in self.forums if f.id in u.forums]
                writer.writerow([u.id, u.username, u.courriel, u.mot_de_passe, ";".join(noms_forums)])

    def sauvegarder_forums(self):
        # Sauvegarde des forums avec la liste de leurs publications
        with open("data/forum.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nom", "description", "publications"])
            for forum in self.forums:
                publications_str = ";".join(str(pub_id) for pub_id in forum.publications)
                writer.writerow([forum.id, forum.nom, forum.description, publications_str])

    def sauvegarder(self):
        # Sauvegarde complète de la base de données (CSV et JSON)
        self.sauvegarder_utilisateurs()
        self.sauvegarder_forums()

        # Sauvegarder publications avec texte des commentaires
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

        # Sauvegarder commentaires
        with open("data/commentaires.json", "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in self.commentaires], f, ensure_ascii=False, indent=2)
