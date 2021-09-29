import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

def introStory():
    # let's introduce them to our world
    print ("Welcome to Vegas!")
    input("Please enter your name >")
    input("Set your Bet: $")


    #pcmd = input("please choose yes to start the Blackjack>")
        
introStory()
def rollDice(minNum, maxNum):
    # any time a chance of something might happen, let's roll a die
    playerresult = random.randint(minNum,maxNum)
    computerresult = random.randint(minNum,maxNum)

    print("Player rolling the dice......")
    print (playerresult)
    print("Computer rolling the dice......")
    print (computerresult)

    if (playerresult > computerresult):
        print ("Player goes first")
    if(playerresult <= computerresult):        
       rollDice(0, 6)

        #input("press enter >")
        #rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return playerresult

rollDice(0 , 6)
 
def poke ():
    input("choose Yes to reveal your first card:")
    playercardNumber1 = random.randint(7,13)
    print (playercardNumber1)
    computercardNumber1 = random.randint(7,13)
    print ("Computer is" )
    print (computercardNumber1)
    input("choose Yes to reveal your second card:")
    playercardNumber2 = random.randint(7,13)
    print (playercardNumber2)
    computercardNumber2 = random.randint(7,13)
    print ("Computer get second card")
    input ("Player choose to Hit again or Stand:" )
   
    player =   (playercardNumber1 + playercardNumber2)
    computer =  (computercardNumber1 + computercardNumber2)

    if ( player < computer):
        print("computerwins")

    if (player > computer):
        print ("player wins")
        
    if (player == computer):
        print("press return")

poke ()
