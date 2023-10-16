while True:
    # Vérifiez la distance avec l'ennemi le plus proche.
    nearestEnemy = hero.findNearestEnemy()
    distance = hero.distanceTo(nearestEnemy)
    # Si ils se rapprochent à moins de 10 mètres, cleave les!
    if distance < 10:
        if hero.isReady("cleave"):
            hero.cleave(nearestEnemy)
    else:
        hero.attack("Chest")
            
        
    # Sinon, attaquer le "coffre" par son nom.
    
    pass
    