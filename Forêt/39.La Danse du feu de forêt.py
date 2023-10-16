# Dans ce niveau la pierre du mal est mauvaise! Évitez les, marchez dans l'autre direction.
while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:     # == means "is equal to"
            hero.moveXY(46, 22)
            
            pass
        else:
            hero.moveXY(34, 22)
            
            
            pass
    else:
        hero.moveXY(40,22)
        
        pass
