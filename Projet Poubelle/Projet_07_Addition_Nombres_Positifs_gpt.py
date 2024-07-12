# Demande les ingrédients
frist = input("premier chiffre: ")
second = input("deux: ")

# Transforme les bananes en pommes
frist = int(frist)
second = int(second)

# Vérifie si les ingrédients sont bons
if frist > 0 and second > 0:

    # Mélange les ingrédients (suit la recette)
    result = frist + second

    # Sers la salade (montre le résultat)
    print("Le résultat est:", result)
else:
    # Les gardes disent "Non !"
    print("Désolé, nous n'acceptons que des nombres positifs.")
    