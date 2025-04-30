import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Exemples de widgets")

# Label
tk.Label(fenetre, text="Nom :").pack()

# Entry
champ_nom = tk.Entry(fenetre)
champ_nom.pack()

# Checkbutton
accepter_var = tk.BooleanVar()
accepter = tk.Checkbutton(fenetre,
                          text="Cocher ou ne pas cocher, telle est la question",
                          variable=accepter_var)
accepter.pack()

# Boutons radio
tk.Label(fenetre, text="Choisissez une option :").pack()
option = tk.StringVar(value="A")
tk.Radiobutton(fenetre, text="Option A", variable=option, value="A").pack()
tk.Radiobutton(fenetre, text="Option B", variable=option, value="B").pack()

# Text
tk.Label(fenetre, text="Commentaires :").pack()
zone_texte = tk.Text(fenetre, height=5, width=30)
zone_texte.pack()

# Listbox
tk.Label(fenetre, text="Choisissez un élément :").pack()
liste = tk.Listbox(fenetre, height=4)
for item in ["Élément 1", "Élément 2", "Élément 3", "Élément 4"]:
    liste.insert(tk.END, item)
liste.pack()

# Scale
tk.Label(fenetre, text="Bouger le curseur :").pack()
curseur = tk.Scale(fenetre, from_=0, to=10, orient=tk.HORIZONTAL)
curseur.pack()

# Spinbox
tk.Label(fenetre, text="Cliquer sur les flèches :").pack()
spinbox = tk.Spinbox(fenetre, from_=0, to=10)
spinbox.pack()

# Button
def valider():
    resultats.delete("1.0", tk.END)  # Efface le contenu précédent
    resultats.insert(tk.END, f"Nom : {champ_nom.get()}\n")
    resultats.insert(tk.END, f"Coché ou pas : {accepter_var.get()}\n")
    resultats.insert(tk.END, f"Option choisie : {option.get()}\n")
    resultats.insert(tk.END, f"Commentaires : {zone_texte.get('1.0', tk.END).strip()}\n")
    resultats.insert(tk.END, f"Élément sélectionné : {liste.get(tk.ACTIVE)}\n")
    resultats.insert(tk.END, f"Valeur du curseur : {curseur.get()}\n")
    resultats.insert(tk.END, f"Valeur du spinbox : {spinbox.get()}\n")

tk.Button(fenetre, text="Valider", command=valider).pack()

# Zone de texte pour afficher les résultats
resultats = tk.Text(fenetre, height=10, width=50)
resultats.pack()

fenetre.mainloop()