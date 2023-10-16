# Build traps on the path when the hero sees a munchkin!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY("fire-trap", 41, 24)
        pass
    else:
        hero.moveXY(19, 19)
        
    # Add an else below to move back to the clearing
    
        # Move to the Wooden X (19, 19)
        