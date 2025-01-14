print("Les variables de la fonction sont la taille et la masse. Ces variables sont tous les deux des floats.")

print("La fonction doit renvoyer l'IMC de l'individu. Cette valeur sera de type float")

import random

def IMC(m, t):
    imc = m / (t ** 2)
    imcApprox = round(imc, 2)
    return imcApprox

m = 65
t = 1.75
print("L'IMC d'une personne avec une masse de", m , "kg et une taille de", t , "m est de", IMC(m,t) )