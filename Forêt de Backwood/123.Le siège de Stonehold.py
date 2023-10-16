# Aide tes amis en battant les serviteurs de Thoktar.
# Vous aurez recours à un équipement fort et une bonne stratégie pour gagner.
# Les drapeaux pourraient aider, mais c'est à toi de décider - sois créatif !
# Il y a un docteur derrière la clôture. Rejoins le X pour être soigné.

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
        
