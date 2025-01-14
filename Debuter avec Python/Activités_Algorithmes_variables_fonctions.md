## Attendus et savoir-faire

- Identifier une variable et son type.
- Affecter une valeur à une variable, en pseudo-code et en Python. Modifier cette valeur.
- Identifier une fonction, en pseudo-code et en Python, ses arguments, ses éventuels renvois. L'appeler.
- Écrire, compléter, modifier un algorithme faisant intervenir des variables et des fonctions.

## Exercices

**Exercice 1**  
Pourquoi les algorithmes sont-ils écrits sous forme de pseudo-code et non directement dans un langage de programmation ?

**Exercice 2 [Pokédex]**  
1. Si l'on devait programmer un pokédex, quelles seraient les informations à enregistrer pour chaque pokémon ?
2. Comment nommer les variables pour les stocker et quels seraient leurs types ?
3. Donner un exemple d'affectation en pseudo-code et en langage de programmation pour chacune de ces variables.

**Exercice 3**  
Vous programmez un logiciel médical dans lequel un médecin pourra enregistrer des informations sur ses patients. Les médecins souhaitent pouvoir enregistrer trois types d'informations :

- d'identité ;
- de contact ;
- médicales.

1. Pour chacune de ces catégories, quelles sont les informations essentielles à avoir ?
2. Comment nommer les variables pour les stocker et quels seront leurs types ?
3. Donner un exemple d'affectation en pseudo-code et en langage de programmation pour chacune de ces variables.

**Exercice 4**  
On considère l'algorithme suivant :  

$$
\begin{array}{l}
\text{Algorithme 2} \\
c \gets \text{côté du carré} \\
P \gets 4 \times c \\
A \gets c^2 \\
b \gets (A > 5)
\end{array}
$$

1. Combien de variables y a-t-il ? Quelles sont elles, et quels sont leurs types ?
2. Donner le logigramme associé à cet algorithme.
3. On affecte $2$ à la variable $c$. Quelles sont alors les valeurs des variables $P$, $A$ et $b$ ?
4. À quoi correspondent les variables $P$, $A$ et $b$ ?
5. Que penser du nom de ces variables ?
5. Proposer le code en Python de cet Algorithme dans un fichier au nom `exercice_4.py` que vous placerez dans ce dossier `Debuter avec Python`
6. Proposer une fonction perimetre qui calcul le perimetre d'un carre `perimetre(x)` dans le meme fichier `exercice_4.py`
7. Proposer une fonction surface qui calcul la surface d'un carre `surface(x)` dans le meme fichier `exercice_4.py`

**Exercice 5 [Cercle]**  
L'algorithme incomplet suivant donne une fonction permettant de calculer le périmètre d'un cercle.

$$
\begin{array}{l}
\text{Algorithme 3} \\
\textbf{perimetre-cercle}(\text{...}) \\
\text{perimetre} \gets \text{...} \\
\text{return ...}
\end{array}
$$

1. Quelle est la formule permettant de calculer le périmètre d'un cercle ?
2. Quel argument doit prendre en entrée la fonction **périmètre_cercle** ? Quel serait le type de cet argument ?
3. Compléter l'algorithme de la fonction ci-dessus afin qu'elle renvoie le périmètre d'un cercle.

**Exercice 6 [Boîte de conserve]**  
On veut écrire deux fonctions permettant le calcul du volume et le calcul de la surface d'une boîte de conserve cylindrique de rayon $r$ et de hauteur $h$.

1. Quelles sont les formules permettant de calculer ce volume et cette aire ?
2. Quelles sont les variables que l'on va utiliser ? Quels sont leurs types ?
3. Écrire les fonctions effectuant ces calculs.

**Exercice 7 [IMC]**  
On souhaite écrire une fonction permettant de calculer l'indice de masse corporelle (IMC) d'un individu. Cet indice se calcule avec :  
$$\text{IMC} = \dfrac{\text{masse}}{ \text{taille}^2} \text{ (en kg/m}^2\text{)}.$$

1. Quelles sont les variables que la fonction doit prendre en entrée ? Quels sont leurs types ?
2. La fonction doit-elle renvoyer quelque chose ? Si oui, de quel type ?
3. Compléter la fonction `IMC` écrite en Python ci-dessous.

```python
def IMC(...):
    ...
    return ...
```

*Indication :* en Python, la puissance s'écrit à l'aide de `**`, par exemple $x^2$ s'écrit `x**2`.

4. Écrire un appel de cette fonction pour une taille de 1,75 m et un poids de 65 kg.

**Exercice 8 [Vitesse moyenne]**  
Écrire une fonction en Python renvoyant une vitesse moyenne à partir d'un temps et d'une distance de parcours.

**Exercice 9 [Accélération moyenne]**  
Écrire une fonction en Python renvoyant une accélération moyenne à partir d'un temps de parcours, de la vitesse au début de ce parcours et à fin de celui-ci.
