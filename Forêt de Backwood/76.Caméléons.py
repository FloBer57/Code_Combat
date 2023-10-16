# Les ogres sont déguisés en pièces ou en gemmes !

while True:
    enemy = hero.findNearestEnemy()
    # Si vous voyez un ennemi - attaquez-le :
    if enemy:
        hero.attack(enemy)
        
    item = hero.findNearestItem()
    if item :
        hero.moveXY(item.pos.x, item.pos.y)# Si vous voyez une pièce ou une gemme - déplacez-vous à sa position X et Y :
    
