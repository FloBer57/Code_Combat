while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        hero.attack(enemy)
        pass
    else:
        hero.moveXY(40,37)
    
    