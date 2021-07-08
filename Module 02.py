#Author Alexander Wallis
#Written for Python 3.9.6
#
import math

def main(): 
    #Cow Data
    cowLength = int(input("Please enter a value for the Cow Length: "))
    cowHeight = int(input("Please enter a value for the Cow height: "))
    #Rhino Data 
    rhinoLength = int(input("Please enter a value for the Rhino Length: "))
    rhinoHeight = int(input("Please enter a value for the Rhino Height: "))
    #Turtle Data
    turtleLength = int(input("Please enter a value for the Turtle Length: "))
    turtleHeight = int(input("Please enter a value for the Turtle Height: "))
    #Bird Data
    birdRadius = int(input("Please enter a value for bird radius: "))

    cPen(cowLength,cowHeight)
    rGround(rhinoLength,rhinoHeight)
    tPetting(turtleLength,turtleHeight)
    bCage(birdRadius)

    print("---------------------------------------------------------------------------")
    #did a big equation instead, coudlnt get variables from functions to work
    #maybe use global variables with scope?

    totalA = round(((cowLength*cowHeight) + (rhinoLength * rhinoHeight) + (turtleLength * turtleHeight) + (3.1415 * (birdRadius**2))),5)
    totalP = round(((cowLength*2) + cowHeight + (rhinoLength*2) + (rhinoHeight * 2) + (turtleLength*2) + turtleHeight + (2 * 3.1415 * birdRadius)),5)
    print ("The TOTAL AREA of all regions is             : " + str(totalA))
    print ("The TOTAL LENGTH of all fences is            : " + str(totalP))
    
  
    print("---------------------------------------------------------------------------")
 

    
def cPen(cL, cH): #cow function with cow variables and calculations
    cArea =  (cL * cH)
    cPer = (cL + cL + cH + cH)
    print ("The area of the Moo Cow Pen is              :" + str(cArea))
    print ("The perimeter of the Moo Cow Pen is         :" + str(cPer))
    


def rGround(rL,rH):#rhino function with rhino variables and calculations 
    rArea = (rL * rH)
    rPer = (rL + rL + rH + rH)
    print("The area of the Rhino Common Ground is       :" + str(rArea))
    print("The perimeter of the Rhino Common Ground is  :" + str(rPer))
    

def tPetting(tL,tH):#turtle function with turtle variables and calculations 
    tArea = (tL * tH)
    tPer = (tL + tL + tH + tH)
    print("The area of the Turtle Petting Area is       :" + str(tArea))
    print("The perimeter of the Turtle Petting Area is  :" + str(tPer))

def bCage(bR): #bird function
    bArea = (3.1415 * (bR**2)) #used 3.1415 instead of math.pi
    bPer = (2 * 3.1415 * bR)
    print("The area of the Bird Cage is                 :" + str(bArea))
    print("The perimeter of the bird cage is            :" + str(bPer))

    #first attempted making a function to call all the other functions but gave in

def tArea(cPen,rGround,tPetting,bCage):
    totalA = 0
    print("The TOTAL AREA of all regions is              :" + str(totalA))

main()