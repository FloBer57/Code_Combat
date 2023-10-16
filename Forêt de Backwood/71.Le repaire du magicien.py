# Allez à Zsofia et récupérez le numéro secret.
hero.moveXY(18, 20)
zso = hero.findNearestFriend().getSecret()

# Divisez le nombre de Zsofia par 4 pour obtenir le numéro de Mihaly.
#  Allez à Mihaly et dites son numéro magique.
mih = zso / 4
hero.moveXY(30, 15)
hero.say(mih)

#  Divisez le nombre de Mihaly par 5 pour obtenir le nombre de Beata
#  Allez à Beata et dites son numéro magique.
bea = mih/5
hero.moveXY(42,20)
hero.say(bea)

san = mih - bea
hero.moveXY(38, 37)
hero.say(san)
#  Soustrayez le numéro de Beata de Mihaly pour obtenir le numéro de Sandor.
#  Allez à Sandor et dites son numéro magique.
