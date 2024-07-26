

#Variable : Un conteneur nommé pour stocker des données.

#Variables :
x = 4
y = "Billy"
a = 4
b = "le plus cool"
c = ", je pense que j'ai saisis le priciple des variable."
d = "Next!!"
e = "Stu " + "quelques " + "chose " + "de " + "fessable" + "?"
f = "Stu" + " " + "quelques" + " " + "chose" + " " + "de" + " " + "fessable" + "?"
g = " ".join(["Stu", "quelques", "chose", "de", "fessable?"])  #Wtf ca, ca brisé mon cerveau
                                                               # remplace le " " avant le join par ", " pour voir la difference.
                                                               #  Ensuite met "billy" a la place de ", "

print(x)
print(y)
print(x + a)
print(y, b)
print(y, b + c + d)
print(e)
print(f)
print(g)
