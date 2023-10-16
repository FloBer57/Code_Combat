def enemyInRange(enemy):
    # Retournez true si l'ennemi est à moins de 5 unités.
    
    return False

def cleaveOrAttack(enemy):
    if hero.isReady('cleave'):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Vérifiez la distance de l'ennemi en appelant la fonction enemyInRange.
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)
