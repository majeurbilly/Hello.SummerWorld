### TOUT en python doit respecter le 'snake_case'
### donc meme tes noms de fichiers doivent respecter le format : minuscules_tirets_entres_mots

def ajouter_article(liste: list[str]):
    article = input("Tu veux quoi bitch?")
    liste.apprend(article)
    print(f"{article} a ete rajouter a la liste!")

def afficher_liste(liste: list[str]):
    print("\nListe de course: ")
    if not liste:
        print("Liste vide!")
    else:
        for i, article in enumerate(liste, 1)
            print(f"{i}. {article}")

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
                                    #À SUIVRE DANS UNE PROCHAINE ÉPISODE
