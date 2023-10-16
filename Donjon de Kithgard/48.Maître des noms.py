# Ton héros ne connaît pas le nom de ces ennemis !
# Les lunettes te donnent la capacité de trouver l'ennemi le plus proche (findNearestEnemy).

# Assigne le résultat de hero.findNearestEnemy() à la variable enemy1:
enemy1 = hero.findNearestEnemy()
# enemy1 maintenant fait référence à l'ennemi le plus proche. Utilise cette variable pour attaquer !
hero.attack(enemy1)
hero.attack(enemy1)

# Maintenant que l'ennemi est battu, appelle  hero.findNearestEnemy()  de nouveau aura pour résultat de trouver le nouvel ennemi le plus proche.
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.attack(enemy2)

# Assigne le résultat de hero.findNearestEnemy()  à la variable enemy3:
enemy3 = hero.findNearestEnemy()
hero.attack(enemy3)
hero.attack(enemy3)
# Maintenant attaque en utilisant la variable enemy3:

