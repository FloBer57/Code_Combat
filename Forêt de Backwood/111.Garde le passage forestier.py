# Utilise les drapeaux pour joindre la bataille ou bien battre en retraite.
# Si tu échoues, soumets encore une fois et réessaye sur des nouvelles vagues aléatoires d'ennemis.
# Tu devrais avoir environ 300 de santé, si ce n'est plus.
while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if flag:
        # Ramasse le drapeau (pickUpFlag)
        hero.pickUpFlag(flag)
        pass
    elif enemy:
        hero.attack(enemy)
        
        pass
