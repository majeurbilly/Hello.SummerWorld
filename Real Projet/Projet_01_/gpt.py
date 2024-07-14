def afficher_menu():
    # Affiche le menu principal
    print("\nMenu :")
    print("1. Ajouter un article")
    print("2. Afficher la liste de courses")
    print("3. Supprimer un article")
    print("4. Quitter")


def ajouter_article(liste):
    # Demande à l'utilisateur d'ajouter un article à la liste
    article = input("Entrez le nom de l'article à ajouter : ")
    liste.append(article)
    print(f"{article} a été ajouté à la liste !")


def afficher_liste(liste):
    # Affiche les articles de la liste de courses
    print("\nListe de courses :")
    if not liste:
        print("Votre liste de courses est vide.")
    else:
        for i, article in enumerate(liste, 1):
            print(f"{i}. {article}")


def supprimer_article(liste):
    # Supprime un article de la liste de courses
    afficher_liste(liste)
    if liste:
        try:
            index = int(input("Entrez le numéro de l'article à supprimer : "))
            if 0 < index <= len(liste):
                article = liste.pop(index - 1)
                print(f"{article} a été supprimé de la liste.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")


def gestionnaire_liste_de_courses():
    # Fonction principale pour gérer la liste de courses
    liste_de_courses = []
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_article(liste_de_courses)
        elif choix == '2':
            afficher_liste(liste_de_courses)
        elif choix == '3':
            supprimer_article(liste_de_courses)
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


# Exécution du programme
gestionnaire_liste_de_courses()
