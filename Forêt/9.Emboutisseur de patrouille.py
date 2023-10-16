# Souviens toi qu'un ennemi peut ne pas exister pour le moment.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Si un ennemi existe, alors attaque le !!
        hero.attack(enemy)
        pass
