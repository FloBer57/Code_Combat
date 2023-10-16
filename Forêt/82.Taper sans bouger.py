# Tu es piègé. Ne bouge pas, ca ferait mal 

# Cette fonction vérifie si l'enemy est dans la distance d'attaque
def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)
    # Presque toute les épées ont une distance d'attaque de 3
    if distance <= 3:
        return True
    else:
        return False

# Attaque les ogres seulement quand ils sont à portée
while True:
    # Trouve le plus proche enemy et sauvegarde le dans une variable
    enemy = hero.findNearestEnemy()
    inAttackRange(enemy)
    canAttack = inAttackRange(enemy)
    if canAttack == True :
        hero.attack(enemy)
        
    # Appelle inAttackRange(enemy) avec enemy comme argument
    # et sauvegarde le résultat dans canAttack
    
    # si le resultat sauvegardé dans canAttack est vrai  True, alors attaque !
    
    pass
