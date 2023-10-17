# Évadez-vous du côté droit de la vallée.

# La fonction déplace le héros vers le bas et vers la droite.
def moveDownRight(step):
    hero.moveXY(hero.pos.x + step, hero.pos.y - step)

#  La fonction déplace le héros vers le haut et vers la droite.
def moveUpRight(step):
    # Complétez cette fonction:
    hero.moveXY(hero.pos.x + step, hero.pos.y + step)
    pass

#  Le chasseur est gentil et montrera la route.
hunter = hero.findFriends()[0]
route = hunter.route
routeIndex = 0

while routeIndex < len(route):
    direction = route[routeIndex]
    if direction > 0:
        moveUpRight(8)
    else:
        moveDownRight(8)
        
        pass
    routeIndex += 1
