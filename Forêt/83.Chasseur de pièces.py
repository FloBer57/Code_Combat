# To make the training more interesting Senick poisoned you.
# While you aren't moving the poison is harmless.

# This function should check if a coin is closer than 20m.
def isCoinClose(coin):
    # Find the distance to the `coin`.
    item = hero.findNearestItem()
    distance = hero.distanceTo(item) 
    if distance < 20 : 
        return True 
    else:
        return False
    # Si la distance est inférieure à 20 :
    
        # Return True
        
    # Else:
    
        # Return False
        
    pass

while True:
    item = hero.findNearestItem()
    if item:
        # If isCoinClose(item) returns true:
        if isCoinClose(item):
            hero.moveXY(item.pos.x, item.pos.y)
