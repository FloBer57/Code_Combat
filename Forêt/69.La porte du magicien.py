# Va vers 'Laszlo' et dis lui son nombre
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# Ajoute 7 au nombre de 'Laszlo' pour obtenir celui d''Erzsebet'
# Va vers 'Erzsebet' et dis lui son nombre
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)


Sim = erz/4
hero.moveXY(30,39)
hero.say(Sim)
# Divise le nombre d''Erzsebet' par 4 pour avoir celui de 'Simonyi'
# Va vers 'Simonyi' et dis lui son nombre
agata = Sim * las 
hero.moveXY(43,26)
hero.say(agata)
# Multiplie le nombre de 'Simonyi' par celui de 'Laszlo' pour obtenir celui d''Agata'
# Va vers 'Agata' et dis lui son nombre

