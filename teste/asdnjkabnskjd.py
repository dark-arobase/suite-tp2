import tkinter as tk
from tkinter import messagebox
from bd import BD  # Assure-toi que bd.py est dans le même dossier

bd = BD()

# Fonction : Créer un utilisateur
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
        nom = entry_nom.get().strip()
        mail = entry_mail.get().strip()
        mdp = entry_mdp.get().strip()
        if not nom or not mail or not mdp:
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
            return
        bd.creer_utilisateur(nom, mail, mdp)
        messagebox.showinfo("Succès", "Utilisateur créé avec succès.")
        fenetre.destroy()

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

# Fonction : Créer un forum
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
        nom = entry_nom.get().strip()
        desc = entry_desc.get().strip()
        if not nom:
            messagebox.showerror("Erreur", "Le nom du forum est requis.")
            return
        bd.creer_forum(nom, desc)
        messagebox.showinfo("Succès", "Forum créé avec succès.")
        fenetre.destroy()

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

# Fonction : Créer une publication
def ouvrir_fenetre_publication():
    fenetre = tk.Toplevel(root)
    fenetre.title("Créer une publication")
    fenetre.geometry("300x350")

    tk.Label(fenetre, text="Titre de la publication").pack()
    entry_titre = tk.Entry(fenetre)
    entry_titre.pack()

    tk.Label(fenetre, text="Contenu").pack()
    text_contenu = tk.Text(fenetre, height=5, width=30)
    text_contenu.pack()

    tk.Label(fenetre, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(fenetre)
    entry_auteur.pack()

    tk.Label(fenetre, text="Forum").pack()
    entry_forum = tk.Entry(fenetre)
    entry_forum.pack()

    def valider():
        titre = entry_titre.get().strip()
        contenu = text_contenu.get("1.0", tk.END).strip()
        auteur = entry_auteur.get().strip()
        forum = entry_forum.get().strip()
        if not titre or not contenu or not auteur or not forum:
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
            return
        u = bd.obtenir_utilisateur_par_nom(auteur)
        f = bd.obtenir_forum_par_nom(forum)
        if u and f:
            bd.creer_publication(titre, contenu, u.id, f.id)
            messagebox.showinfo("Succès", "Publication créée avec succès.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Auteur ou forum introuvable.")

    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

# Fonction : Ajouter un commentaire
def ouvrir_fenetre_commentaire():
    fenetre = tk.Toplevel(root)
    fenetre.title("Ajouter un commentaire")
    fenetre.geometry("300x300")

    tk.Label(fenetre, text="Contenu du commentaire").pack()
    text_contenu = tk.Text(fenetre, height=4, width=30)
    text_contenu.pack()

    tk.Label(fenetre, text="Nom de l'auteur").pack()
    entry_auteur = tk.Entry(fenetre)
    entry_auteur.pack()

    tk.Label(fenetre, text="Titre de la publication").pack()
    entry_pub = tk.Entry(fenetre)
    entry_pub.pack()

    def valider():
        contenu = text_contenu.get("1.0", tk.END).strip()
        auteur = entry_auteur.get().strip()
        titre_pub = entry_pub.get().strip()
        if not contenu or not auteur or not titre_pub:
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
            return
        u = bd.obtenir_utilisateur_par_nom(auteur)
        p = next((pub for pub in bd.publications if pub.titre == titre_pub), None)
        if u and p:
            bd.creer_commentaire(contenu, u.id, p.id)
            messagebox.showinfo("Succès", "Commentaire ajouté avec succès.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Auteur ou publication introuvable.")

    tk.Button(fenetre, text="Ajouter", command=valider).pack(pady=10)

# Fonction : Joindre un forum
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
        utilisateur = entry_utilisateur.get().strip()
        forum = entry_forum.get().strip()
        u = bd.obtenir_utilisateur_par_nom(utilisateur)
        f = bd.obtenir_forum_par_nom(forum)
        if u and f:
            bd.joindre_forum(utilisateur, forum)
            messagebox.showinfo("Succès", f"{utilisateur} a rejoint le forum {forum}.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Utilisateur ou forum introuvable.")

    tk.Button(fenetre, text="Joindre", command=valider).pack(pady=10)

# Quitter l'application
def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter PyForum ?"):
        root.destroy()

# Fenêtre principale
root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("400x500")
root.configure(bg="lightblue")

tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

# Boutons de menu
tk.Button(root, text="1. Créer un utilisateur", command=ouvrir_fenetre_utilisateur, width=30).pack(pady=2)
tk.Button(root, text="2. Créer un forum", command=ouvrir_fenetre_forum, width=30).pack(pady=2)
tk.Button(root, text="3. Créer une publication", command=ouvrir_fenetre_publication, width=30).pack(pady=2)
tk.Button(root, text="4. Ajouter un commentaire", command=ouvrir_fenetre_commentaire, width=30).pack(pady=2)
tk.Button(root, text="5. Joindre un forum", command=ouvrir_fenetre_joindre_forum, width=30).pack(pady=2)
tk.Button(root, text="6. Quitter", command=quitter, width=30).pack(pady=20)

root.mainloop()
