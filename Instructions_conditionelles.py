#   Exercice 1:

#          Début
#            |
#     +--- Saisir la taille ---+
#            |
#       Taille > 150 ?
#       /          \
#     Oui           Non
#     /               \
#Afficher          Afficher
#"Vous pouvez    "Vous êtes trop
# entrer..."      petits..."
#            |
#           Fin

### Fonctionnement de l'algorithme :

#L'algorithme permet de déterminer si une personne peut entrer ou non en fonction de sa taille. Il effectue les actions suivantes :

#1. **Prend une valeur de taille (en centimètres).**
#2. **Compare cette valeur à 150 cm :**
#   - Si la taille est **supérieure à 150 cm**, l'algorithme renvoie le message : **"Vous pouvez entrer, ne vomissez pas svp."**
#   - Si la taille est **inférieure ou égale à 150 cm**, l'algorithme renvoie le message : **"Vous êtes trop petits, allez manger de la soupe."**

### Exemples de valeurs de la variable `taille` :

#1. **Taille = 160 cm** :
#   - La taille est **supérieure à 150 cm**, donc l'algorithme renverra : **"Vous pouvez entrer, ne vomissez pas svp."**

#2. **Taille = 150 cm** :
#   - La taille est **égale à 150 cm**, donc l'algorithme renverra : **"Vous êtes trop petits, allez manger de la soupe."**

#3. **Taille = 140 cm** :
#   - La taille est **inférieure à 150 cm**, donc l'algorithme renverra : **"Vous êtes trop petits, allez manger de la soupe."**

### Résumé des issues :
#- Si la taille est strictement **supérieure à 150 cm**, l'algorithme renvoie le message d'entrée.
#- Si la taille est **inférieure ou égale à 150 cm**, l'algorithme renvoie le message d'exclusion.

#   Exercice 2:

#                Début
#                  |
#              Jeter le dé
#                  |
#        +---- dé ≤ 2 ? ----+
#        |                  |
#       Oui                Non
#        |                  |
#Diviser votre_santé   3 ≤ dé ≤ 8 ?
#    par 2             /         \
#        |           Oui         Non
#        |            |           |
#      Fin     santé_adversaire  santé_adversaire
#                   ←               ← 0
#         Fin    santé_adversaire - puissance_attaque
#                           |
#                          Fin


#   Exercice 3:

#Pour chacune des valeurs de la variable **dé** (8, 10, et 2), l'algorithme effectue différentes actions. Utilisons les valeurs initiales suivantes : 

#- **votre_santé = 100**
#- **santé_adversaire = 200**
#- **puissance_attaque = 120**

#Analysons les résultats de l'algorithme **Attaque** pour chaque valeur de **dé**.

### 1. **dé = 8** :

#**Étape 1 :** On jette le dé et il donne 8.

#**Étape 2 :** L'algorithme vérifie si **dé ≤ 2**.
#- Ici, **8 > 2**, donc on passe à l'étape suivante.

#**Étape 3 :** L'algorithme vérifie si **3 ≤ dé ≤ 8**.
#- Ici, **8 est compris entre 3 et 8**, donc on exécute cette condition :  
#  **santé_adversaire ← santé_adversaire - puissance_attaque**

#**Calcul :**  
#  **santé_adversaire = 200 - 120 = 80**

#**Résultat final :**  
#  - **votre_santé = 100** (inchangée)  
#  - **santé_adversaire = 80**

### 2. **dé = 10** :

#**Étape 1 :** On jette le dé et il donne 10.

#**Étape 2 :** L'algorithme vérifie si **dé ≤ 2**.
#- Ici, **10 > 2**, donc on passe à l'étape suivante.

#**Étape 3 :** L'algorithme vérifie si **3 ≤ dé ≤ 8**.
#- Ici, **10 > 8**, donc on passe à l'étape suivante.

#**Étape 4 :** La condition restante est celle du **sinon** (dé > 8), donc l'algorithme exécute :  
#  **santé_adversaire ← 0**

#**Résultat final :**  
#  - **votre_santé = 100** (inchangée)  
#  - **santé_adversaire = 0** (adversaire vaincu)

### 3. **dé = 2** :

#**Étape 1 :** On jette le dé et il donne 2.

#**Étape 2 :** L'algorithme vérifie si **dé ≤ 2**.
#- Ici, **2 ≤ 2**, donc on exécute cette condition :  
#  **votre_santé ← votre_santé / 2**

#**Calcul :**  
#  **votre_santé = 100 / 2 = 50**

#**Résultat final :**  
#  - **votre_santé = 50**  
#  - **santé_adversaire = 200** (inchangée)

### Récapitulatif des résultats pour chaque valeur de dé :

#1. **dé = 8** :  
#   - **votre_santé = 100**  
#   - **santé_adversaire = 80**

#2. **dé = 10** :  
#   - **votre_santé = 100**  
#   - **santé_adversaire = 0**

#3. **dé = 2** :  
#   - **votre_santé = 50**  
#   - **santé_adversaire = 200**

#   Exercice 4:

#Si pokemon_choisi = Bulbizarre :
#    pokemon_rival ← Carapuce
#Sinon Si pokemon_choisi = Carapuce :
#    pokemon_rival ← Salamèche
#Sinon Si pokemon_choisi = Salamèche :
#    pokemon_rival ← Bulbizarre
#Sinon :
#    Afficher "Pokémon non valide"

#Exercice 4:

#L'utilisation de == pour les comparaisons et de = pour les affectations permet de garder le code explicite et de minimiser les erreurs.

#Exercice 5:

#                Début
#                  |
#   Saisir identifiant et authentifiant
#                  |
#  +--- identifiant ≠ "dark.vador@empire.gouv" ? ---+
#  |                  |                            |
# Oui                Non                           |
#  |                  |                       +--- authentifiant ≠ "*c0t3Ob$cUr*" ? ---+
# Afficher       Passer à l'étape suivante     |                 |
#"Erreur :      Vérifier l'authentifiant       Oui               Non
# identifiant        |                          |                 |
# erroné."       |                           Afficher       Afficher
#               |                       "Erreur : mot de "Que la Force
#               |                      passe erroné."   soit avec vous
#               |                                       Seigneur Vador."
#               |                                            |
#              Fin                                           Fin

#L'algorithme vérifie si les informations d'identification (l'identifiant et l'authentifiant ou mot de passe) sont correctes pour accorder l'accès. Voici ce qu'il fait :

#Vérification de l'identifiant :
#Si l'identifiant est différent de "dark.vador@empire.gouv", l'algorithme renvoie : "Erreur : identifiant erroné."
#Si l'identifiant est correct mais que l'authentifiant est différent de "*c0t3Ob$cUr*", l'algorithme renvoie : "Erreur : mot de passe erroné."
#Vérification de l'authentifiant :
#Succès :
#Si les deux informations sont correctes (l'identifiant et l'authentifiant), l'algorithme renvoie : "Que la Force soit avec vous Seigneur Vador."
#Exemples de couples de valeurs (identifiant et authentifiant) :
#Identifiant incorrect :
#identifiant : "anakin.skywalker@empire.gouv"
#authentifiant : "*c0t3Ob$cUr*"
#Résultat : "Erreur : identifiant erroné."
#L'identifiant est incorrect, même si l'authentifiant est bon. L'algorithme renvoie une erreur liée à l'identifiant.
#Authentifiant incorrect :
#identifiant : "dark.vador@empire.gouv"
#authentifiant : "motDePasseInvalide"
#Résultat : "Erreur : mot de passe erroné."
#L'identifiant est correct, mais l'authentifiant est erroné. L'algorithme renvoie une erreur liée au mot de passe.
#Identifiant et authentifiant corrects :
#identifiant : "dark.vador@empire.gouv"
#authentifiant : "*c0t3Ob$cUr*"
#Résultat : "Que la Force soit avec vous Seigneur Vador."
#Les deux informations sont correctes, donc l'algorithme renvoie le message de succès.

#Exercice 6:

def attaque(dé, votre_santé, santé_adversaire, puissance_attaque):
    if dé <= 2:
        votre_santé = votre_santé / 2
    elif 3 <= dé <= 8:
        santé_adversaire = santé_adversaire - puissance_attaque
    else:
        santé_adversaire = 0
    return votre_santé, santé_adversaire

#   Exercice 7:

def puissance_finale_subie(puissance_initiale, type_attaque):
    if type_attaque in ["Acier", "Électrique", "Vol"]:
        return puissance_initiale / 2
    elif type_attaque == "Sol":
        return puissance_initiale * 2
    else:
        return puissance_initiale

#   Exercice 8:

def puissance_ball_ombre(type_adversaire):
    puissance_initiale = 80
    if type_adversaire in ["Psy", "Spectre"]:
        return puissance_initiale * 2
    elif type_adversaire == "Ténèbres":
        return puissance_initiale * 0.5
    elif type_adversaire == "Normal":
        return 0
    else:
        return puissance_initiale

#   Exercice 9:

#Début
#    Si dé < 2 :
#        PV ← PV / 2
#    Sinon Si dé < 9 :
#        PVA ← PVA - P
#    Sinon :
#        PVA ← 0
#Fin

# dé = 8 :
#Étape 1 : On jette le dé et il donne 8.

#Étape 2 : Vérification des conditions :

#dé < 2 : 8 n'est pas inférieur à 2 → On passe à l'étape suivante.
#Étape 3 : Vérification de la deuxième condition :

#dé < 9 : 8 est inférieur à 9 → Exécuter cette condition.
#Calcul :

#PVA = PVA - P
#PVA = 150 - 120 = 30
#Résultat final :

#PV = 100 (inchangée)
#PVA = 30
#2. dé = 10 :
#Étape 1 : On jette le dé et il donne 10.

#Étape 2 : Vérification des conditions :

#dé < 2 : 10 n'est pas inférieur à 2 → On passe à l'étape suivante.
#Étape 3 : Vérification de la deuxième condition :

#dé < 9 : 10 n'est pas inférieur à 9 → On passe à l'étape suivante.
#Étape 4 : Exécuter la condition Sinon :

#PVA = 0 (points de vie de l'adversaire réduits à 0)
#Résultat final :

#PV = 100 (inchangée)
#PVA = 0 (adversaire vaincu)
#3. dé = 2 :
#Étape 1 : On jette le dé et il donne 2.

#Étape 2 : Vérification des conditions :

#dé < 2 : 2 n'est pas inférieur à 2 → On passe à l'étape suivante.
#Étape 3 : Vérification de la deuxième condition :

#dé < 9 : 2 est inférieur à 9 → Exécuter cette condition.
#Calcul :

#PVA = PVA - P
#PVA = 150 - 120 = 30
#Résultat final :

#PV = 100 (inchangée)
#PVA = 30

#   Exercice 10:

#   Début
#    Saisir pokemon_choisi

#    Si pokemon_choisi = Germignon :
#        pokemon_rival ← Héricendre
#    Sinon Si pokemon_choisi = Héricendre :
#        pokemon_rival ← Kaiminus
#    Sinon Si pokemon_choisi = Kaiminus :
#        pokemon_rival ← Germignon
#    Sinon :
#        Afficher "Pokémon non valide"
    
#    Afficher "Le Pokémon choisi par le rival est :", pokemon_rival
#Fin

#   Exercice 11:

def starter(pokemon_choisi):
    if pokemon_choisi == "Bulbizarre":
        pokemon_rival = "Carapuce"
    elif pokemon_choisi == "Carapuce":
        pokemon_rival = "Salamèche"
    else:
        pokemon_rival = "Bulbizarre"
    return pokemon_rival