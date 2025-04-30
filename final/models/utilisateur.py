class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.forums = []

    def rejoindre_forum(self, forum):
        if forum not in self.forums:
            self.forums.append(forum)

    def __str__(self):
        return f"{self.nom} ({self.email})"
