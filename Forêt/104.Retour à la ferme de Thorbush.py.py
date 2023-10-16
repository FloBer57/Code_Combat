# La fonction maybeBuildTrap (traduction : peutEtreFabriqueUnPiege) définit DEUX paramètres !
def maybeBuildTrap(x, y):
    # Utilise x et y pour les coordonnées auxquelles aller
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY("fire-trap", x, y)
        pass
        # utilise buildXY pour construire un "fire-trap" aux x et y donnés
        
while True:
    # Ceci appelle maybeBuildTrap avec les coordonnées de l'entrée du haut
    maybeBuildTrap(43, 50)
    maybeBuildTrap(25, 34)
    maybeBuildTrap(45, 20)
    # Maintenant utilise maybeBuildTrap à l'entrée de gauche
    
    # Maintenant utilise maybeBuildTrap à l'entrée du bas
    
    