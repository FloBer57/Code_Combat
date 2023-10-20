# Récolte 25 pièces d'or et indique à Naria le total.
# Utilise l'instruction break pour arreter de récolter les pièces quand totalGold >= 25

totalGold = 0
while True:
    coin = hero.findNearestItem()
    if coin:
        # Pick up the coin.
        hero.moveXY(coin.pos.x, coin.pos.y)
        
        totalGold = totalGold + coin.value
        
        # Add the coin's value to totalGold
        # Permet d'obtenir la valeur :  coin.value
        
        pass
    if totalGold == 25:
        # Permet d'arrêter la loop pour exécuter le code en dessous
        # The loop ends, code after the loop will run.
        break

# Fin de la récolte d'or !
hero.moveXY(58, 33)
# Aller voir Naria et dis lui combien d'or tu as recolté
hero.say(totalGold)
