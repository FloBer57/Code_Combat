# Les ogres attaquent à proximité de la colonie !
# Fais attention, car les ogres ont semé du poison dans la terre.
# Ramasse des pièces et vaincs les ogres, mais fait attention aux pièges et au poison !

while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)
    item = hero.findNearestItem()
    if item.type == "gem" or item.type == "coin" :
        hero.moveXY(item.pos.x, item.pos.y)
        
    # Vérifie quel est le type de l'objet pour être sûre que le héro ne ramasse pas du poison !
    # Si le type d'objet est une "gem" ou une "coin":
    
        # Ensuite déplace toi et ramasse le:
        
