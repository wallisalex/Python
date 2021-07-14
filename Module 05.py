# Author Alexander Wallis
# Written for Python 3.9.6
#

global x,y #global variables to store data
x = 5
y = 0

import random

def main():

    def getGuess(): #function with return

        a = int(input("Take a guess at the secret number:"))
        return a #returns value from function

    def DifandGuess(difficulty:int): #function with multiple returns
        
        difRange=[25,100,1000] #ranges coresponding to difficulty
        guesses=[5,8,12] #guesses coresponding to difficulty HAD TO USE [] BECAUES () would not work
        
        return difRange[difficulty-1],guesses[difficulty-1]; # returning multiple values and subtracting 1 because python list starts at 0 
           
    def guessingGame(): #setting up game function

        #STOP = 1001 #creates loops that repeats unless a user enters valid number
        #while STOP != 0: 
        #no longer using while loop to loop through list, only keeping it for documentation

            print("Welcome to GUESS MY NUMBER... Please select a difficulty :"); #prints diffuclty options as a clean menu

            print("1.) Easy   (Number Range: 1-25   ; Guesses: 5 ) ");

            print("2.) Medium (Number Range: 1-100  ; Guesses: 8 ) ");

            print("3.) Hard   (Number Range: 1-1000 ; Guesses: 12) ");

            difficulty = int(input(": ")) #collects user input for difficulty and calls from funbncitonearlier
        
            print("The secret number has been generated... the game has begun.\n")

            difRange,guesses = DifandGuess(difficulty) #runs multiple return function with user input to return coresponding values

            rand=random.randint(0,difRange) #generates random number based on user input between 1 and X 

            #GUESS LOOP TIME

            for i in range(0,guesses): #loops until guesses run out or number is guessed
                guess = getGuess() #calling the return variable from funciton above 

                if guess == rand:
                    print("You have successfully guessed the secret number. Horray for you.")
                    print("YOU WIN!!!")
                    i = 0 #breaks loop/could have used break?

                else:
                    if guess > rand:
                        print("The secret number is lower than " + guess)
                    else:
                        print("The secret number is greater than " + guess)

                print("You have " + guesses + " left...")



    guessingGame()


main()