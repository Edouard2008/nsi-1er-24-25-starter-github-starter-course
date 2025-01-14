c = 6
P = 4 * c
A = c ** 2
b = A > 5 

print(f"Perimetre du carre: {P}")
print(f" Aire du carre: {A}")
print(f"L'aire est-elle superior a 5? {b}")
x = 5
def perimetre(x):
    P = 4*x
    return P
def surface(x):
    A = x **2
    return A
print("le perimetre est:",perimetre(x))
print("L'air est:", surface(x))
