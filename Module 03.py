# Author Alexander Wallis
# Written for Python 3.9.6
#
# In Python, there is support for the following quantitative comparison
# operations (same operators used by C/C++):
# Less Than - <
# Less Than or Equal To - <=
# Greater Than - >
# Greater Than or Equal To - >=
# Equal To - ==
# Not Equal To - !=

global x,y #global variables to store data
x = 5
y = 0

def main():
       
    sNum = int(input("Please enter a secret number: ")) #takes in input for the secret number 

    def ClearScreen(): #clear screen function found in assignment directions
        clear = ('\n' * 40)
        print(clear)


    def GuessNum(): #function takes in input from user, uses global variable to count down from 5 guesses, determines is the guess is great than, less than, or equal to the secret number
        guess = int(input("Try to guess the secret number: "))
        y = guess
        global x
        if  sNum < y:
            print("The secret number is less than " + str(y) + '\n')
            x = x -1
         
        if sNum > y:
            print("The secret number is greater than " + str(y)+ '\n')
            x = x -1
           
        if sNum == y:
            print("You got it !! " + '\n')
            print("Congratulations... the secret number was " + str(y) + '\n')
            print("YOU WIN... GAME OVER")
            x = -1
                           
    ClearScreen()
    #not using loops, but if statements to reach the goal of 5 
    if x > 0: 
        GuessNum()
    if x > 0: 
        GuessNum()
    if x > 0: 
        GuessNum()
    if x > 0: 
        GuessNum()
    if x > 0: 
        GuessNum()
            
    if x == 0: #is user runs out of tries this runs 
        print("Sorry... you wre not able to guess the secret number")
        print("YOU LOSE... GAME OVER" + '\n')
        print("BTW... the secret number was " + (str(sNum)) +"... Better luck next time")


main()
