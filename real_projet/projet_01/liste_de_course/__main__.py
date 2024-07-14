from real_projet.projet_01.liste_de_course.affichage import afficher_menu, afficher_liste
from real_projet.projet_01.liste_de_course.ajout import ajouter_article
from real_projet.projet_01.liste_de_course.supprimer import supprimer_article


def gestionnaire_liste_de_courses():
    liste_de_courses = []
    choix = None
    while choix != '4':   # Une condition c'est meilleur qu'un while True (while choix n'est pas egale a 4)
        afficher_menu()
        choix = input("choisissez une numero : ")
        if choix == '1':
            ajouter_article(liste_de_courses)
        elif choix == '2':
            afficher_liste(liste_de_courses)
        elif choix == '3':
            supprimer_article(liste_de_courses)
        elif choix == '4':
            print("Au revoir!!")
        else:
            print("choix pas valide man.")


if __name__ == "__main__":
    gestionnaire_liste_de_courses()
