# Ne t'inquiètes pas des ogres de petite et moyenne taille.
# Tes cibles sont de type "brawler".
# Quand un "brawler" est plus proche que 50m, fais tirer l'artillerie.

while True:
    # Trouves l'ennemi le plus proche et sa distance.
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    
    if enemy:
        if enemy.type == "brawler" and distance < 50 : 
            hero.say("Fire!")
            
        
    # si l'ennemi est de type "brawler"
    # ET sa distance doit être inférieure à 50 mètres,
    # Ensuite dites "Fire!" pour signaler à l'artillerie de tirer.
    
    pass
