# Ce tableau comprend les amis et les ogres
# Les éléments impairs sont des ogres, les éléments pairs sont tes amis
everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul',  'Todd']
enemyIndex = 0

while enemyIndex < len(everybody):
    # Utilise les crochets [ ] pour récupérer le nom des ogres depuis le tableau
    
    hero.attack(everybody[0])
    hero.attack(everybody[2])
    hero.attack(everybody[4])
    # Attaque en utilisant la variable contenant le nom de l'ogre
    
    # Incrémente de 2 pour passer les amis
    enemyIndex += 2

# Après avoir battu les ogres, déplace toi à l'oasis
hero.moveXY(36, 53)
