# Vous devez collecter plusieurs items.
# Mais... le yéti voulait les gemmes!
# Ramassez tous les items que vous voyez SAUF les gemmes.

while True:
    item = hero.findNearestItem()
    if item:
        if item.type != "gem":
            hero.moveXY(item.pos.x, item.pos.y)
            
        # Si item.type n'est pas égal à "gem":
        pass
            # Rendez-vous à la position de l'item.
            
