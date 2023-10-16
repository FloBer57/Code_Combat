# Si vous essayez d'attaquer un ennemi distant, votre héros chargera vers lui en ignorant les drapeaux.
# Vous devez vous assurer de n'attaquer que les ennemis proches de vous !

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        # Ramassez le drapeau.
        hero.pickUpFlag(flag)
        hero.say("Je devrais ramasser le drapeau.")
    elif enemy:
        # N'attaquez que si l'ennemi est à moins de 10 mètres
        distance = hero.distanceTo(enemy)
        if enemy and distance < 10:
            hero.attack(enemy)
