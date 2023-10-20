# This function allows to fight until the certain time
# and report about defeated enemies.
def fightAndReport(untilTime):
    defeated = 0
    while True:
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.attack(enemy)
            if enemy.health <= 0:
                defeated += 1
        if hero.time > untilTime:
            break
    hero.moveXY(59, 33)
    hero.say(defeated)


def collectAndReport(untilTime):
    money = 0
    while True:
        coin = hero.findNearestItem()
        if coin:
            hero.moveXY(coin.pos.x, coin.pos.y)
            money += coin.value
        if hero.time > untilTime:
            break
    hero.moveXY(59, 33)
    hero.say(hero.gold)
    
    
    
# Fight 15 seconds and tell Naria how many enemies you defeated.
fightAndReport(15)

# Collect coins until the clock reaches 30 seconds.
collectAndReport(30)

# Tell Naria how much gold you collected.
hero.say(hero.gold)

# Fight enemies until the clock reaches 45 seconds.
fightAndReport(45)