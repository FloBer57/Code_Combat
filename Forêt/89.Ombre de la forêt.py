# Le Grand ogre ne peut pas vous voir dans la forêt.
# Attaque seulement les petits ogres dans la forêt.
# Collecte les pièces et les gemmes seulement.
# Ne sort pas de la forêt et ne mange ni boit rien .

while True:
    # Trouve l'ennemis le plus proche.
    enemy = hero.findNearestEnemy()
    
    
    if enemy:
        if enemy.type == "munchkin" or enemy.type == "thrower":
            hero.attack(enemy)
        
    
    item = hero.findNearestItem()
    
    
    if item:
        if item.type == "gem" or item.type == "coin":
            hero.moveXY(item.pos.x, item.pos.y)
            
        else:
            False
        
    # Attaquez seulement si c'est un type "Lanceur" ou "munchkin".
    
    # Trouve l'objet le plus proche.
    
    # Collecte seulement si c'est des "gemmes" ou des "pièces". 
    
    pass
