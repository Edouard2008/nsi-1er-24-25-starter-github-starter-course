# Premiere_entrainement

Espace d'entrainement  
NSI Premiere

# Site de formation sur GIT
[Comprendre GIT avec grafikart.fr](https://grafikart.fr/formations/git)# Soumettre son travail : Add - Commit - push
- git add .
- commit -m "Mon commentaire - exercices fait"
- git push


# Recuperer la derniere version du prof - update upstream
- git fetch upstream
- git merge upstream/main
- git add .
- git commit -m "update upstream"
- git push

# Procédure pour ajouter un fichier Python et un fichier de test dans le même dépôt GitHub :

1. **Créer un dépôt GitHub** :
   - Créez un dépôt (repository) sur GitHub, ou accédez à un dépôt existant.
   
2. **Ajouter le fichier Python** :
   - Créez un fichier Python localement, par exemple `main.py`.
   - Dans ce fichier, écrivez votre code Python.
   - Ajoutez et commitez ce fichier à votre dépôt avec les commandes Git :
     ```bash
     git add main.py
     git commit -m "Add main Python file"
     git push
     ```

3. **Ajouter un fichier de test** :
   - Créez un fichier de test, par exemple `test_main.py`, où vous écrirez les tests unitaires.
   - Ajoutez et commitez ce fichier de test au dépôt :
     ```bash
     git add test_main.py
     git commit -m "Add test file"
     git push
     ```

4. **Activer les tests unitaires** :
   - Pour utiliser les tests unitaires, vous pouvez configurer GitHub Actions pour automatiser les tests à chaque commit ou simplement lancer les tests localement avec `pytest`.

## Exemple simple de code Python et de test :

### Fichier `main.py` :
```python
def add(a, b):
    return a + b
```

### Fichier de test `test_main.py` :
```python
import pytest
from main import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

## Exécution des tests :
Si vous avez installé `pytest`, vous pouvez lancer les tests via la commande :
```bash
pytest
```

Cela exécute les tests du fichier `test_main.py` et vérifie que les résultats sont corrects.

# Environnement virtuel
Travailler dans un environnement virtuel permet de garder en memoire toutes les dependances que vous installez
- python3 -m venv myenv
- source myenv/bin/activate
git push origin --delete nom-de-la-nouvelle-branche
```
Pour desactiver
- source deactivate
