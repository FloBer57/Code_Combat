# Ceci définit une fonction nommée findAndAttackEnemy
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# Ce code ne fait pas partie de la fonction.
while True:
    # Maintenante tu peux patrouiller le village en utilisant findAndAttackEnemy
    hero.moveXY(35, 34)
    findAndAttackEnemy()
    
    hero.moveXY(60,31)
    findAndAttackEnemy()
    
    
    # Utilise findAndAttackEnemy
    
