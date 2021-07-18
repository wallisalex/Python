# Author Alexander Wallis
# Written for Python 3.9.6
# Pico Centro 

a = 0
b = 1 
c = 2

pica = 0
centro = 0 

def Clear(): #clear screen function
    clear = ('\n' * 40)
    print(clear)

def main():
    
    pica = 0
    centro = 0 
        
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

    print("Guess #01")
    gA = int(input("Please enter the first digit in your guess : "))
    gB = int(input("Please enter the seccond digit in your guess : "))
    gC = int(input("Please enter the third digit in your guess : "))
    print()

    print("+--------------------------------------+")
    print("| YOUR GUESS     | PICA  | CENTRO      |")
    print("+--------------------------------------+")
    print("| "+ str(gA) +" " + str(gB) +" "+ str(gC)+"         "  +  " |       |            |")
    print("+--------------------------------------+")
    print()

        # is pGuess1 a pica or centro?

    if gA == a:

        centro += 1

    elif a == gB:

        pica += 1

    elif a == gC:

        pica += 1


        
   







main()

