# Utilisez la fonction checkAndAttack pour faciliter la lecture de votre code.

# Cette fonction a un paramètre.
# Un paramètre est un moyen de transmettre des informations dans une fonction.
def checkAndAttack(target):
    # Le paramètre 'target' est juste une variable!
    # Il contient l'argument lorsque la fonction a été appelée.
    if target:
        hero.attack(target)
    hero.moveXY(43, 34)

while True:
    hero.moveXY(58, 52)
    topEnemy = hero.findNearestEnemy()
    # En utilisant la fonction checkAndAttack avec la variable topEnemy.
    checkAndAttack(topEnemy)
    
    hero.moveXY(58, 16)
    bottomEnemy = hero.findNearestEnemy()
    checkAndAttack(bottomEnemy)
    # Créez une variable nommée bottomEnemy et trouvez l'ennemi le plus proche
    # Utilisez la fonction checkAndAttack et incluez la variable bottomEnemy.
    
