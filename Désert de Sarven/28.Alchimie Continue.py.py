# La course des Ogres pour l'eau, distillé par Omarn Brewstone !
# Utilise "Continue" pour vérifier les conditions de l'embuscade
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # S'il n'y a pas d'ennemis, continue la boucle
    if not enemy:
        continue
    
    # S'il y a un ennemi, mais pas d'objets, demande une potion et continue la boucle.
    if not item:
        hero.say("Donne moi une boisson !")
        continue
    
    # utilise "if" pour contrôler le type d'objet. Si le type est "poison", continue la boucle.
    if item and item.type == 'poison' :
        continue
    
    else :
        hero.moveXY(item.pos.x, item.pos.y)
        hero.moveXY(34, 47)
    # Sinon, la potion doit être une bouteille d'eau, donc va la ramasser et retourne à ton point de départ.
    # so moveXY to the potion, then back to the start!
    