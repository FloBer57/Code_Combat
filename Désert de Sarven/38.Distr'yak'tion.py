# Protégez Brandy des yaks assoiffés !
# Ramassez de l'or pour construire des leurres pour distraire les yaks.
# Utilisez les drapeaux pour décider où et quand construire les leurres.

while True:
    flag = hero.findFlag("green")
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if flag :
        
        hero.pickUpFlag(flag)
        
    if item :
        hero.moveXY(item.pos.x, item.pos.y)
    if hero.gold > 25 :
        hero.buildXY("decoy",hero.pos.x, hero.pos.y)
        
