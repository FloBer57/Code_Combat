# Utilisez des drapeaux de différentes couleurs pour exécuter de différentes tâches.

while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")
    
    # S'il y a un drapeau vert, construisez une barrière.
    if flagGreen :
        hero.buildXY("fence",flagGreen.pos.x, flagGreen.pos.y)
        # Build a "fence" at flagGreen's position.
        hero.pickUpFlag(flagGreen)
        # Garder en esprit de ramasser les drapeaux après de les avoir utiliser!
        
    # S'il y a un drapeau noir, construisez un piège à feu.
    if flagBlack:
        hero.buildXY("fire-trap", flagBlack.pos.x, flagBlack.pos.y)
        hero.pickUpFlag(flagBlack)
        # Build a "fire-trap" at flagBlack's position.
        
        # Garder en esprit de ramasser les drapeaux après de les avoir utiliser!
        
    # Move back to the center.
    hero.moveXY(43, 31)
    