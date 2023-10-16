while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        pass  # Remplacer ceci par votre propre code.
        # Trouvez la distance par rapport à l'ennemi avec distanceTo.
        distance = hero.distanceTo(enemy)
        if distance < 5:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
            
        # Si la distance est inférieure à 5 mètres...
        
            # ... si "cleave" est prêt, cleave!
            
            # ... sinon, attaquez simplement.
            