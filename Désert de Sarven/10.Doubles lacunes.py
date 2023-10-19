# Amenez le héros et le paysan au sud.

# La fonction déplace votre héros le long de la ligne centrale.
def moveDownCenter():
    x = 40
    y = hero.pos.y - 12
    hero.moveXY(x, y)

# La fonction construire une clôture sur la droite de quelque chose :something.
def buildRightOf(something):
    # buildXY une "fence" 20 mètres à quelque chose(something) est à droite.
    hero.buildXY("fence", hero.pos.x -  7, hero.pos.y)
    pass

# La fonction construire une clôture sur la gauche de quelque chose :something.
def buildLeftOf(something):
    # buildXY une "fence" 20 mètres à quelque chose(something) est à gauche.
    hero.buildXY("fence", hero.pos.x + 7, hero.pos.y)
    pass

while True:
    ogre = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if ogre:
        buildLeftOf(ogre)
    if coin:
        buildRightOf(coin)
    moveDownCenter()
