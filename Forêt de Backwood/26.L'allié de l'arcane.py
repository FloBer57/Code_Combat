# Fendez les Munchkins pour survire!
# Assurez vous que vous avez assez d'armure.

while True:
    ogre = hero.findNearestEnemy(ogre)
    if hero.isReady("cleave"):
        hero.cleave(ogre)
    else:
        hero.attack(ogre)
        
