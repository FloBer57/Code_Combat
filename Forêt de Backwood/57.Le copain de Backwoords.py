# Tu as maintenant un animal de compagnie!

def speak(event):
    # Votre animal de compagnie devrait répondre avec pet.say()
    pet.say("Oui")
    pass

# Cela dit à ton animal de compagnie via la fonction speak() quand elle entend quelque chose
pet.on("hear", speak)

# Parles à ton animal de compagnie!
hero.say("Salut Kitty")
