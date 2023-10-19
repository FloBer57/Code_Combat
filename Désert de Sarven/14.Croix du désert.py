# Regarde de quelle direction viennent les orgres.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Gauche : enemy.pos.x est plus petit que hero.pos.x
        isLeft = hero.pos.x  > enemy.pos.x
        # Au-dessus : enemy.pos.y est plus grand que  hero.pos.y
        isAbove = hero.pos.y < enemy.pos.y
        # Droite :  enemy.pos.x est supérieur à hero.pos.x
        isRight = hero.pos.x < enemy.pos.x
        # Au-dessous : enemy.pos.y est inférieur à hero.pos.y
        isDown = hero.pos.y > enemy.pos.y
        # Si l'ennemi isAbove et isLeft:
        # buildXY() l'objet "fire-trap" au repère X.
        if isLeft and isAbove:
            hero.buildXY("fire-trap", 20, 51)
        # Si l'ennemi isAbove et isRight:
        # buildXY() l'objet "fire-trap" au repère X.
        if isLeft and isDown:
            hero.buildXY("fire-trap", 20, 17)
            
        # Si l'ennemi isBelow et isLeft:
        # buildXY() l'objet "fire-trap" au repère X.
        if isDown and isRight:
            hero.buildXY("fire-trap", 60, 17)
        # Si l'ennemi isBelow et isRight:
        # buildXY() l'objet "fire-trap" au repère X.
        if isAbove and isRight : 
            hero.buildXY("fire-trap", 60, 51)
            
        hero.moveXY(40, 34)
    else:
        hero.moveXY(40, 34)