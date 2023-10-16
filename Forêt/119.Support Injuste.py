# Faufile toi à travers la forêt et tends une embuscade au chaman.
# Ecoute le Commandant Craig pour savoir si des ennemis approchent.

# Tu pourras placer des drapeaux après avoir cliqué sur Envoyer.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.pickUpFlag(flag)
        
        pass
    elif enemy:
        hero.attack(enemy)
        
        pass
