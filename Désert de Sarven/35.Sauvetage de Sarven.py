while True:
    enemy = hero.findNearestEnemy()
    item = hero.findItems()
    greenflag = hero.findFlag("green")
    
    if greenflag:
        hero.pickUpFlag(greenflag)
        
    if enemy:
        if hero.isReady("power-up"):
            hero.powerUp()
            
        else:
            hero.attack(enemy)
    if item and item.type == "coin" :
        hero.moveXY(coin.pos.x, coin.pos.y)
    if item and item.type =="potion":
        hero.moveXY(item.pos.x, item.pos.y)
