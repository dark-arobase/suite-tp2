import tkinter as tk
import random

LARGEUR = 400
HAUTEUR = 300
NB_PV = 5
DUREE_NIVEAU_MS = 15000  # Durée de chaque niveau (en millisecondes)

class JeuUndertale:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=LARGEUR, height=HAUTEUR, bg="black")
        self.canvas.pack()

        self.niveau = 1
        self.pv = NB_PV
        self.vitesse_projectile = 5
        self.frequence_projectile = 1000
        self.projectiles = []
        self.en_jeu = True

        self.joueur = self.canvas.create_oval(190, 140, 210, 160, fill="red")
        self.texte_pv = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 14),
                                                text=f"PV : {self.pv}")
        self.texte_niveau = self.canvas.create_text(10, 30, anchor="nw", fill="white", font=("Arial", 14),
                                                    text=f"Niveau : {self.niveau}")

        self.root.bind("<KeyPress>", self.bouger_joueur)

        self.root.after(1000, self.generer_projectile)
        self.root.after(50, self.mise_a_jour)
        self.root.after(DUREE_NIVEAU_MS, self.passer_au_niveau_suivant)

    def bouger_joueur(self, event):
        dx, dy = 0, 0
        if event.keysym in ("z", "Z", "w", "W"):
            dy = -10
        elif event.keysym in ("s", "S"):
            dy = 10
        elif event.keysym in ("q", "Q", "a", "A"):
            dx = -10
        elif event.keysym in ("d", "D"):
            dx = 10
        self.canvas.move(self.joueur, dx, dy)

    def generer_projectile(self):
        if not self.en_jeu:
            return
        x = random.randint(0, LARGEUR - 10)
        p = self.canvas.create_rectangle(x, 0, x + 10, 10, fill="white")
        self.projectiles.append(p)
        self.root.after(self.frequence_projectile, self.generer_projectile)

    def mise_a_jour(self):
        if not self.en_jeu:
            return

        joueur_coords = self.canvas.coords(self.joueur)

        for p in self.projectiles[:]:
            self.canvas.move(p, 0, self.vitesse_projectile)
            proj_coords = self.canvas.coords(p)

            if self.collision(joueur_coords, proj_coords):
                self.pv -= 1
                self.canvas.itemconfig(self.texte_pv, text=f"PV : {self.pv}")
                self.canvas.delete(p)
                self.projectiles.remove(p)

                if self.pv <= 0:
                    self.fin_du_jeu("Tu as perdu !")
                    return

            elif proj_coords[1] > HAUTEUR:
                self.canvas.delete(p)
                self.projectiles.remove(p)

        self.root.after(50, self.mise_a_jour)

    def collision(self, obj1, obj2):
        return not (
            obj1[2] < obj2[0] or
            obj1[0] > obj2[2] or
            obj1[3] < obj2[1] or
            obj1[1] > obj2[3]
        )

    def passer_au_niveau_suivant(self):
        if not self.en_jeu:
            return
        self.niveau += 1
        self.vitesse_projectile += 1
        self.frequence_projectile = max(300, self.frequence_projectile - 100)
        self.canvas.itemconfig(self.texte_niveau, text=f"Niveau : {self.niveau}")
        self.root.after(DUREE_NIVEAU_MS, self.passer_au_niveau_suivant)

    def fin_du_jeu(self, message):
        self.en_jeu = False
        self.canvas.create_text(LARGEUR // 2, HAUTEUR // 2, fill="red", font=("Arial", 24), text=message)

# Lancer le jeu
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Undertale - Mode Esquive")
    jeu = JeuUndertale(root)
    root.mainloop()
