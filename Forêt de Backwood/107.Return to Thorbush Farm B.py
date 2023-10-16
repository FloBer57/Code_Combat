# The function maybeBuildTrap defines TWO parameters!
def maybeBuildTrap(x, y):
    # Use x and y as the coordinates to move to.
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        pass
        hero.buildXY("fire-trap",x,y)
        # Use buildXY to build a "fire-trap" at the given x and y.
        
while True:
    # This calls maybeBuildTrap, with the coordinates of the bottom entrance.
    maybeBuildTrap(38, 20)
    
    # Now use maybeBuildTrap at the right entrance!
    maybeBuildTrap(56, 34)
    # Now use maybeBuildTrap at the top entrance!
    maybeBuildTrap(38, 48)
    