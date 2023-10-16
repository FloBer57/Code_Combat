# Utilisez ce que vous avez appris pour vaincre les ogres.
# Remember: it takes two attacks to defeat an ogre munchkin!
while True:
    enemy = hero.findNearestEnemy()
    if enemy :
        hero.attack(enemy)
    else :
        hero.moveLeft()
    
