# Lure the ogres into a trap. These ogres are careful.
# They will only follow if the hero is injured.

# This function checks the hero's health 
# and returns a Boolean value.
def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False

while True:
    # Move to the X only if shouldRun() returns True
    if shouldRun(True):
        hero.moveXY(75, 37)
    else:
        enemy = hero.findNearestEnemy()
        hero.attack(enemy)
    # Else, attack!
    