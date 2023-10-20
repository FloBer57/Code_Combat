# Tu testes sur le terrain une nouvelle unité de combat : le Leurre.
# Construis 4 leurres, puis fais ton rapport à Naria combien tu en as construit.

decoysBuilt = 0
while True:
    coin = hero.findNearestItem()
    
    if coin:
        # Collect the coin!
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    # Chaque leurre coûte 25 Or. Utilise la Pierre Sensorielle en Quartz
    # Pour savoir si tu as plus que 25 Or
    if hero.gold > 25 :
        hero.buildXY("decoy",hero.pos.x, hero.pos.y)
        decoysBuilt = decoysBuilt + 1
        
        # Garde le compte des leurres déjà construits au fur et à mesure que tu les construits.
        
    if decoysBuilt == 4:
        # Sors de la boucle lorsque tu en as construit 4. (mots clef : break signifie casser ; loop signifie boucle)
        break
        pass
    
hero.say("Fini de construire des leurres !")
hero.moveXY(14, 36)
# Va voir Naria et dis lui combien de leurres tu as construit.
hero.say(decoysBuilt)