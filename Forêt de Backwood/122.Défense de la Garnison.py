# Tue tous les ogres qui attaquent.
# Utilise des drapeaux pour t'éloigner des Ogres les plus dangereux.

# De l'aide est nécessaire sur le front.
# Retourne en arrière si quelqu'un essaye de  se faufiler.

        
while True:
    enemy = hero.findNearestEnemy()
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    
    if green:
        hero.pickUpFlag(green)
    if black:
        hero.pickUpFlag(black)
        if hero.isReady("cleave"):
            hero.cleave(enemy)
            
    elif enemy:
        hero.attack(enemy)
        
