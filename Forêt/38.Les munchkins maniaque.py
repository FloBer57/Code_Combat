# Un autre coffre dans le champ à ouvrir!
# Attaque le coffre pour forcer son ouverture.
# Certains munchkins ne resteront pas tranquilles pendant que tu les attaques!
# Défends-toi quand un munchkin se rapproche trop.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        hero.cleave(enemy)
        
        pass
    elif distance < 5:
        hero.attack(enemy)
        
        pass
    else:
        hero.attack("Chest")
        
        pass
    
