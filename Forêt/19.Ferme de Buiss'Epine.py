# Patrouille aux entrées du village.
# Construits un "fire-trap" (piège explosif) quand tu aperçois un Ogre.
# Ne fais pas exploser de paysan !

while True:
    hero.moveXY(43, 50)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43, 50)

    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    # Check if `left` exists.
    if left:
        hero.buildXY("fire-trap", 25,34)
        # Build a trap at 25, 34 if the enemy exists.
        
    hero.moveXY(43, 20)
    bot = hero.findNearestEnemy()
    # Set a variable for the bottom enemy.
    if bot:
        hero.buildXY("fire-trap",43,20)
    # Check if the bottom enemy exists.
    
        # Build a trap at 43, 20 if an enemy exists.
        