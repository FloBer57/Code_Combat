# Tu as été pris dans un piège à loup!
# Envoie ton animal de compagnie récupérer les potions de vie!

def goFetch():
    # Tu peu utiliser des boucles dans une fonction gestionnaire.
    while True:
        potion = hero.findNearestItem()
        if potion:
            pet.fetch(potion)
            
            pass

# Quand ton animal de compagnie est crée, il déclenche l'événement "spawn".
# Cela dit à ton animal de compagnie d'exécuter la fonction goFetch au début du niveau:
pet.on("spawn", goFetch)
