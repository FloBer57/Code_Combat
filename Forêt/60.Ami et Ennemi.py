# Paysans et péons se réunissent dans la forêt.
# Dirige les paysans vers la bataille et les péons à s'en aller!

while True:
    friend = hero.findNearestFriend()
    enemy = hero.findNearestEnemy()
    if friend:
        hero.say("Vers la bataille, " + friend.id + "!")
    if enemy : 
        hero.say("Vers la bataille, " + enemy.id + "!")
    