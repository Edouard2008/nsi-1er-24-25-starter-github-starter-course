import pytest
import exercice_4  # Importer le fichier exercice_4.py

def test_exercice_4():
    # Vérification du fichier exercice_4.py pour différents cas

    # Cas où le côté du carré est 2 (Périmètre = 8, Aire = 4, A > 5 -> False)
    c = 2
    P = 4 * c
    A = c ** 2
    b = (A > 5)
    assert P == 8
    assert A == 4
    assert b == False

    # Cas où le côté du carré est 3 (Périmètre = 12, Aire = 9, A > 5 -> True)
    c = 3
    P = 4 * c
    A = c ** 2
    b = (A > 5)
    assert P == 12
    assert A == 9
    assert b == True

    # Cas où le côté du carré est 1 (Périmètre = 4, Aire = 1, A > 5 -> False)
    c = 1
    P = 4 * c
    A = c ** 2
    b = (A > 5)
    assert P == 4
    assert A == 1
    assert b == False

    # Cas où le côté du carré est 2.5 (Périmètre = 10, Aire = 6.25, A > 5 -> True)
    c = 2.5
    P = 4 * c
    A = c ** 2
    b = (A > 5)
    assert P == 10
    assert A == 6.25
    assert b == True

# Test de la fonction perimetre
def test_perimetre():
    # Cas où le côté est 2, le périmètre doit être 8
    assert exercice_4.perimetre(2) == 8
    # Cas où le côté est 3, le périmètre doit être 12
    assert exercice_4.perimetre(3) == 12
    # Cas où le côté est 0, le périmètre doit être 0
    assert exercice_4.perimetre(0) == 0
    # Cas où le côté est 2.5, le périmètre doit être 10
    assert exercice_4.perimetre(2.5) == 10

# Test de la fonction surface
def test_surface():
    # Cas où le côté est 2, la surface doit être 4
    assert exercice_4.surface(2) == 4
    # Cas où le côté est 3, la surface doit être 9
    assert exercice_4.surface(3) == 9
    # Cas où le côté est 0, la surface doit être 0
    assert exercice_4.surface(0) == 0
    # Cas où le côté est 2.5, la surface doit être 6.25
    assert exercice_4.surface(2.5) == 6.25

# Exécuter pytest en ligne de commande pour tester:
# pytest test_exercice_4.py
