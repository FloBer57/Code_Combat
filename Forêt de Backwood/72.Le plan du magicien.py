# Allez à Eszter et récupérez le numéro secret.
hero.moveXY(16, 32)
esz = hero.findNearestFriend().getSecret()

# Multipliez par 3 et soustrayez 2 pour obtenir le nombre de Tamas.
#  N'oubliez pas d'utiliser des parenthèses pour effectuer des calculs dans le bon ordre.
# Allez à Tamas et dites son numéro magique.
tam = (esz * 3) - 2
hero.moveXY(24, 28)
hero.say(tam)

# Soustrayez 1 et multipliez par 4 pour obtenir le nombre de Zsofi.
# Allez à Zsofi et dites son numéro magique.
zso = ( tam-1 ) * 4 
hero.moveXY(32, 24)
hero.say(zso)
# Ajoutez les nombres de Tamas et Zsofi, puis divisez par 2 pour obtenir le numéro d'Istvan.
# Allez à Istvan et dites son numéro magique.
ist = (tam + zso) / 2
hero.moveXY(40, 20)
hero.say(ist)
#  Ajoutez les nombres de Tamas et Zsofi. Soustrayez le nombre d'Istvan de Zsofi. Multipliez les deux résultats pour obtenir le numéro de Csilla.
# Allez à Csilla et dites son numéro magique.
csi = (tam + zso ) * ( zso - ist )
hero.moveXY(48, 16)
hero.say(csi)
