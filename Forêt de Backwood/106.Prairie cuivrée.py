# Ramassez toutes les pièces dans chaque prairie.
# Utilisez les drapeaux pour vous déplacer entre les prairies.
# Cliquez sur Envoyer quand vous êtes prêt à placer les drapeaux.

while True:
    flag = hero.findFlag()
    if flag:
        pass  # 'pass' est un espace réservé, il n'a aucun effet.
        # Pick up the flag.
        hero.pickUpFlag(flag)
    else:
        # Automatically move to the nearest item you see.
        item = hero.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            hero.moveXY(x, y)
