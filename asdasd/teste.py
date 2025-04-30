import tkinter as tk
import os


def quitter_et_lancer_piege():
    os.system('"C:/Program Files/Python312/python.exe" asdasd/piege.py')  # <-- corrige le chemin si nécessaire
    root.destroy()

def mettre_a_jour_resultats(event=None):
    resultats.config(state='normal')
    resultats.delete("1.0", tk.END)
    resultats.insert(tk.END, f"Nom : {champ_nom.get()}\n")
    resultats.insert(tk.END, f"Commentaires : {zone_texte.get('1.0', tk.END).strip()}\n")
    selection = liste.curselection()
    if selection:
        resultats.insert(tk.END, f"Élément sélectionné : {liste.get(selection)}\n")
    else:
        resultats.insert(tk.END, "Élément sélectionné : Aucun\n")
    resultats.config(state='disabled')

root = tk.Tk()
root.title("PyForum - Menu Principal")
root.geometry("600x600")
root.configure(bg="white")

tk.Label(root, text="Bienvenue sur PyForum", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="---- Menu ----", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Choisissez une option :", font=("Arial", 16)).pack(pady=10)

# Remplace l'Entry mal utilisé par un Label multi-lignes
instructions = (
    "1. Créer un utilisateur\n2. Créer un forum\n3. Créer une publication\n"
    "4. Ajouter un commentaire à une publication\n5. Joindre un forum\n6. Quitter\n"
    "7. Va te faire un café ?\n8. Voulez-vous faire un commentaire"
)
tk.Label(root, text=instructions, font=("Arial", 12), bg="white", justify=tk.LEFT).pack(pady=5)

# Champ de saisie pour le nom d'utilisateur
tk.Label(root, text="Nom :", bg="white").pack()
champ_nom = tk.Entry(root)
champ_nom.pack()
champ_nom.bind("<KeyRelease>", mettre_a_jour_resultats)

# Champ commentaire
tk.Label(root, text="Commentaires :", bg="white").pack()
zone_texte = tk.Text(root, height=5, width=30)
zone_texte.pack()
zone_texte.bind("<KeyRelease>", mettre_a_jour_resultats)

# Listbox
tk.Label(root, text="Choisissez un élément :", bg="white").pack()
liste = tk.Listbox(root, height=4)
for item in ["Élément 1", "Élément 2", "Élément 3", "Élément 4"]:
    liste.insert(tk.END, item)
liste.pack()
liste.bind("<<ListboxSelect>>", mettre_a_jour_resultats)

# Zone de texte pour afficher les résultats
tk.Label(root, text="Résultat :", bg="white").pack(pady=5)
resultats = tk.Text(root, height=10, width=50, state='disabled')
resultats.pack()

# Bouton quitter
tk.Button(root, text="Quitter", command=quitter_et_lancer_piege).pack(pady=20)

root.mainloop()
