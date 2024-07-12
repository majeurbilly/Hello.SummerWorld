# Initialiser la somme à 0
somme = 0

# Boucle pour demander 5 nombres
for i in range(5):
    nombre = int(input(f"Veuillez saisir l'entier numéro {i+1} : "))
    somme += nombre  # Ajouter le nombre à la somme

# Afficher le résultat
print("La somme de vos nombres est :", somme)
