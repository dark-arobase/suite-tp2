import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("400x500")
root.configure(bg="lightblue")

def ouvrir_fenetre_utilisateur():
    fenetre = tk.Toplevel(root)
    
    def valider():
        print("0")
        fenetre.destroy()
    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_forum():
    fenetre = tk.Toplevel(root)
    
    def valider():
        print("0")
        fenetre.destroy()
    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_publication():
    fenetre = tk.Toplevel(root)
    
    def valider():
        print("0")
        fenetre.destroy()
    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_commentaire():
    fenetre = tk.Toplevel(root)
    
    def valider():
        print("0")
        fenetre.destroy()
    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def ouvrir_fenetre_joindre_forum():
    
    fenetre = tk.Toplevel(root)
    def valider():
        print("0")
        fenetre.destroy()
    tk.Button(fenetre, text="Créer", command=valider).pack(pady=10)

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter PyForum ?"):
        root.destroy()


tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

tk.Button(root, text="1. Créer un utilisateur", command=ouvrir_fenetre_utilisateur, width=30).pack(pady=2)
tk.Button(root, text="2. Créer un forum", command=ouvrir_fenetre_forum, width=30).pack(pady=2)
tk.Button(root, text="3. Créer une publication", command=ouvrir_fenetre_publication, width=30).pack(pady=2)
tk.Button(root, text="4. Ajouter un commentaire", command=ouvrir_fenetre_commentaire, width=30).pack(pady=2)
tk.Button(root, text="5. Joindre un forum", command=ouvrir_fenetre_joindre_forum, width=30).pack(pady=2)
tk.Button(root, text="6. Quitter", command=quitter, width=30).pack(pady=20)

root.mainloop()