# Les Ogres escaladent !
# Protège les paysans suffisamment longtemps afin que la milice puisse s'assembler.
while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
        pass
    
    if black:
        hero.pickUpFlag(black)
        if hero.isReady("cleave"):
            hero.cleave(enemy)
            
    elif enemy:
        hero.attack(enemy)
        # Utilise les drapeaux pour te déplacer en bonne position, et utilise Fendre (cleave) si cette capacité est prête.
        
        