# Suis le chemin des pièces vers le X rouge à la sortie.

while True:
    # Cela trouve l'item le plus proche.
    item = hero.findNearestItem()
    if item:
        # Cela stocke la position de l'item dans une variable.
        itemPosition = item.pos
        # Mets les coordonnées X et Y de l'item dans des variables.
        itemX = itemPosition.x
        itemY = itemPosition.y
        # Maintenant, utilise moveXY pour se déplacer vers itemX et itemY : 
        hero.moveXY(itemX, itemY)
