# Demande combien de nombres l'utilisateur veut additionner
n = int(input("Combien de nombres voulez-vous additionner ? "))

# Initialise la somme à 0
somme = 0

# Utilise une boucle for pour demander les nombres et les additionner
for i in range(n):
    nombre = int(input(f"Veuillez saisir l'entier numéro {i+1} : "))
    somme += nombre

# Affiche le résultat
print("La somme de vos nombres est :", somme)
