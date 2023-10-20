# Les while-loops se répètent jusqu'à ce que la condition soit fausse.

ordersGiven = 0
while ordersGiven < 5:
    # Bougez et ordonnez à chacun de vos alliés de participer à la bataille. (Vous ne pouvez les entendre que si vous vous tenez directement devant eux.)
    hero.moveXY(hero.pos.x, hero.pos.y - 10)
    hero.say("Attack!")
    # Order your ally to "Attack!" with hero.say
    # They can only hear you if you are on the X.
    hero.say("Attack!")
    ordersGiven += 1

    # Be sure to increment ordersGiven!
    

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        
    # Lorsque vous donnez des ordres, participez à l'attaque.
    
