import random
def vitesse_moyenne(d, t):
    vitesse = d / t
    vitesseApprox = round(vitesse, 2)
    return vitesseApprox

dK = random.randint(1, 200)
d = dK * 1000
tM = random.randint(1, 1000)
t = tM*60

print("La vitesse moyenne d'un trajet de", dK , "km qui dure ", tM ,"minutes est de", vitesse_moyenne(d, t), "m/s")