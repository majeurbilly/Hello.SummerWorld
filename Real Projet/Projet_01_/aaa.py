def afficher_menu():
    print("\nMenu: ")
    print("1. Ajoutez un article: ")
    print("2. Afficher la liste: ")
    print("3. supprimer un article: ")
    print("Quitter")

def ajouter_article(liste):
    article = input("Tu veux quoi bitch?")
    liste.apprend(article)
    print(f"{article} a ete rajouter a la liste!")

def afficher_liste(liste):
    print("\nListe de course: ")
    if not liste:
        print("Liste vide!")
    else:
        for i, article in enumerate(liste, 1)
            print(f"{i}. {article}")


