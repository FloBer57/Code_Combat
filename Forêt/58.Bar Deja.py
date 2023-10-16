# Vous pouvez concaténer des chaînes ensemble, et ajouter des nombres dans des chaînes.
# Chantez, en utilisant la concaténation de chaînes:
# X potions of health on the wall!
# X potions of health!
# Take Y down, pass it around!
# X-Y potions of health on the wall.

potionsOnTheWall = 10
numToTakeDown = 1
while True:
    hero.say(potionsOnTheWall + " potions of health on the wall!")
    # Chantez la ligne suivante:
    hero.say(potionsOnTheWall + " potions of health")
    # Chantez la ligne suivante:
    hero.say("take" + numToTakeDown + " down, pass it around!")
    potionsOnTheWall = potionsOnTheWall - numToTakeDown
    hero.say(potionsOnTheWall + " potions of health on the wall!")
