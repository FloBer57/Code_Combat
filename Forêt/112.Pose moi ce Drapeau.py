# Pose des drapeaux où tu veux construire des pièges.
# Lorsque tu ne poses pas de pièges, ramasse des pièces !

while True:
    flag = hero.findFlag()
    if flag:
        # Comment récupérer flagX et flagY à partir de la position du drapeau (flag.pos) ?
        fx = flag.pos.x
        fy = flag.pos.y
        # (Regarde plus bas comment récupérer les coordonnées x et y d'un objet)
        
        
        hero.buildXY("fire-trap", fx, fy)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            hero.moveXY(itemX, itemY)
