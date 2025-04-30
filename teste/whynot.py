import tkinter as tk
from tkinter import messagebox
from bd import BD  # Assure-toi que le fichier bd.py est dans le même dossier

bd = BD()

# Fonction pour ouvrir une fenêtre pour la création d'un utilisateur
def ouvrir_fenetre_utilisateur():
    f = tk.Toplevel(root)
    f.title("Créer un utilisateur")
    f.geometry("300x250")

    tk.Label(f, text="Nom d'utilisateur").pack()
    entry_nom = tk.Entry(f)
    entry_nom.pack()

    tk.Label(f, text="Courriel").pack()
    entry_mail = tk.Entry(f)
    entry_mail.pack()

    tk.Label(f, text="Mot de passe").pack()
    entry_mdp = tk.Entry(f, show="*")
    entry_mdp.pack()

    def valider():
        nom = entry_nom.get()
        mail = entry_mail.get()
        mdp = entry_mdp.get()
        bd.creer_utilisateur(nom, mail, mdp)
        messagebox.showinfo("Succès", "Utilisateur créé avec succès.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

# Fonction pour ouvrir une fenêtre pour la création d'un forum
def ouvrir_fenetre_forum():
    f = tk.Toplevel(root)
    f.title("Créer un forum")
    f.geometry("300x200")

    tk.Label(f, text="Nom du forum").pack()
    entry_nom = tk.Entry(f)
    entry_nom.pack()

    tk.Label(f, text="Description").pack()
    entry_desc = tk.Entry(f)
    entry_desc.pack()

    def valider():
        nom = entry_nom.get()
        desc = entry_desc.get()
        bd.creer_forum(nom, desc)
        messagebox.showinfo("Succès", "Forum créé avec succès.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

# Fonction pour ouvrir une fenêtre pour la création d'une publication
def ouvrir_fenetre_publication():
    f = tk.Toplevel(root)
    f.title("Créer une publication")
    f.geometry("300x300")

    tk.Label(f, text="Titre de la publication").pack()
    entry_titre = tk.Entry(f)
    entry_titre.pack()

    tk.Label(f, text="Contenu de la publication").pack()
    entry_contenu = tk.Entry(f)
    entry_contenu.pack()

    tk.Label(f, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(f)
    entry_auteur.pack()

    tk.Label(f, text="Forum de la publication").pack()
    entry_forum = tk.Entry(f)
    entry_forum.pack()

    def valider():
        titre = entry_titre.get()
        contenu = entry_contenu.get()
        auteur = entry_auteur.get()
        forum = entry_forum.get()
        u = bd.obtenir_utilisateur_par_nom(auteur)
        f = bd.obtenir_forum_par_nom(forum)
        if u and f:
            bd.creer_publication(titre, contenu, u.id, f.id)
            messagebox.showinfo("Succès", "Publication créée avec succès.")
        else:
            messagebox.showerror("Erreur", "Auteur ou forum introuvable.")
        f.destroy()

    tk.Button(f, text="Créer", command=valider).pack(pady=10)

# Fonction pour ouvrir une fenêtre pour ajouter un commentaire à une publication
def ouvrir_fenetre_commentaire():
    f = tk.Toplevel(root)
    f.title("Ajouter un commentaire")
    f.geometry("300x250")

    tk.Label(f, text="Contenu du commentaire").pack()
    entry_contenu = tk.Entry(f)
    entry_contenu.pack()

    tk.Label(f, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(f)
    entry_auteur.pack()

    tk.Label(f, text="Titre de la publication").pack()
    entry_pub = tk.Entry(f)
    entry_pub.pack()

    def valider():
        contenu = entry_contenu.get()
        auteur = entry_auteur.get()
        titre_pub = entry_pub.get()
        u = bd.obtenir_utilisateur_par_nom(auteur)
        p = next((p for p in bd.publications if p.titre == titre_pub), None)
        if u and p:
            bd.creer_commentaire(contenu, u.id, p.id)
            messagebox.showinfo("Succès", "Commentaire ajouté avec succès.")
        else:
            messagebox.showerror("Erreur", "Auteur ou publication introuvable.")
        f.destroy()

    tk.Button(f, text="Ajouter", command=valider).pack(pady=10)

# Fonction pour ouvrir une fenêtre pour rejoindre un forum
def ouvrir_fenetre_joindre_forum():
    f = tk.Toplevel(root)
    f.title("Joindre un forum")
    f.geometry("300x200")

    tk.Label(f, text="Nom d'utilisateur").pack()
    entry_utilisateur = tk.Entry(f)
    entry_utilisateur.pack()

    tk.Label(f, text="Nom du forum à rejoindre").pack()
    entry_forum = tk.Entry(f)
    entry_forum.pack()

    def valider():
        utilisateur = entry_utilisateur.get()
        forum = entry_forum.get()
        bd.joindre_forum(utilisateur, forum)
        messagebox.showinfo("Succès", f"L'utilisateur {utilisateur} a rejoint le forum {forum}.")
        f.destroy()

    tk.Button(f, text="Joindre", command=valider).pack(pady=10)

# Fonction pour quitter l'application
def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter PyForum ?"):
        root.destroy()

# Fenêtre principale
root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("400x500")
root.configure(bg="lightblue")

tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

# Boutons du menu
tk.Button(root, text="1. Créer un utilisateur", command=ouvrir_fenetre_utilisateur, width=30).pack(pady=2)
tk.Button(root, text="2. Créer un forum", command=ouvrir_fenetre_forum, width=30).pack(pady=2)
tk.Button(root, text="3. Créer une publication", command=ouvrir_fenetre_publication, width=30).pack(pady=2)
tk.Button(root, text="4. Ajouter un commentaire", command=ouvrir_fenetre_commentaire, width=30).pack(pady=2)
tk.Button(root, text="5. Joindre un forum", command=ouvrir_fenetre_joindre_forum, width=30).pack(pady=2)
tk.Button(root, text="6. Quitter", command=quitter, width=30).pack(pady=20)

root.mainloop()
