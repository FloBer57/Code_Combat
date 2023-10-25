# Defeat skeletons and collect lightstones.

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # Attack while enemy has health.
        while enemy.health > 0:
            hero.attack(enemy)
        enemyIndex += 1
    items = hero.findItems()
    itemIndex = 0
    # Iterate over all items.
    while itemIndex < len(items):
        item = items[itemIndex]
        # Pendant que la distance est strictement supérieure à 4:        
        distance = hero.distanceTo(item)
        if distance >= 4:
            hero.moveXY(item.pos.x, item.pos.y)
            # Essaye de prendre l'objet.
            
        # Don't forget to increase itemIndex.
        itemIndex += 1
