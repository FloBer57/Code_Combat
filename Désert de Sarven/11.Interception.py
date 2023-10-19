# Stand between the peasant and the tower.
while True:
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    # Calculate x by adding friend.pos.x to enemy.pos.x
    x = friend.pos.x + enemy.pos.x
    x = x/2
    # Then divide by 2.
    # Check the guide if you need more help!
    
    # Now do the same for y
    y = friend.pos.y + enemy.pos.y
    y = y/2
    # Move to the x and y coordinates you calculated.
    hero.moveXY(x, y)

