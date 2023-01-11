# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code1* :
Comptage du nombre d'occurences (répétitions) dans une liste non triée.
Ne pas utiliser count()
Exemple :
Entrées : L=[3,2,7,1,3,3,4,5,6,3,7,2] et 3
Sortie : 4
"""
def nombre_occurences(L, répétitions):
    nb = 0
    for i in L:
        if i == répétitions:
            nb += 1
    return nb

L = [3, 2, 7, 1, 3, 3, 4, 5, 6, 3, 7, 2]
répétitions = 3
print(nombre_occurences(L, répétitions))




""" Code2* :
Comptage du nombre d'occurences inférieures à l'occurence choisie dans une liste non trièe
Ne pas utiliser count()
Exemple :
Entrée : L=[3,2,7,1,3,3,4,5,6,3,7,2] et 4
Sortie : Il y a 7 occurences inféreures à l'occurence 4 dans la liste
"""

def nombre_inbférieur_occurences(L1, nombre):
    nbr = 0
    for i in L1:
        if i < nombre:
            nbr += 1
    return nbr

# Exemple d'utilisation
L1 = [3, 2, 7, 1, 3, 3, 4, 5, 6, 3, 7, 2]
nombre = 4
print("Il y a", nombre_inbférieur_occurences(L1, nombre), "occurences inférieures à l'occurence", nombre, "dans la liste")


