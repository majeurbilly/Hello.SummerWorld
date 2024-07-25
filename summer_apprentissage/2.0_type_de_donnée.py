
#Variable : Un conteneur nommé pour stocker des données.
#Type de Données : La nature de la valeur contenue dans la variable.


#int (nombre entier) : #2.1
age = 25
pomme = 72
jours = 365
dette de mouton = -6

                            nombre = int("42")
                              print(nombre)  # Affiche 42


#float (nombre décimal) : #2.2
pi = 3.14
temperature = -10.5
prix du gaz = 1.83

                            nombre_flottant = float("3.14")
                              print(nombre_flottant)  # Affiche 3.14


#str (chaîne de caractères) : #2.3
greeting = "Salutation"
nom = "Billy"
age = "69"
f = "Stu" + " " + "quelques" + " " + "chose" + " " + "de" + " " + "fessable" + "?"
g = " ".join(["Stu", "quelques", "chose", "de", "fessable?"])

                              chaine_1 = str(123)
                                print(chaine_1)     # Affiche 123
                            chaine_2 = str("salut comment ca va")
                                print(chaine_2)     # Affiche salut comment ca va


#bool (booléen ; verifie les conditions) : #2.4
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


#list (liste ; collection ordonné modifiable) : #2.5
numbers = [1, 2, 3, 4]
fruits = ["pomme", "banane", "cerise"]

                                ma_liste = [10, 20, 30]
                                    print(ma_liste)  # Affiche [10, 20, 30]


#tuple (tuple ; collection ordonné immuable *non modifialbe) : #2.6
coordinates = (10, 20)

                                mon_tuple = (10, 20, 30)
                                    print(mon_tuple)  # Affiche (10, 20, 30)


#dict (dictionnaire ; collection paire, clé-valeur) :  #2.7
student = {"name": "Alice", "age": 25}

                                mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}
                                    print(mon_dict)  # Affiche {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}


#set (ensemble ; valeur unique non ordonné) :  #2.8
unique_numbers = {1, 2, 3, 4}

                                fruits = set(["pomme", "banane", "cerise"])
                                    print(fruits)  # Affiche {'pomme', 'banane', 'cerise'}


