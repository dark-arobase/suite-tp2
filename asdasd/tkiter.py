import tkinter as tk
import os

def quitter_et_lancer_piege():
    os.system('"C:/Program Files/Python312/python.exe" asdasd/piege.py')  # <-- exécute le fichier piege.py
    root.destroy()

root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("600x600")
root.configure(bg="white")


tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="---- Menu ----", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Choisissez une option :", font=("Arial", 16)).pack(pady=10)
tk.Entry(
    root,
    text="1. Créer un utilisateur\n2. Créer un forum\n3. Créer une publication\n"
         "4. Ajouter un commentaire à une publication\n5. Joindre un forum\n6. Quitter\n"
         "va te faire un café ? \n8 voulais vous faire un commentaire",
    font=("Arial", 12)
).pack()

# Champ de saisie pour le nom d'utilisateur
champ_nom = tk.Entry(root)
champ_nom.pack()

# Text
tk.Label(root, text="Commentaires :").pack()
zone_texte = tk.Text(root, height=5, width=30)
zone_texte.pack()
# Listbox
tk.Label(root, text="Choisissez un élément :").pack()
liste = tk.Listbox(root, height=4)
for item in ["Élément 1", "Élément 2", "Élément 3", "Élément 4"]:
    liste.insert(tk.END, item)
liste.pack()

# Button
def valider():
    resultats.delete("1.0", tk.END)  # Efface le contenu précédent
    resultats.insert(tk.END, f"Nom : {champ_nom.get()}\n")
    resultats.insert(tk.END, f"Commentaires : {zone_texte.get('1.0', tk.END).strip()}\n")
    resultats.insert(tk.END, f"Élément sélectionné : {liste.get(tk.ACTIVE)}\n")
    resultats.insert(tk.END, "Vous avez cliqué sur le bouton !\n")

tk.Button(root, text="Valider", command=valider).pack()
# Zone de texte pour afficher les résultats
resultats = tk.Text(root, height=10, width=50)
resultats.pack()

tk.Button(root, text="Quitter", command=quitter_et_lancer_piege).pack(pady=20)
tk.Entry(root).pack()

root.mainloop()

'''
def afficher_menu():
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")

def main():
    bd = BD()
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6): ")
        
        # Option 1 : Créer un utilisateur
        if choix == '1':
            username = input("Nom d'utilisateur: ")
            courriel = input("Courriel: ")
            mot_de_passe = input("Mot de passe: ")
            bd.creer_utilisateur(username, courriel, mot_de_passe)
        # Option 2 : Créer un forum
        elif choix == '2':
            nom = input("Nom du forum: ")
            desc = input("Description (facultatif): ")
            bd.creer_forum(nom, desc)
        # Option 3 : Créer une publication
        elif choix == '3':
            titre = input("Titre: ")
            contenu = input("Contenu: ")
            auteur = input("Nom d'utilisateur de l'auteur: ")
            forum = input("Nom du forum: ")
            u = bd.obtenir_utilisateur_par_nom(auteur)
            f = bd.obtenir_forum_par_nom(forum)
            if u and f:
                bd.creer_publication(titre, contenu, u.id, f.id)
            else:
                print("Auteur ou forum introuvable.")
        # Option 4 : Ajouter un commentaire à une publication
        elif choix == '4':
            contenu = input("Contenu du commentaire: ")
            auteur = input("Nom d'utilisateur de l'auteur: ")
            titre_pub = input("Titre de la publication: ")
            u = bd.obtenir_utilisateur_par_nom(auteur)
            p = next((p for p in bd.publications if p.titre == titre_pub), None)
            if u and p:
                bd.creer_commentaire(contenu, u.id, p.id)
            else:
                print("Auteur ou publication introuvable.")
        # Option 5 : Joindre un forum
        elif choix == '5':
            utilisateur = input("Nom d'utilisateur: ")
            forum = input("Nom du forum à joindre: ")
            bd.joindre_forum(utilisateur, forum)
        # Option 6 : Quitter
        elif choix == '6':
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break
        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)   # Pause de 1 seconde avant de réafficher le menu'''