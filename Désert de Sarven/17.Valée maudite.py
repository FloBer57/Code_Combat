# Il fait trop chaud dehors! A chaque seconde tu perds de la vie.

while True:
    item = hero.findNearestItem()
    enemy = hero.findNearestEnemy()
    # Attack if enemy exists AND enemy.team is "ogres"
    # AND enemy.type is "skeleton"
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)
        
        
    elif item and item.type == "potion" and (hero.health < (hero.maxHealth / 4)) :
        hero.moveXY(item.pos.x, item.pos.y)
            
    # Collect if item exists AND item.type is "potion"
    # AND hero.health is less than hero.maxHealth / 4
    