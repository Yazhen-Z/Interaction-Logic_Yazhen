#Assignment3

print ("Welcome to Garden in the Sky")
print ("Please answer the questions to recive your own plant.")
print ("Here is the enternce")

# variables containing all of your story info
Plante1 = raw_input("If you are walking in the desert, which plante do you expect to appear in front of you?: ")
color1 = raw_input("What is your favorite color?: ")
Flower1 = raw_input("How many flowers do you want?: ")
object1 = raw_input("What's your favorite material?: ")
Scale1 = raw_input("How big you want your plante to be?:")
Name1 = raw_input("Give your plante a name: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "You are in the entrance of the garden of sky, and" + Plante1 + " is your subconscious representation. It is " + color1 + " with " + Flower1 + " beautiful flowers. " \
"The size is " + Scale1 + " and the whole plante is made by " + object1 + ". " \
"Congratulations on getting your plant: " + Name1 + " Come and plant it in the garden of sky!" 

# finally we print the story
print (story)