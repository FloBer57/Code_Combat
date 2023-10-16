# Les commandes ci-dessous ne fonctionne que si la condition "If" est vraie (true).
# Modifie toutes les conditions (Si / Alors ; if / else) pour battre ce niveau.

# == signifie "est égale à".
if 1 + 1 + 2 == 3:  # ∆ Make this false.
    hero.moveXY(5, 15)  # Se déplacer vers les mines les plus proches.


if 2 + 3 == 5:  # ∆ Make this true.
	hero.moveXY(15, 40)  # Se déplacer vers la première gemme.

# != signifie "n'est pas égal à".
if 2 + 3 != 4:  # ∆ Make this true.
	hero.moveXY(25, 15)  # Se déplacer vers la seconde gemme.
	
# le signe < signifie "est inférieur à".
if 2 < 3:  # ∆ Make this true.
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)


if False:  # ∆ Make this false.
	hero.moveXY(50, 10)

if True:  # ∆ Make this true.
	hero.moveXY(55, 25)
