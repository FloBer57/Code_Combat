# Attend les ogres, bat-les et récupère l'or.

while True:
    enemies = hero.findEnemies()
    # enemyIndex est utilisé pour itérer sur le tableau d'ennemis.
    enemyIndex = 0
    # tant que enemyIndex est inférieur à len(enemies), c'est-à-dire la longueur du tableau des ennemis
    while enemyIndex < len(enemies):
        # Attaque l'ennemi à enemyIndex
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        # Augmente enemyIndex de un.
        enemyIndex += 1
    coins = hero.findItems()
    # coinIndex est utililsé pour itérer sur le tableau de pièces (coins).
    coinIndex = 0
    while coinIndex < len(coins):
        # récupère une pièce (coin) du tableau de pièces en utilisant coinIndex
        coin = coins[coinIndex]
        # Récupère cette pièce.
        hero.moveXY(coin.pos.x, coin.pos.y)
        # Augmenter coinIndex de un.
        coinIndex += 1
