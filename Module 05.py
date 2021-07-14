# Author Alexander Wallis
# Written for Python 3.9.6
#

import random

def main():

    def getGuess(): #function with return

        a = int(input("Take a guess at the secret number:"))
        return a #returns value from function

    def DifandGuess(difficulty:int): #function with multiple returns
        
        difRange=[25,100,1000] #ranges coresponding to difficulty
        guesses=[5,8,12] #guesses coresponding to difficulty HAD TO USE [] BECAUES () would not work
        
        return difRange[difficulty-1],guesses[difficulty-1]; # returns value in list depending on input. -1 becaues python starts counting from 0
           
    def guessingGame(): #setting up game function

        #STOP = 1001 #creates loops that repeats unless a user enters valid number
        #while STOP != 0: 
        #no longer using while loop to loop through list, only keeping it for documentation

            print("Welcome to GUESS MY NUMBER... Please select a difficulty :"); #prints diffuclty options as a clean menu

            print("1.) Easy   (Number Range: 1-25   ; Guesses: 5 ) ");

            print("2.) Medium (Number Range: 1-100  ; Guesses: 8 ) ");

            print("3.) Hard   (Number Range: 1-1000 ; Guesses: 12) ");

            difficulty = int(input(": ")) #collects user input for difficulty and calls from funbnciton from earlier
            difRange,guesses = DifandGuess(difficulty) #runs multiple return function with user input to return coresponding values
            rand=random.randint(0,difRange) #generates random number based on user input between 1 and X 

            print("The secret number has been generated... the game has begun.\n") #lets the user know the game is ready 
                       
            #GUESS LOOP TIME

            for i in range(0,guesses): #loops until guesses run out or number is guessed
                guess = getGuess() #calling the return variable from funciton above 
               
                if guess == rand: #if the guess is the same as the random number the user wins
                    print()
                    print("You have successfully guessed the secret number. Horray for you.")
                    print("YOU WIN!!!")
                    i = 0 #breaks loop/could have used break?

                if guess != rand: #could have used else?
                    if guess > rand: #checks if the users guess is greather than the number
                        guesses = guesses -1
                        print("The secret number is lower than " + str(guess))
                        print()
                        
                    if guess < rand: #checks if the users guess is greather than the number
                        guesses = guesses -1
                        print("The secret number is greater than " + str(guess))
                        print()

                    if guesses != 0:
                        print("You have " + str(guesses) + " left...")      #printed "you have zero guesses left" so i hard coded it out
                        
                
                if guesses == 0: #once the gueses counter tallies down, print that
                    print("You poor sap.. You didn't get the secret number in the allowed")
                    print("number of guesses. Better luck next time loser!")
                    print("YOU LOSE!!!")
                    print("BTW... The secret number was " + str(rand))
                    print()                    


    guessingGame()


main()