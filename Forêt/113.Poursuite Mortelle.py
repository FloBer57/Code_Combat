# Attrape toutes les pièces et utilise les drapeaux pour construire des pièges derrière toi.
# Tu t'occupes de ces ogres.

while True:
    flag = hero.findFlag()
    item = hero.findNearestItem()
    if flag:
        hero.pickUpFlag(flag)
        hero.buildXY("fire-trap", flag.pos.x, flag.pos.y)
    elif item:
        if item.type == "coin" : 
            hero.moveXY(item.pos.x, item.pos.y)
        