# Attaque seulement les ennemis de type "munchkin" ou "thrower".
# N'attaque pas les "burls". Fuis les "ogres" !
while True:
    enemy = hero.findNearestEnemy()
    
    # Souviens-toi : n'attaque pas le type "burl" !
    if enemy.type == "burl":
        hero.say("Je n'attaque pas ce Burl !")
    
    # La propriété "type" indique quel genre de créature c'est
    if enemy.type == "munchkin":
        hero.attack(enemy)
    
    # Utilise "if" pour attaquer un "thrower"
    if enemy.type == "thrower":
        hero.attack(enemy)
    
    # Si c'est un "ogre" utilise moveXY pour aller à la porte du village !
    if enemy.type == "ogre" : 
        hero.moveXY(21, 39)
        
    