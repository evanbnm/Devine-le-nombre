"""
devine_le_nombre_gui.py
------------------------
Jeu "Devine le nombre" avec interface graphique Tkinter.

Auteur : Evan
Date : 2024-12-13
"""

import tkinter as tk
from tkinter import messagebox
import random

class DevineLeNombre:
    """
    Classe pour gérer le jeu "Devine le nombre" avec une interface graphique Tkinter.
    """
    def __init__(self, fenetre):
        """
        Initialise l'interface graphique et le jeu.
        
        :param fenetre: Fenêtre Tkinter principale.
        """
        self.fenetre = fenetre
        self.fenetre.title("Devine le nombre")
        
        # Initialiser le nombre secret et les essais
        self.nombre_secret = random.randint(1, 100)
        self.essais = 0

        # Créer les widgets
        self.label_instruction = tk.Label(fenetre, text="Devinez le nombre entre 1 et 100")
        self.label_instruction.pack()

        self.entree_nombre = tk.Entry(fenetre)
        self.entree_nombre.pack()

        self.bouton_valider = tk.Button(fenetre, text="Valider", command=self.verifier)
        self.bouton_valider.pack()

        self.label_essais = tk.Label(fenetre, text="Essais : 0")
        self.label_essais.pack()

    def verifier(self):
        """
        Vérifie la proposition du joueur et donne un indice.
        """
        try:
            # Récupérer la proposition du joueur
            guess = int(self.entree_nombre.get())
            self.essais += 1
            self.label_essais.config(text=f"Essais : {self.essais}")
            
            # Vérifier la proposition
            if guess < self.nombre_secret:
                messagebox.showinfo("Indice", "C'est plus grand !")
            elif guess > self.nombre_secret:
                messagebox.showinfo("Indice", "C'est plus petit !")
            else:
                messagebox.showinfo("Bravo !", f"Félicitations, vous avez deviné le nombre en {self.essais} essais !")
                self.reinitialiser_jeu()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    def reinitialiser_jeu(self):
        """
        Réinitialise le jeu après une victoire.
        """
        self.nombre_secret = random.randint(1, 100)
        self.essais = 0
        self.label_essais.config(text="Essais : 0")
        self.entree_nombre.delete(0, tk.END)

def main():
    """
    Fonction principale pour démarrer le jeu.
    """
    fenetre = tk.Tk()
    jeu = DevineLeNombre(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":
    main()