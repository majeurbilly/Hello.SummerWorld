from typing import Any

#  Variable : Un conteneur nommé pour stocker des données.
#  GAB: Commentaires doivent etre sous le format '# espace espace texte'
#  ^ comme les deux commentaires ci-dessus qui commence deux espaces apres le #

t = 0  # GAB: si tu veux commenter sur une ligne, alors seulement un espace apres le # suffit.

x = "billy"
y = 42
y = 3.14  # GAB: Ici tu utilise le fait que python est dynamique pour modifier le type de la variable.
#  GAB: C'est quelque chose d'interdit dans la plupart des langages de programmation. Puisque tu as declaré y comme un int (implicitement) et tu l'as changé en float apres.
#  GAB: Personellement, je prefere declarer les variables avec leur type car je devrais le connaitre la plupart du temps. Si je ne le connais pas, c'est la que j'utiliserais le dynamisme de python.

est_vrai: bool = True  # GAB: Tu peux declarer le type de la variable comme ca. C'est une bonne pratique. (: bool entre le nom de la variable de le signe egale)
ma_liste_de_chiffre: list[int] = [1, 2, 3, 4, 5]
ma_liste_de_mot: list[str] = ["moi", "plus toi", "plus zoboumafou"]
liste_en_phrase: str = " ".join(ma_liste_de_mot)
mon_tuple: tuple[int, int, int] = (10, 20, 30)
mon_dict: dict[str, Any] = {"nom": "billy",
                            "binaritée": 1}  # GAB: Any est un type special qui peut etre n'importe quoi. Ca me permet de definir le type de mon dictionnaire sans savoir ce que la valeur peut etre.
mon_set: set[int] = {1, 2, 3, 4, 5}
valeur_1: str | None = None  # GAB: None est un type special qui represente l'absence de valeur. Ici je dit que valeur_1 peut etre soit un str soit None et je met none pour l'instant.
valeur_2: bool = True
valeur_3: bool = False
octets = b"commprend pas encore"  # GAB: Occupe toi pas de ca c'est pentoute utile sauf sur tres rares occasions
tableau_octets = bytearray(b"wtf")  # GAB: voir commentaire ci-dessus
vue = memoryview(b"wtfx1000")  # GAB: voir commentaire ci-dessus

print(x)
print(y)
print(y)
print(est_vrai)
print(ma_liste_de_chiffre)
print(ma_liste_de_mot)
print(liste_en_phrase)
print(mon_tuple)
print(mon_dict)
print(mon_set)
print(valeur_1)
print(valeur_2)
print(valeur_3)
print(octets)
print(tableau_octets)
print(vue)
