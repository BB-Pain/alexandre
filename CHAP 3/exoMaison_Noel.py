# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code :
Créez la liste L_match_2=['Samira', 'Laura', 'Lucie']
la liste L_match_2 sera créée à partir de la liste L_match_1 dont vous remplacerez Léa par Laura
vous pourrez utiliser copy()
"""


"""
L_match_1=["Samira","Léa","Lucie"]

L_match_2 = L_match_1.copy()


L_match_2[1] = 'Laura'

print(L_match_2)
"""


""" Code :
Créez le dictionnaire D_match_2={'joueuse1': 'Samira', 'Joueuse2': 'Laura', 'Joueuse3': 'Lucie'}
le dico D_match_2 sera créée à partir du dico D_match_1 dont vous remplacerez Léa par Laura
vous pourrez utiliser copy()
"""

"""
D_match_1 = {'joueuse1': 'Samira', 'joueuse2': 'Léa', 'joueuse3': 'Lucie'}

D_match_2 = D_match_1.copy()

D_match_2['joueuse2'] = 'Laura'
print(D_match_2)
"""




""" Code :
Quel est l'instruction permettant d'afficher "Mbappé" depuis le dictionnaire dicoProfs ?
"""



"""
dicoProfs={"SI":"Effel","Phys":" Einstein","Espagnol":"Dali","Anglais":"Shakespeare","EPS":["Bolt","Mbappé"],"H-G":"Michelet"}

# Affichage de la valeur associée à la clé 'EPS'
print(dicoProfs['EPS'])  # Affiche ['Bolt', 'Mbappé']

# Affichage Juste Mbappé
print(dicoProfs['EPS'][1]) 
"""






""" Code :
Ecrivez un code qui crée la liste suivante : [[1, 2], [2, 2], [3, 2], ... [9, 2]]
"""


"""
liste = []

liste = [[i, 2] for i in range(1, 10)]

print(liste)
"""





""" Code :
Ecrivez un code qui crée la liste suivante par compréhension : [[1, 2], [2, 2], [3, 2], ... [9, 2]]
"""

"""
# Création de la liste en utilisant une compréhension de liste
liste = [[i, 2] for i in range(1, 10)]

print(liste)  # Affiche [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]
"""

""" Code :
Ecrivez un code qui crée la liste L suivante à partir des listes L1 et L2 de même taille : L=[0,1,2,'d','e','f','g','h','i','j']
"""


"""
L1 = [0,1,2,3,4,5,6,7,8,9]
L2 = ['a','b','c','d','e','f','g','h','i','j']
L=[]

for x in L1:
   L.append(x)

for y in L2:
   L.append(y)

print(L) 
"""
""" Code :
Ecrivez un code qui cré la liste L suivante par compréhension à partir des listes L1 et L2 de même taille : L=[0,1,2,'d','e','f','g','h','i','j']
"""

L1 = [0,1,2,3,4,5,6,7,8,9]
L2 = ['a','b','c','d','e','f','g','h','i','j']
L = L1 + L2

print(L)