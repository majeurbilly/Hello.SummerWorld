from real_projet.projet_01.liste_de_course.affichage import afficher_liste


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
