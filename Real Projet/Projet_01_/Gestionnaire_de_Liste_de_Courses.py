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


def supprimer_article(liste):
    afficher_liste(liste)
    if liste:
        try:
            index = int(input("Entre le numero de l'article que tu veux supprimer : "))
            if 0 < index <= len(liste):
                article = liste.pop(index - 1)
                print(f"{article} a ete mis a la poubelle!")
            else:
                print("ce nest pas valide")
        except ValueError:
            print("numero invalide, put un autre numero.")


def gestionnaire_liste_de_courses():
    liste_de_courses = []
    choix = input("choisissez une option : ")
    if choix == '1':
        ajouter_article(liste_de_courses)
    elif choix == '2':
        afficher_liste(liste_de_courses)
    elif choix == '4':
        print("Au revoir!!")
        break
    else:
        print("choix pas valide man.")

