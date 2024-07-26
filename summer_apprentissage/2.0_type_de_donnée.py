# Variable : Un conteneur nommé pour stocker des données.
# Type de Données : La nature de la valeur contenue dans la variable.
from typing import Any

# int (nombre entier) : #2.1
age: int = 25
pomme: int = 72
jours: int = 365
#  dette  << ligne invalide
#  de     << ligne invalide
mouton: int = -6

nombre: int = int("42")
print(nombre)  # Affiche 42

# float (nombre décimal) : #2.2
pi: float = 3.14
temperature: float = -10.5
#  prix  << ligne invalide
#  du  << ligne invalide
gaz: float = 1.83

nombre_flottant: float = float("3.14")
print(nombre_flottant)  # Affiche 3.14

# str (chaîne de caractères) : #2.3
greeting: str = "Salutation"
nom: str = "Billy"
age = "69"  # GAB: Type invalide, vu quon as mit int a la ligne 5.
f = "Stu" + " " + "quelques" + " " + "chose" + " " + "de" + " " + "fessable" + "?"
g = " ".join(["Stu", "quelques", "chose", "de", "fessable?"])

chaine_1: str = str(123)
print(chaine_1)  # Affiche 123
chaine_2: str = str("salut comment ca va")
print(chaine_2)  # Affiche salut comment ca va

# bool (booléen ; verifie les conditions) : #2.4


#  lumiere.allumee = True  # C'est un bon concept pour visualiser mais tu as pas creer une classe Lumiere.
#  lumiere.fermee = False  # Voici ce que ca pourrait ressembler:

class Lumiere:
    def __init__(self, etat_initial: bool):
        self.allumee = etat_initial
        self.fermee = not etat_initial

    def allumer(self):
        self.allumee = True
        self.fermee = False

    def eteindre(self):
        self.allumee = False
        self.fermee = True


lumiere: Lumiere = Lumiere(True)
lumiere.allumee = False
lumiere.fermee = True
lumiere.allumer()
print(lumiere.allumee)  # Affiche True

utilisateur_connecte: bool = True
print(bool(1))  # Affiche True
print(bool(2))  # Affiche True
print(bool(3))  # Affiche True
print(bool(4))  # Affiche True
print(bool(5))  # Affiche True
print(bool(10000000000000000000000000000))  # Affiche True
print(bool(-1))  # Affiche True
print(bool(-90))  # Affiche True

utilisateur_deconnecte: bool = False
print(bool(0))  # Affiche False
print(bool(""))  # Affiche False
print(bool([]))  # Affiche False
print(bool({}))  # Affiche False
print(bool(()))  # Affiche False
print(bool(None))  # Affiche False
print(bool(False))  # Affiche False

valeur_booleenne: bool = bool(1)
print(valeur_booleenne)  # Affiche True
valeur_booleenne: bool = bool(0)
print(valeur_booleenne)  # Affiche False

# list (liste ; collection ordonné modifiable) : #2.5
numbers: list[int] = [1, 2, 3, 4]
fruits: list[str] = ["pomme", "banane", "cerise"]

ma_liste: list[int] = [10, 20, 30]
print(ma_liste)  # Affiche [10, 20, 30]

# tuple (tuple ; collection ordonné immuable *non modifialbe) : #2.6
coordinates: tuple[int, int] = (10, 20)

mon_tuple: tuple[int, int, int] = (10, 20, 30)
print(mon_tuple)  # Affiche (10, 20, 30)

# dict (dictionnaire ; collection paire, clé-valeur) :  #2.7
student: dict[str, Any] = {"name": "Alice", "age": 25}

mon_dict: dict[str, str | int] = {"nom": "Alice", "âge": 25, "ville": "Paris"}
print(mon_dict)  # Affiche {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}

# set (ensemble ; valeur unique non ordonné) :  #2.8
unique_numbers: set[int] = {1, 2, 3, 4}

fruits = set(["pomme", "banane", "cerise"])
print(fruits)  # Affiche {'pomme', 'banane', 'cerise'}
