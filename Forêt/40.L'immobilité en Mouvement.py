# Vous pouvez imbriquer une condition if dans une autre condition if.
# Faite attention à la manière dont les conditions if interagissent entre elles.
# Assurez-vous que l'indentation soit correcte!
# Il est utile de démarrer avec un if/else externe,
# utilisation des commentaires en tant qu'espaces réservés pour le if/else interne:

while True:
    enemy = hero.findNearestEnemy()
    # S'il y a un ennemi, alors...
    if enemy:
        # Créez une variable de distance avec distanceTo.
        distance = hero.distanceTo(enemy)
        if distance < 5 :
            hero.attack(enemy)
            
        else:
            hero.shield()
            
            
        # Si la distance est inférieure à 5 mètres, alors il faut attaquer.
        
        # Sinon (l'ennemi est loin), alors il faut utiliser le bouclier.
        
        pass
    # Sinon (s'il n y a pas d'ennemi)...
    else:
        # .. puis revenir à X.
        hero.moveXY(40, 34)
