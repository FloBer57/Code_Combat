# Avancez pour atteindre l'oasis
# mais reculez pour éviter les Yaks a proximité
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # Déplacez-vous à gauche en soustrayant 10 de vos coordonnées X
        hero.moveXY(x - 10, y)
        # Use moveXY to move to the new x, y position.
        
        pass
    else:
        # Déplacez-vous à droite en additionnant 10 à vos coordonnées X
        hero.moveXY(x + 10, y)
        # Use moveXY to move to the new x, y position.
        
        pass
