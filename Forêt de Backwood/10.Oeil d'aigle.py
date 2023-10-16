# Souviens toi qu'un ennemi peut ne pas exister pour le moment.
while True:
    enemy = hero.findNearestEnemy()
    # S'il un ennemi existe, alors attaque-le !!
    if enemy:
        hero.attack(enemy)
