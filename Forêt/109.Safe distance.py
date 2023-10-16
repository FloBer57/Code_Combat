# Collect coins to repair the cart while staying close to the peasant!

while True:
    item = hero.findNearestItem()
    if item:
        distance = hero.distanceTo(item)
        if distance <15 :
            hero.moveXY(item.pos.x,item.pos.y)
            # Move to the red X after collecting the coin.
            hero.moveXY(42, 45)
            

