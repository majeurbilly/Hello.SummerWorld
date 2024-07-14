### TOUT en python doit respecter le 'snake_case'
### donc meme tes noms de fichiers doivent respecter le format : minuscules_tirets_entres_mots.py

# seulement les valeures de type constante (que tu peux garantir que la valeur ne va jamais changer) ont le format TOUTE_EN_MAJUSCULE.
# seulement les classes (tu est pas rendu la encore) utilise le format 'Capitalization() De() La() Premiere() Lettre()'
# la raison pourquoi c'est comme ca cest que par default tout est minuscule donc c'est des methodes, si tu voit du code qui commence avec une majuscule tu sait que cest une classe et si tu voit du code qui est toute en majuscule tu sait que cest une constante
# ex.:  from my_python_file_somewhere import une_methode_qui_multiplie, Tiguan, LA_DATE_DE_LA_ST_JEAN_DE_CETTE_ANNEE

def ajouter_article():
    article = input("Tu veux quoi bitch?")
    liste.apprend(article)
    print(f"{article} a ete rajouter a la liste!")

def afficher_liste():
    print("\nListe de course: ")
    if not liste:
        print("Liste vide!")
    else:
        for i, article in enumerate(liste, 1):
            print(f"{i}. {article}")

def supprimer_article():
    # une bonne pratique quand tu as pas encore implementer ton code cest de le decrire en commentaire

    # Si liste est pas vide --> caller afficher_liste pour montrer au user quoi il peu delete (if)
    #  ->  Ensuite demander au user quel chiffre correspond au truc a deleter (input)
    #  ->  Si chiffre est dans liste (if input in liste)
    #  ->  ->  retirer element a l'index donner par le user
    #  ->  Sinon redemander a l'utilisateur de choisir (ou ramener au menu selon ton choix) (else)
    # Sinon liste est vide --> afficher message comme quoi ya fuckall a deleter (else)
    pass

user_input: str | None = None
liste: list[str] = []


while user_input != 4:
  print("""
  Bienvenue chez PapaJohn's
  Commandes:

  1) Ajouter articles
  2) Afficher la liste
  3) Supprimer un article
  4) Quitter cette enfer pythonique
  """)
  user_input = input("Entrez votre chiffre icitte: ")
  match user_input:
      case 1:
        ajouter_article()
      case 2:
        afficher_liste()
      case 3:
        supprimer_article()
      case 4:
        print('bye bye!')
        exit(0)
      case _:
        print(f'yo wtf is : {user_input}?!? Im out!')
        exit(1)
                                    # À SUIVRE DANS UNE PROCHAINE ÉPISODE
