import pickle

def sauvegarder_donnees(utilisateurs, forums, fichier='data/save.pkl'):
    with open(fichier, 'wb') as f:
        pickle.dump({'utilisateurs': utilisateurs, 'forums': forums}, f)

def charger_donnees(fichier='data/save.pkl'):
    try:
        with open(fichier, 'rb') as f:
            donnees = pickle.load(f)
            return donnees['utilisateurs'], donnees['forums']
    except FileNotFoundError:
        return [], []
