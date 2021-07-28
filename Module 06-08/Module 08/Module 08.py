
# IMPORTS
import sys

# GLOBAL CONSTANTS
INPUT_FILE = "A08S-GOLBoardInterfaceData.dat"
NUM_ROWS = 10
NUM_COLS = 10
MARK_LIVE = "L"
MARK_DEAD = "D"

# FUNCTIONS
def main():
    print()
    # create a 2d array that represents the board
    gameBoard = Create2DArray(NUM_ROWS, NUM_COLS)
       
    # populate the board with dead squares to start
    InitializeBoard(gameBoard)
    
    
    # populate the board with live coordinates from the data file
    PopulateBoardFromFile(gameBoard, INPUT_FILE)
    
   
    # display the board to see if everything worked
    DisplayBoard(gameBoard, 0)



def Create2DArray(firstDimensionLength, secondDimensionLength): #this function takes in a value for creating the array 
    #creats the list we plan to return, as a 1D list 
    returnList = []
    
    #this for loops creates the first dimension of indexs based on the firstDimensionLength (global value of 10)
    for x in range(firstDimensionLength):
        returnList.append([]) #returns the appened list with 10 values of 'none'
          
    for x in range(firstDimensionLength): 
        for y in range(secondDimensionLength): #creating the second dimension of indexs based on the secondDimensionLength (global value of 10)
            returnList[x].append(0) #replaces the [] with 0 as a place holder
    
    # return the generated list
    return returnList

def InitializeBoard(board): #takes in the 2D list, will create loop to "scan" the array and populate the cells for death     
       
    for i in range(0,len(board[0])): #goes through every postion in the 2D array, and replaces the 0's with DEAD cells
        for j in range(0, len(board[0])):
            board[i][j] = MARK_DEAD #the board is now populated with DEAD CELLS
 
def PopulateBoardFromFile(board, fileName):
    tempList = []
    data = []
    row,col = [],[]
    
    inHandle = open(fileName, "r") #opening the file for read 
    #lineBuffer = inHandle.readline() #reading the first line in the file 
            
    for line in inHandle.readlines(): #goes through all the lines and splits them, then assigns them positions in the new 2D array
        cord = (line.split())
        row = (cord[0])
        col = (cord[1])
        tempList = [row,col]
        data.append(tempList)

    # pop() can throw error if given index is out of range, so use try / except
    
    for i in range(len(data)):
        try:
            row = data[i][0]
            col = data[i][1]
            board[int(row)][int(col)] = MARK_LIVE
        
        except ValueError:
            print("EXCEPTION: The token '"+ row + "' or ' " + col + " could not be parsed from the data file.")
        
        except IndexError:
            print("EXCEPTION: The coordinate (" + row +", "+ col + ") cannot be accessed on the board.")
    
    
    
    

def DisplayBoard(board, generationLabel):
    print("+---------------------+")
    print("| GENERATION # "+ str(generationLabel)+"      |")
    print("+---------------------+")

    for i in board:
        for j in i:
            print(j + " | ", end='')
        print()



main()