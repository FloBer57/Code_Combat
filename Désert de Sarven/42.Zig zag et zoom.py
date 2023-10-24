# Échappez-vous de la vallée de la mort!
# Déplacez-vous en zig-zag avec une ( "réelle fonction modulable" ?)

# Cette fonction retourne une valeur de 0 à 15:
def mod15(n):
    while n >= 15:
        n -= 15
    return n

# Cette fonction devrait retourner une valeur de 0 à 9:
def mod9(n):
    # Si "n" est plus grand ou égal à 9, soustraire 9 à "n":
    while n >= 9:
        n -= 9
    return n

# Ne changez pas ce code suivant:
while True:
    time = hero.time
    if time < 30:
        y = 10 + 3 * mod15(time)
    else:
        y = 20 + 3 * mod9(time)
    x = 10 + time
    hero.moveXY(x, y)
