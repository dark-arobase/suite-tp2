class Commentaire:
    def __init__(self, contenu, auteur, publication):
        self.contenu = contenu
        self.auteur = auteur
        self.publication = publication

    def __str__(self):
        return f"{self.auteur.nom}: {self.contenu}"
