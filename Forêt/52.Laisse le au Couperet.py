# Ceci montre comment définir une fonction appelée cleaveWhenClose
# Cette fonction définit un paramètre appelé `target`
def cleaveWhenClose(target):
    if hero.distanceTo(target) < 5:
        if hero.isReady("cleave"):
            hero.cleave(target)
        else:
            hero.attack(target)


# Ce code ne fait pas partie de la fonction.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        cleaveWhenClose(enemy)
