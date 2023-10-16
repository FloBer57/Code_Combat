# Ramassez les pièces seulement si elles sont proches de 20m.
# Ramassez toutes les gemmes.

while True:
    item = hero.findNearestItem()
    distance = hero.distanceTo(item)
    # Si le type de l'item est "gemme"
    if item.type == "gem" or distance < 20 :
        hero.moveXY(item.pos.x, item.pos.y)
    # OU la distance vers l'item à moins de 20 mètres.
    
        # Se déplacer vers l'emplacement de l'item.
        
