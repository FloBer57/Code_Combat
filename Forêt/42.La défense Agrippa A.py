while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        pass  # Remplacez ceci par votre propre code.
        # Trouvez la distance par rapport à l'ennemi avec distanceTo.
        distance = hero.distanceTo(enemy)
        if distance < 5:
            if hero.isReady("cleave"):
                hero.cleave(enemy)
                
            # Si la distance est inférieur à 5 mètres...
        else:
            hero.attack(enemy)
            # ... si "cleave" est prêt, cleave!
            
            # ... sinon, attaquez juste.
            