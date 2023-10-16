# Patrouillez aux entrées du village.
# Si vous trouvez un ennmi, attaquez-le.
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    hero.moveXY(60,31)
    
    rightEnemy = hero.findNearestEnemy()
    if rightEnemy:
        hero.attack(rightEnemy)
        hero.attack(rightEnemy)
    # Trouvez l'ennemi de droite.
    
    # Utilisez "if" pour attaquer s'il y a un ennemi à droite.
    
