# Fendez les Munchkins pour survire!
# Assurez vous que vous avez assez d'armure.

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
        
