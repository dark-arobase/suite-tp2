import tkinter as tk
import os

def quitter_et_lancer_piege():
    os.system('"C:/Program Files/Python312/python.exe" asdasd/piege.py')  # <-- exécute le fichier piege.py
    root.destroy()

def ouvrir_fenetre_utilisateur():
    # On efface tout le contenu de la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()

    # Et on affiche le nouveau contenu
    tk.Label(root, text="Créer un utilisateur", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Nom d'utilisateur :", font=("Arial", 14)).pack(pady=5)
    tk.Entry(root).pack(pady=5)
    tk.Label(root, text="Mot de passe :", font=("Arial", 14)).pack(pady=5)
    tk.Entry(root, show="*").pack(pady=5)
    tk.Button(root, text="Valider", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Retour au menu", font=("Arial", 14)).pack(pady=20)

def afficher_menu():
    # On efface les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="---- Menu ----", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Choisissez une option :", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="1. Créer un utilisateur", command=ouvrir_fenetre_utilisateur, font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="2. Créer un forum", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="3. Créer une publication", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="4. Ajouter un commentaire à une publication", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="5. Joindre un forum", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="6. Quitter", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="va te faire un café ?", font=("Arial", 16)).pack(pady=10)
    tk.Button(root,text="8. Voulez-vous faire un commentaire ?", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Quitter", command=quitter_et_lancer_piege).pack(pady=20)
    tk.Entry(root).pack()

# Lancement initial du menu
root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("600x650")
root.configure(bg="white")
afficher_menu()
root.mainloop()
'''
import tkinter as tk
import os

def quitter_et_lancer_piege():
    os.system('"C:/Program Files/Python312/python.exe" piege.py')  # Assurez-vous que piege.py est au bon endroit
    root.destroy()

root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("600x650")
root.configure(bg="white")

tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="---- Menu ----", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Choisissez une option :", font=("Arial", 16)).pack(pady=10)

etat = tk.Label(root, text="Non connecté", font=("Arial", 12))
etat.pack(pady=10)

menu_bar = tk.Menu(root)

# Menu Utilisateur
menu_utilisateur = tk.Menu(menu_bar, tearoff=0)
menu_utilisateur.add_command(label="Créer")
menu_utilisateur.add_command(label="Se connecter")
menu_utilisateur.add_command(label="Modifier")
menu_utilisateur.add_command(label="Supprimer")
menu_bar.add_cascade(label="Utilisateur", menu=menu_utilisateur)

# Menu Forum
menu_forum = tk.Menu(menu_bar, tearoff=0)
menu_forum.add_command(label="Créer forum")
menu_forum.add_command(label="Rejoindre forum")
menu_bar.add_cascade(label="Forum", menu=menu_forum)

# Menu Publication
menu_publication = tk.Menu(menu_bar, tearoff=0)
menu_publication.add_command(label="Créer publication")
menu_bar.add_cascade(label="Publication", menu=menu_publication)

# Menu Commentaire
menu_commentaire = tk.Menu(menu_bar, tearoff=0)
menu_commentaire.add_command(label="Ajouter commentaire")
menu_bar.add_cascade(label="Commentaire", menu=menu_commentaire)

root.config(menu=menu_bar)

# Boutons
tk.Button(root, text="1. Créer un utilisateur", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="2. Créer un forum", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="3. Créer une publication", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="4. Ajouter un commentaire à une publication", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="5. Joindre un forum", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="6. Quitter", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Va te faire un café ?", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="8. Voulez-vous faire un commentaire ?", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Quitter", command=quitter_et_lancer_piege).pack(pady=20)
tk.Entry(root).pack()

root.mainloop()

'''