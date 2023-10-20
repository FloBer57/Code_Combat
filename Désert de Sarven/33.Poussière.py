# Utilisez "while" pour faire une boucle jusqu'à ce que vous ayez assez frappé pour tuer 10 munchkins.

attacks = 0
while attacks < 10:
    # Attack the nearest enemy!
    enemy = hero.findNearestEnemy()
    if enemy :
        hero.attack(enemy)
    # Incrementing means to increase by 1.
    # Increment the `attacks` variable.
    attacks += 1

# Lorsque vous avez terminé, fuyez au point d'embuscade.
hero.say("I should retreat!")
hero.moveXY(79, 33)
#∆ Don't just stand there blabbering!
