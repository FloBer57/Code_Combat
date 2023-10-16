# The ogres are holed up in their camp
# Break through their defenses with a calculated strike!

hero.moveXY(55, 14)
hero.moveXY(92, 9)

# Construis un piège-de-feu ("fire-trap") sur la croix rouge.
hero.buildXY("fire-trap", 94, 19)
# Recule vers la croix de bois pour éviter l'onde de choc.
hero.moveXY(56, 14)
# Attends que le péon vienne enquêter sur ton piège de feu flambant neuf.
# Entre dans le camp et pose des pièges de feu sur chaque croix rouge.
hero.buildXY("fire-trap", 90, 53)
hero.buildXY("fire-trap", 60, 62)
# Crie à tes troupes de se retirer ( conseil : Utilise say (qui signifie 'dire', 'Retreat!') )
hero.say("Retreat!")
# Enfuis-toi en revenant à l'extrême gauche de la carte, sur le point de ralliement signalé par une croix de bois.
hero.moveXY(10, 29)
