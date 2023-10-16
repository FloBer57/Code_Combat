# Attack les munchkins, appelle les brawlers et ignore les burls.

# Cette fonction définit le comportement des héros face aux ennemis.
def dealEnemy(enemy):
    # Si enemy.type est "munchkin":
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" :
        hero.attack(enemy)
        # Ensuite attaque-le:
        
    # Si le type d'ennemi est "brawler":
    if enemy.type == "brawler" :
        hero.say("ouaiouaiouai")
        # Alors dis quelque chose au brawler.
        
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)
