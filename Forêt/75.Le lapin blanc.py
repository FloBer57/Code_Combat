# Suivez la pierre de lumière pour passer entre les pièges.

while True:
    item = hero.findNearestItem()
    if item:
        # Enregistrez la position de l'item dans une nouvelle variable en utilisant item.pos :
        x = item.pos.x
        y = item.pos.y
        
        hero.moveXY(x, y)
        # Enregistrez les coordonnées X et Y en utilisant pos.x et pos.y :
        
        # Déplacez-vous jusqu'au coordonnées en utilisant moveXY() et les variables X et Y :
        
        pass
