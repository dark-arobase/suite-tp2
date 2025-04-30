class Publication:
    def __init__(self, titre, contenu, auteur, forum):
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
        self.forum = forum
        self.commentaires = []

    def ajouter_commentaire(self, commentaire):
        self.commentaires.append(commentaire)

    def __str__(self):
        return f"{self.titre} by {self.auteur.nom}"
