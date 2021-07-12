# Author Alexander Wallis
# Written for Python 3.9.6
#

def Main():

    rectLength = int(input("Please enter a value for the Rectangle's Length: "))
    rectWidth = int(input("Please enter a value for the Rectangle's Width: "))
    
    
    def DrawRect(rH, rW): #rectangle function which takes in varibles for legnth and width 
            x = rH
            y = rW

            for _ in range(x):
                for num in range(1, y + 1):
                    print(num * "*")
                print("")

            print(x)
    
    
    
    
    DrawRect(rectLength,rectWidth)


    
      
        
        








Main()