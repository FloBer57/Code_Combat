# S'il y a un enemi, attaquez-le.
# Sinon, attaquez le coffre !

while True:
    # Utilisez if/else.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.attack("Chest")
    
    