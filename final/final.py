import tkinter as tk
import os

def quitter_et_lancer_piege():
    os.system('"C:/Program Files/Python312/python.exe" asdasd/piege.py')  # <-- exécute le fichier piege.py
    root.destroy()

root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("600x650")
root.configure(bg="white")


tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="---- Menu ----", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Choisissez une option :", font=("Arial", 16)).pack(pady=10)

menu_bar = tk.Menu(root)

etat = tk.Label(root, text="Non connecté", font=("Arial", 12))
etat.pack(pady=10)

menu_utilisateur = menu_bar, tearoff=0
menu_utilisateur.add_command(label="Créer")
menu_utilisateur.add_command(label="Se connecter")
menu_utilisateur.add_command(label="Modifier")
menu_utilisateur.add_command(label="Supprimer")
menu_bar.add_cascade(label="Utilisateur")

menu_forum = menu_bar, tearoff=0
menu_forum.add_command(label="Créer forum")
menu_forum.add_command(label="Rejoindre forum")
menu_bar.add_cascade(label="Forum", menu=menu_forum)

menu_publication = menu_bar, tearoff=0
menu_publication.add_command(label="Créer publication")
menu_bar.add_cascade(label="Publication", menu=menu_publication)

menu_commentaire = menu_bar, tearoff=0
menu_commentaire.add_command(label="Ajouter commentaire")
menu_bar.add_cascade(label="Commentaire", menu=menu_commentaire)

root.config(menu=menu_bar)

tk.Button(root,text="1. Créer un utilisateur", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="2. Créer un forum", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="3.Créer une publication", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="4. Ajouter un commentaire à une publication", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="5. Joindre un forum", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="6. Quitter", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="va te faire un café ?", font=("Arial", 16)).pack(pady=10)
tk.Button(root,text="8 voulais vous faire un commentaire", font=("Arial", 16)).pack(pady=10)


tk.Button(root, text="Quitter", command=quitter_et_lancer_piege).pack(pady=20)
tk.Entry(root).pack()

root.mainloop()




'''
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
resultats.pack()'''