# Atteignez l'oasis. Attention aux nouveaux ennemis : les ogres éclaireurs !
# Allez vers le haut et la droite en ajoutant votre position en x et en y.

while True:
    enemy = hero.findNearestEnemy()
    x = hero.pos.x
    y = hero.pos.y
    # Attaque tout les ennemis que tu croise.
    if enemy :
        hero.attack(enemy)
    elif not enemy :
        hero.moveXY(x + 1, y + 1)
    # Ou si il n'y à aucun ennemis en vue, continue d'avancer vers en haut à droite.
    
    pass
    