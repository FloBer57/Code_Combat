    # Use an event handler so pet and hero will both run!

def petMove():
    pet.moveXY(51, 21)

# Use pet.on("spawn", petMove) instead of petMove().
# This way your hero and pet will run at the same time.
pet.on("spawn",petMove)# ∆ Replace this with pet.on("spawn", petMove)
hero.moveXY(50, 12)
