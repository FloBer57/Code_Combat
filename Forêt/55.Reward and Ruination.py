# It seems like the Ogre Chieftain is stealing your gems!
# Use the two artillery cannons for your goals.

while True:
    enemy = hero.findNearestEnemy()
    cake = hero.findNearestItem()
    
    
    if enemy:
        enemypos = enemy.pos.x + enemy.pos.y
        hero.say("Enemy at " + enemy.pos.x + enemy.pos.y)
        
    if not enemy :
        if cake : 
            cakepos = cake.pos.x + cake.pos.y 
            hero.say("Cake at " + cake.pos.x + cake.pos.y)
    # Now that you have sweet revenge,
    # why not have your cake and eat it, too?
    # Find the item's position and 
    # say it for your artillery to target.
    