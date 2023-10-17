# Allez à l'oasis en vous déplaçant vers le bas, 10m à la fois
# Construisez des clôtures 20m à gauche de chaque ogre

while True:
    enemy = hero.findNearestEnemy()
    heroX = hero.pos.x
    heroY = hero.pos.y
    
    if enemy:
        hero.buildXY("fence", enemy.pos.x -20, enemy.pos.y)
        pass
    else:
        # Descendez vers le bas 10 unités à la fois
        hero.moveXY(heroX, heroY -10)
        pass
