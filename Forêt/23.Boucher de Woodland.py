# Utilisez votre nouvelle capacité "cleave" (fendre) aussi souvent que possible.

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
        pass
    else:
        hero.attack(enemy)
        
        pass
