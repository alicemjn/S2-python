import tkinter as tk
import random

HEIGHT = 500
WIDTH = 500

root = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.grid()

#pour faire le disque
x=random.randint(10,WIDTH-10)  #car endroit du cercle aléatoire
y=random.randint(10,HEIGHT-10)
create.oval(x-50, y+50, x+50, y-50)

#pour faire le carre
x0=random.randint(10,WIDTH-10)
y0=random.randint(10,HEIGHT-10)
create.carre(#coordonées)

#bouton choix couleur
choixcouleur=tk.Button(root,text="choix couleur",command=choix_couleur) #créer le bouton
def choix_couleur : #créer la fonction associée à la commande
choixcouleur.grid(row=0, column=1) #placer le bouton 

root.mainloop() # Lancement de la boucle principale