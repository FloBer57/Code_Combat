# N'insulte pas cette tribu d'ogres pacifiques.

while True:
    item = hero.findNearestItem()
    if item:
        # If item.type N'EST PAS EGAL A "gem"
        if item.type != "gem":
            # Ensuite, suit ton loup domestique.
            hero.moveXY(pet.pos.x, pet.pos.y)
            
        else:
            hero.moveXY(item.pos.x, item.pos.y)
        
        
            # Déplace-toi jusqu'à la position de la gemme.
            
