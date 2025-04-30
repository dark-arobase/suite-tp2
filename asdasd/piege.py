# piege.py
import tkinter as tk
from tkinter import messagebox

def refuser_de_partir():
    messagebox.showwarning("Trop tard 😈", "Tu ne peux pas fermer cette fenêtre si facilement !")

root = tk.Tk()
root.title("Piège activé")
root.geometry("300x200")
tk.Label(root, text="Trop tard, le piège est lancé 😈", font=("Arial", 12)).pack(pady=20)
tk.Button(root, text="Essaye de quitter", command=refuser_de_partir).pack()

# Interdit la fermeture par la croix rouge
root.protocol("WM_DELETE_WINDOW", refuser_de_partir)

root.mainloop()
