import random
import math
print("1. La formule pour calculer le perimetre d'une cercle est: 2πr ")

print("2. L'argument est le rayon du cercle. Cet serait de type float")

a = random.randint(1, 10)
pi = (math.pi)
def perimetre_cercle(a):
    perimetre = 2 * pi * a
    perimetreApprox = round(perimetre, 2)
    return perimetreApprox
print("Le perimetre du cercle de rayon", a , "est de environ ", perimetre_cercle(a))