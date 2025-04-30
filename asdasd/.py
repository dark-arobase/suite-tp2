import tkinter as tk
from tkinter import messagebox

# Simulations des données
utilisateurs = []
forums = []
publications = []
commentaires = []

class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe

class Forum:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

class Publication:
    def __init__(self, titre, contenu, auteur, forum):
        self.titre = titre
        self.contenu = contenu
        self.auteur = auteur
        self.forum = forum

class Commentaire:
    def __init__(self, contenu, auteur, publication):
        self.contenu = contenu
        self.auteur = auteur
        self.publication = publication

# Fonctions des fenêtres
def ouvrir_fenetre_utilisateur():
    fenetre = tk.Toplevel(root)
    fenetre.title("Créer un utilisateur")
    fenetre.geometry("300x250")

    tk.Label(fenetre, text="Nom d'utilisateur").pack()
    entry_nom = tk.Entry(fenetre)
    entry_nom.pack()

    tk.Label(fenetre, text="Courriel").pack()
    entry_mail = tk.Entry(fenetre)
    entry_mail.pack()

    tk.Label(fenetre, text="Mot de passe").pack()
    entry_mdp = tk.Entry(fenetre, show="*")
    entry_mdp.pack()

    def valider():
        nom = entry_nom.get()
        mail = entry_mail.get()
        mdp = entry_mdp.get()
        utilisateurs.append(Utilisateur(nom, mail, mdp))
        messagebox.showinfo("Succès", "Utilisateur créé avec succès.")
        fenetre.destroy()

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_forum():
    fenetre = tk.Toplevel(root)
    fenetre.title("Créer un forum")
    fenetre.geometry("300x200")

    tk.Label(fenetre, text="Nom du forum").pack()
    entry_nom = tk.Entry(fenetre)
    entry_nom.pack()

    tk.Label(fenetre, text="Description").pack()
    entry_desc = tk.Entry(fenetre)
    entry_desc.pack()

    def valider():
        nom = entry_nom.get()
        desc = entry_desc.get()
        forums.append(Forum(nom, desc))
        messagebox.showinfo("Succès", "Forum créé avec succès.")
        fenetre.destroy()

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_publication():
    fenetre = tk.Toplevel(root)
    fenetre.title("Créer une publication")
    fenetre.geometry("300x300")

    tk.Label(fenetre, text="Titre de la publication").pack()
    entry_titre = tk.Entry(fenetre)
    entry_titre.pack()

    tk.Label(fenetre, text="Contenu de la publication").pack()
    entry_contenu = tk.Entry(fenetre)
    entry_contenu.pack()

    tk.Label(fenetre, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(fenetre)
    entry_auteur.pack()

    tk.Label(fenetre, text="Forum de la publication").pack()
    entry_forum = tk.Entry(fenetre)
    entry_forum.pack()

    def valider():
        titre = entry_titre.get()
        contenu = entry_contenu.get()
        auteur_nom = entry_auteur.get()
        forum_nom = entry_forum.get()

        auteur = next((u for u in utilisateurs if u.nom == auteur_nom), None)
        forum = next((f for f in forums if f.nom == forum_nom), None)

        if auteur and forum:
            publications.append(Publication(titre, contenu, auteur, forum))
            messagebox.showinfo("Succès", "Publication créée avec succès.")
        else:
            messagebox.showerror("Erreur", "Auteur ou forum introuvable.")
        fenetre.destroy()

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_commentaire():
    fenetre = tk.Toplevel(root)
    fenetre.title("Ajouter un commentaire")
    fenetre.geometry("300x250")

    tk.Label(fenetre, text="Contenu du commentaire").pack()
    entry_contenu = tk.Entry(fenetre)
    entry_contenu.pack()

    tk.Label(fenetre, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(fenetre)
    entry_auteur.pack()

    tk.Label(fenetre, text="Titre de la publication").pack()
    entry_pub = tk.Entry(fenetre)
    entry_pub.pack()

    def valider():
        contenu = entry_contenu.get()
        auteur_nom = entry_auteur.get()
        titre_pub = entry_pub.get()

        auteur = next((u for u in utilisateurs if u.nom == auteur_nom), None)
        pub = next((p for p in publications if p.titre == titre_pub), None)

        if auteur and pub:
            commentaires.append(Commentaire(contenu, auteur, pub))
            messagebox.showinfo("Succès", "Commentaire ajouté avec succès.")
        else:
            messagebox.showerror("Erreur", "Auteur ou publication introuvable.")
        fenetre.destroy()

    tk.Button(fenetre, text="Ajouter", command=valider).pack(pady=10)

def ouvrir_fenetre_joindre_forum():
    fenetre = tk.Toplevel(root)
    fenetre.title("Joindre un forum")
    fenetre.geometry("300x200")

    tk.Label(fenetre, text="Nom d'utilisateur").pack()
    entry_utilisateur = tk.Entry(fenetre)
    entry_utilisateur.pack()

    tk.Label(fenetre, text="Nom du forum à rejoindre").pack()
    entry_forum = tk.Entry(fenetre)
    entry_forum.pack()

    def valider():
        utilisateur_nom = entry_utilisateur.get()
        forum_nom = entry_forum.get()

        utilisateur = next((u for u in utilisateurs if u.nom == utilisateur_nom), None)
        forum = next((f for f in forums if f.nom == forum_nom), None)

        if utilisateur and forum:
            messagebox.showinfo("Succès", f"{utilisateur.nom} a rejoint le forum {forum.nom}.")
        else:
            messagebox.showerror("Erreur", "Utilisateur ou forum introuvable.")
        fenetre.destroy()

    tk.Button(fenetre, text="Joindre", command=valider).pack(pady=10)

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter PyForum ?"):
        root.destroy()

# Interface principale
root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("400x500")
root.configure(bg="lightblue")

tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

tk.Button(root, text="1. Créer un utilisateur", command=ouvrir_fenetre_utilisateur, width=30).pack(pady=2)
tk.Button(root, text="2. Créer un forum", command=ouvrir_fenetre_forum, width=30).pack(pady=2)
tk.Button(root, text="3. Créer une publication", command=ouvrir_fenetre_publication, width=30).pack(pady=2)
tk.Button(root, text="4. Ajouter un commentaire", command=ouvrir_fenetre_commentaire, width=30).pack(pady=2)
tk.Button(root, text="5. Joindre un forum", command=ouvrir_fenetre_joindre_forum, width=30).pack(pady=2)
tk.Button(root, text="6. Quitter", command=quitter, width=30).pack(pady=20)

root.mainloop()
