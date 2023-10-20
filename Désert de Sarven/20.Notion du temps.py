# Utilise ton nouveau pouvoir pour choisir ce que tu dois faire :  hero.time

while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # Durant les 10 premières secondes : se battre.
    if hero.time < 10:
        hero.attack(enemy)
        pass
    # Sinon, si on est toujours dans les 35 premières secondes, ramasser des Pièces.
    elif hero.time < 35:
        hero.moveXY(item.pos.x, hero.pos.y)
        pass
    # Après 35 secondes, rejoindre le raid !
    else:
        if hero.time > 35:
            enemy = hero.findNearestEnemy()
            hero.attack(enemy)
        pass
