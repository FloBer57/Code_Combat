# Votre Cleave est sur 10 secondes de temps d'attente.
# Utilisez une autre instruction "else"  pour vous défendre pendant la recharge.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave()
    else:
        hero.attack(enemy)
    
        