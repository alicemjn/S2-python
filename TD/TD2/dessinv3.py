import tkinter as tk
import random as rd

couleur_choisie = "white"  

def choisir_couleur():
    global couleur_choisie
    couleur = input("Tapez une couleur (ex: red, blue, green, yellow, etc.) : ")
    couleur_choisie=couleur
def cercle() :
    rayon=rd.randint(10,400)
    x1=rd.randint(50,1050-rayon*2)
    y1=rd.randint(50,500-rayon*2)
    x2, y2 = x1 + rayon * 2, y1 + rayon * 2
    canva.create_oval(x1, y1, x2, y2, fill=couleur_choisie, outline="black")

def carre() :
    cote=rd.randint(100,400)
    x1=rd.randint(50,1050-cote)
    y1=rd.randint(50, 500-cote)
    x2,y2= x1+cote, y1+cote
    canva.create_rectangle(x1,y1,x2,y2, fill=couleur_choisie, outline="black" )

def croix() :
    taille = rd.randint(20, 100) 
    x_centre = rd.randint(50+taille, 1050 - taille)
    y_centre = rd.randint(50+taille, 500 - taille)
    x1, y1 = x_centre - taille, y_centre - taille  
    x2, y2 = x_centre + taille, y_centre + taille  
    x3, y3 = x_centre - taille, y_centre + taille  
    x4, y4 = x_centre + taille, y_centre - taille 
    canva.create_line(x1, y1, x2, y2, fill=couleur_choisie, width=2)
    canva.create_line(x3, y3, x4, y4, fill=couleur_choisie, width=2) 


racine=tk.Tk()
racine.title("mon dessin")
canva=tk.Canvas(racine,width=1100,height=550,bg="black")
canva.place(x=250,y=100)    

cercle=tk.Button(racine, text="cercle", command=cercle, font = ("helvetica", "30"))
cercle.place(x=50, y=150)
carre=tk.Button(racine, text="carre", command=carre, font=("helvetica", "30"))
carre.place(x=50, y=300)
croix=tk.Button(racine, text="croix", command=croix,font=("helvetica", "30") )
croix.place(x=50, y=450)
choisir_couleur=tk.Button(racine, text="choisis une couleur", command=choisir_couleur,font=("helvetica", "30"))
choisir_couleur.place(x=500, y=10)

racine.mainloop()