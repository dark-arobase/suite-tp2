class Forum:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.publications = []

    def ajouter_publication(self, publication):
        self.publications.append(publication)

    def __str__(self):
        return f"{self.nom}: {self.description}"
