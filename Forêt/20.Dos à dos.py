# Restez au mileu et protégez !

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Soit attaquez l'ennemi...
        hero.attack(enemy)
        pass
    else:
        hero.moveXY(40,34)
        # ...soit reculez jusqu'à votre position de défense.
        
        pass
