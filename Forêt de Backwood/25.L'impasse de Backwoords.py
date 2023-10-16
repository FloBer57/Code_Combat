# Ces Munchkins ont peur du héros!
# Par contre, quand ils seront assez nombreux, les Munchkins se regrouperont et t'embusqueront! Fais attention!
# À chaque fois que tu le peux, `cleave` afin de détruire le groupe d'ennemis.

while True:
    enemy = hero.findNearestEnemy()
    
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
    
        # Fends!
        
    # Autrement, si 'cleave' n'est pas prêt:
    
        # Attaque l'ogre le plus proche
        