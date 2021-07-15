# Author Alexander Wallis
# Written for Python 3.9.6
#

def Main():

    rectLength = int(input("Please enter a value for the Rectangle's Length: ")) #user input for rectangle
    rectWidth = int(input("Please enter a value for the Rectangle's Width: "))
    
    triHeight = int(input("Please enter a value for the Triangles height: ")) #user input for right triangle

    pyraBase = int(input("Please enter a value for the pyramids base: ")) #pyramid base
    
    def DrawRect(rH, rW): #rectangle function which takes in varibles for legnth and width 
        x = rH #converting user input to temp varibles 
        y = rW
                
        print("Displaying a " + str(x) + " x " + str(y) + " rectangle.") #outputing the size and type of shape

        print("") 

        for i in range(x):  #
            print("* " * y) #prints list based on user input 
        
        print("")
        print("")
   
                
    def DrawRtri(tH):

        x = tH #converting user input to temp variable 

        print("Displaying a triangle with a height = " + str(x) ) #outputing the size and type of shape as well as converting temp variable to string
        
        print("")
    
        i = 1 #creating temp variable for while loop, feels like java
        while i <= x : #forming while loop 
            print ("* " * i) #prints a line based on user input
            i += 1 #counts up to make sure loop ends
            
        print("")
        print("")
     

    def DrawPyra(pB):
        x = pB

        print("Displaying a pyramid with base radius = " + str(x))
        print()

        for i in range(x): #nested for loop to create pyramid, x represents row

            for j in range(x - i - 1): #creates number of columns
                print("  ", end ="") #prints spaces 

            for j in range(2 * i + 1): #doubles user input 
                print ("* ", end = "") #ends the line like \n, but allows you to the end print statement with any character/string
            

            print ()
            
    DrawRect(rectLength,rectWidth)
    DrawRtri(triHeight)
    DrawPyra(pyraBase)

    
      
        
        








Main()