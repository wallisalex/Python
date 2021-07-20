# Author Alexander Wallis
# Written for Python 3.9.6
# Pico Centro 

a = 0
b = 1 
c = 2

pica = 0
centro = 0 

guess1 = 0
guess2 = 0
guess3 = 0

counter = 10

def Clear(): #clear screen function
    clear = ('\n' * 40)
    print(clear)
 
def main():
    global gA
    global gB
    global gC

    global pica
    global centro

    global a
    global b
    global c

    global counter

    print("+--------------------------------------+")
    print( "|        WELCOME TO PICA-CENTRO        |")
    print ("+--------------------------------------+")

    a = int(input("Please enter the first digit in your number : "))
    b = int(input("Please enter the seccond digit in your number : "))
    c = int(input("Please enter the third digit in your number : "))
       
        #Digits in guess, every digit can be a pica,centro,neither BUT CANT BE BOTH
        #repeat digits
        #ElIf 

    print("The secret number has been set to: " + str(a) + " " + str(b) + " " + str(c))
    input("PRESS ANY KEY TO CLEAR THE SCREEN AND BEGIN THE GAME ")
    Clear()

    for i in range(0,counter): 
        
        print("Guess #" + str(i + 1)) #prints place in for loops +1 since it starts at 0
        guess1 = int(input("Please enter the first digit in your guess : "))
        guess2 = int(input("Please enter the seccond digit in your guess : "))
        guess3 = int(input("Please enter the third digit in your guess : "))
                    
        # is guess1 a pica or centro?
 
        if guess1 == a: #
            centro += 1

        elif guess1 == b: #if previous is not true try this 
            pica += 1

        elif guess1 == c:  #then try this
            pica += 1

        # is guess2 a pica or centro?

        if guess2 == b:
            centro += 1

        elif guess2 == c:
            pica += 1

        elif guess2 == a:
            pica += 1

        # is guess3 a pica or centro?

        if guess3 == c:
            centro += 1

        elif guess3 == a:
            pica += 1

        elif guess3 == b:
            pica += 1

        print("+--------------------------------------+")
        print("| YOUR GUESS     | PICA  | CENTRO      |")
        print("+--------------------------------------+")
        print("| "+ str(guess1) +" " + str(guess2) +" "+ str(guess3)+"         "  +  " |   "+ str(pica) +"    |    " + str(centro) +"       |")
        print("+--------------------------------------+")
        print()
        
        if centro == 3: 
            print("VICTORY!    The secret number was: " + str(a) + " " + str(b) + " " + str(c))
            i = 9
            break #if the user wins the game, break the loop

        if i == 9: #when the for loop ends display this message
            print("YOU LOSE.  You are out of guesses.  The secret number was: " + str(a) + " " + str(b) + " " + str(c))
                 
        pica = 0  #counter for pica and centro are reset to 0 at the start of each turn to prevent infinite counting
        centro = 0
        counter = counter - 1 

       


main()

