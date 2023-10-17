# Laissez les yaks approcher, puis déplacez vous 10m tout droit pour esquiver.
# Esquivez 4 yaks pour compléter le niveau.

while True:
    # Obtenez votre position actuelle (x et y) en utilisant votre Pierre de réflexion.
    x = hero.pos.x
    y = hero.pos.y
    
    # Trouve le yak le plus proche.
    yak = hero.findNearestEnemy()
    
    # Utilisez "if" pour vous déplacer uniquement lorsqu'un yak est à 10m.
    if hero.distanceTo(yak) < 10:
        # Pour avancer tout droit, ajoutez 10 à votre position x.
        hero.moveXY(x + 10, y)
        # Utilisez moveXY pour bouger !
        
        pass
    