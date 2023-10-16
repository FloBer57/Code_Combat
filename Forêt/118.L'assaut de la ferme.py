# Les soldats vont arriver peu à peu, mais les Ogres les submergeront.
# Une simple boucle d'attaque ne sera pas suffisante pour te garder en vie.
while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    if green:
        hero.pickUpFlag(green)
    elif black:
        hero.pickUpFlag(black)
        if hero.isReady("cleave"):
            hero.cleave(enemy)
            
    else:
        if enemy:
            
            hero.attack(enemy)
