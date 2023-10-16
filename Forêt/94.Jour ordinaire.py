# Tue les mioches, ramasse les pièces. Comme d'habitude.
# Utilise ET pour vérifier l'existance et le type dans une phrase.

while True:
    enemy = hero.findNearestEnemy()
    # Avec ET, le type est validé seulement si il existe des énemies.
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy)
    # Trouve l'objet le plus proche.
    item = hero.findNearestItem()
    if item and item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y)
    
    # Collecte les objets si il existe et si leurs type est "coin".
    
