# Cette fonction attaque l'ennemi le plus proche.
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# Définis une fonction pour fendre les ennemis (mais seulement lorsque la capacité est prête).
def findAndCleaveEnemy():
    # Trouve l'ennemi le plus proche:
    enemy = hero.findNearestEnemy()
    # Si un ennemi existe:
    if hero.isReady("cleave"):
        hero.cleave(enemy)
        # Et lorsque "fendre" est prêt:
        
            # Il est temps de fendre!
            
    pass

# Dans la boucle principale, patrouille, fends et attaque.
while True:
    # Déplace-toi vers le point de patrouille, fends et attaque.
    hero.moveXY(35, 34)
    findAndCleaveEnemy()
    findAndAttackEnemy()
    
    # Déplace-toi vers l'autre point:
    hero.moveXY(60, 31)
    # Utilise la fonction findAndCleaveEnemy:
    findAndCleaveEnemy()
    # Utilise la fonction findAndAttackEnemy:
    findAndAttackEnemy()
