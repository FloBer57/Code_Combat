# Survivez aux deux vagues en vous protégeant et en fendant vos ennemis.
# Quand "cleave" n'est pas prêt, utilisez votre talent "shield".
# Vous aurez besoin d'au moins 142 points de vie pour survivre.
enemy = hero.findNearestEnemy()

while True:
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
        
