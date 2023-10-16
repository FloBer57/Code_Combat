# Obtiens deux secrets de la part du sorcier, avec comme valeur true ou false.
# Consultes le guide pour les notes afin d'écrire des expressions logiques.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# si secretA et le secretB sont tous les deux vrais, prends le chemin du haut, sinon, prends le chemin du bas.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# si soit le secretA ou le secretB est vrai,prends le chemin du haut. 
if secretA == True or secretB == True : 
    hero.moveXY(32, 33)
else:
    hero.moveXY(32, 15)
hero.moveXY(38, 24)
# si le secretB n'est pas vrai, prends le chemin du haut.
if secretB != True :
    hero.moveXY(44,33)
else:
    hero.moveXY(44, 15)    
    
hero.moveXY(50, 24)
