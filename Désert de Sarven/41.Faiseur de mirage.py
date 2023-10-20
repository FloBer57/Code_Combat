# Lure the ogres into an ambush!

# Tant que votre or est inférieur à 25, ramassez des pièces.
while True:
    if hero.gold < 25 :
        item = hero.findNearestItem()
        hero.moveXY(item.pos.x, item.pos.y)
        
    if hero.health == hero.maxHealth :
        hero.say("AHAHAH")
        
    if hero.gold >= 25:
        hero.buildXY("decoy", 72, 68)
        break
    
hero.moveXY(22, 16)
        
# Alors, construisez un leuure pour écarter les bagarreurs.

# Tant que votre santé est complète, insultez les petits ogres pour les provoquer.

# Faites alors retraite dans votre base pour leur tendre une embuscade.
