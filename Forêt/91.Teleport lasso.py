# Our wizards teleport ogres from their camp here.
# They appear for a short period and they are stunned.
# Attack only weak and near ogres.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # If enemy.type is "munchkin"
    if enemy:
        if enemy.type == 'munchkin' and distance < 20:
            hero.attack(enemy)
        
    # AND the distance to it is less than 20m
    
        # Then attack it.
        
