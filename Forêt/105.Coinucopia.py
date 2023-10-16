# Appuyez sur Envoyer quand vous êtes prêt à placer les drapeaux.
# Les boutons drapeau apparaissent dans le coin inférieur gauche après avoir appuyé sur Envoyer.
while True:
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    else:
        hero.say("Placez un drapeau pour que je m'y rende.")
    