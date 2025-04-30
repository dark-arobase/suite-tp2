import tkinter as tk
from tkinter import messagebox

def afficher_resultat(texte):
    zone_resultats.config(state='normal')
    zone_resultats.delete("1.0", tk.END)
    zone_resultats.insert(tk.END, texte)
    zone_resultats.config(state='disabled')

def creer_utilisateur():
    afficher_resultat("Fonction: créer un utilisateur")

def creer_forum():
    afficher_resultat("Fonction: créer un forum")

def creer_publication():
    afficher_resultat("Fonction: créer une publication")

def ajouter_commentaire():
    afficher_resultat("Fonction: ajouter un commentaire")

def joindre_forum():
    afficher_resultat("Fonction: joindre un forum")

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter PyForum ?"):
        root.destroy()

def faire_un_cafe():
    afficher_resultat("Bonne idée ! Va te faire un café ☕")

# Fenêtre principale
root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("350x450")
root.configure(bg="lightblue")

# Titre
label = tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16, "bold"), bg="lightblue")
label.pack(pady=10)

# Boutons du menu
tk.Button(root, text="1. Créer un utilisateur", command=creer_utilisateur, width=30).pack(pady=2)
tk.Button(root, text="2. Créer un forum", command=creer_forum, width=30).pack(pady=2)
tk.Button(root, text="3. Créer une publication", command=creer_publication, width=30).pack(pady=2)
tk.Button(root, text="4. Ajouter un commentaire", command=ajouter_commentaire, width=30).pack(pady=2)
tk.Button(root, text="5. Joindre un forum", command=joindre_forum, width=30).pack(pady=2)
tk.Button(root, text="6. Quitter", command=quitter, width=30).pack(pady=2)
tk.Button(root, text="7. Va te faire un café ?", command=faire_un_cafe, width=30).pack(pady=10)

# Zone de résultats en bas
tk.Label(root, text="Résultat :", bg="lightblue").pack()
zone_resultats = tk.Text(root, height=5, width=40, state='disabled', bg="white")
zone_resultats.pack(pady=10)

root.mainloop()
