# La propriété `pos` est un object avec les propriétés 'x' et 'y'.
# 'pos.x' est un nombre représentant la position horizontale sur la carte.
# 'pos.y' est un nombre représentant la position verticale sur la carte.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        x = enemy.pos.x
        y = enemy.pos.y
        
        # dit la position 'x' et 'y' séparée par une virgule.
        hero.say(x + "," + y)
    else:
        hero.say("Cease" + " " + "Fire!")
