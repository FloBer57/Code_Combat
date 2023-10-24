# An ARRAY is a list of items.

# This array is a list of your friends' names.
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# Array indices start at 0, not 1!
friendIndex = 0

# Loop over each name in the array.
# The len() function gets the length of the list.
while friendIndex < len(friendNames):
    # Use square brackets to get a name from the array.
    friendName = friendNames[friendIndex]
    
    # Tell your friend to go home.
    # Use + to connect two strings.
    hero.say(friendName + ', go home!')
    friendIndex += 1
    # Increment friendIndex to get the next name.
    
  

hero.buildXY("fence", 30, 30)  
# Retreat to the oasis and build a "fence" on the X.
