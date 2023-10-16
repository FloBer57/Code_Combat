# Certaines pièces et gemmes attirent les éclairs.
# Le héros devrait seulement ramasser les pièces en argent et les gemmes bleues.

while True:
    item = hero.findNearestItem()
    
    # Vérifie si le type de l'objet est "coin"
    # L'objet AND est égal à 2.
    if item.type == "coin" and item.value == 2:
        hero.moveXY(item.pos.x, item.pos.y)
    # Une gemme bleue a une valeur de 10.
    gem = hero.findNearestItem()
    
    if item.type == "gem" and item.value == 10 :
        hero.moveXY(item.pos.x, item.pos.y)
        
    # Verifie si le type de l'objet est une "gem"
    # L'objet AND est égal à 10.
    
