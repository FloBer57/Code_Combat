# Utilisez une boucle pour bouger et attaquer.

while True:
    
    hero.moveRight()
    hero.moveUp()
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)
    hero.moveDown()
    hero.moveDown()
    hero.moveUp()
    
    