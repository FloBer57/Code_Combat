# Bats les ogres dans leur propre camp !

while True:
    enemy = hero.findNearestEnemy()
    # Utilise un if-statement pour vérifier qu’un ennemi existe :
    if enemy:
        hero.attack(enemy)
        
        # Attaque l’ennemi s’il existe :
        