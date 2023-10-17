# Ramassez les pièces. Ignorez les yaks des sables et 
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        if enemy.type != "sand-yak" or enemy.type != "burl":
            
            hero.attack(enemy)
        
    elif item:
        hero.moveXY(item.pos.x, item.pos.y)
        
        pass
    else:
        hero.moveXY(41, 31)
