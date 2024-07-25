
#Variable : Un conteneur nommé pour stocker des données.
#Type de Données : La nature de la valeur contenue dans la variable.


#int (nombre entier) :
age = 25
pomme = 72
jours = 365
dette de mouton = -6

                            nombre = int("42")
                              print(nombre)  # Affiche 42


#float (nombre décimal) :
pi = 3.14
temperature = -10.5
prix du gaz = 1.83

                            nombre_flottant = float("3.14")
                              print(nombre_flottant)  # Affiche 3.14


#str (chaîne de caractères) :
greeting = "Salutation"
nom = "Billy"
age = "69"
f = "Stu" + " " + "quelques" + " " + "chose" + " " + "de" + " " + "fessable" + "?"
g = " ".join(["Stu", "quelques", "chose", "de", "fessable?"])

                              chaine = str(123)
                                print(chaine)
                            chaine = str("salut comment ca va")
                                print(chaine)


#bool (booléen ; verifie les conditions) :
lumiere.allumee = True
lumiere.fermee = False
utilisateur_connecte = True
print(bool(1))  # Affiche True
print(bool(2))  # Affiche True
print(bool(3))  # Affiche True
print(bool(4))  # Affiche True
print(bool(5))  # Affiche True
print(bool(10000000000000000000000000000))  # Affiche True
print(bool(-1)) # Affiche True
print(bool(-90)) # Affiche True

utilisateur_deconnecte = False
print(bool(0))       # Affiche False
print(bool(""))      # Affiche False
print(bool([]))      # Affiche False
print(bool({}))      # Affiche False
print(bool(()))      # Affiche False
print(bool(None))    # Affiche False
print(bool(False))   # Affiche False

                                valeur_booleenne = bool(1)
                                    print(valeur_booleenne)  # Affiche True
                                valeur_booleenne = bool(0)
                                    print(valeur_booleenne)  # Affiche False


#list (liste ; collection ordonné modifiable) :
numbers = [1, 2, 3, 4]
fruits = ["pomme", "banane", "cerise"]

                                ma_liste = [10, 20, 30]
                                    print(ma_liste)  # Affiche [10, 20, 30]


#tuple (tuple ; collection ordonné immuable *non modifialbe) :
coordinates = (10, 20)

                                mon_tuple = (10, 20, 30)
                                    print(mon_tuple)  # Affiche (10, 20, 30)


#dict (dictionnaire ; collection paire, clé-valeur) :
student = {"name": "Alice", "age": 25}

                                mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}
                                    print(mon_dict)  # Affiche {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}


#set (ensemble ; valeur unique non ordonné) :
unique_numbers = {1, 2, 3, 4}

                                fruits = set(["pomme", "banane", "cerise"])
                                    print(fruits)  # Affiche {'pomme', 'banane', 'cerise'}


