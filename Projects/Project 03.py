# GLOABALS
from sys import base_exec_prefix
import copy
NUM_ROWS = 10 # number of rows on the board

NUM_COLS = 10 # number of columns on the board

MARK_LIVE = "*" # the symbol displayed on the board

# for a living cell

MARK_DEAD = " " # the symbol displayed on the board

# for a dead cell

INPUT_FILE = "P03S-StartingState.dat" # input file name

# MAIN

def main():

	# make an empty 2D array

	board = Create2DArray(NUM_ROWS, NUM_COLS)

	# initialize the Game Board (ALL DEAD)

	InitializeBoard(board)

	# load the board data from a file (COME TO LIFE)

	print ("Reading Data From Input File (%s)" % (INPUT_FILE))

	PopulateBoardFromFile(board, INPUT_FILE)

	# get generation count from the user

	desiredGenerations = input("How many generations to simulate: ")

	for count in range(int(desiredGenerations)):

		DisplayBoard(board, count)

		board = GenerationalShift(board)



def Create2DArray(rows, columns): #this function takes in a value for creating the array 
    #creats the list we plan to return, as a 1D list 
    returnList = []
    
    #this for loops creates the first dimension of indexs based on the firstDimensionLength (global value of 10)
    for x in range(rows):
        returnList.append([]) #returns the appened list with 10 values of 'none'
          
    for x in range(rows): 
        for y in range(columns): #creating the second dimension of indexs based on the secondDimensionLength (global value of 10)
            returnList[x].append(0) #replaces the [] with 0 as a place holder
    
    # return the generated list
    return returnList

def InitializeBoard(board): #takes in the 2D list, will create loop to "scan" the array and populate the cells for death     
       
    for i in range(0,len(board[0])): #goes through every postion in the 2D array, and replaces the 0's with DEAD cells
        for j in range(0, len(board[0])):
            board[i][j] = MARK_DEAD #the board is now populated with DEAD CELLS
 
def PopulateBoardFromFile(board, fileName): 
    tempList = [] #creating local variables to alter list
    data = []
    row,col = [],[]
    
    inHandle = open(fileName, "r") #opening the file for read 
    
            
    for line in inHandle.readlines(): #goes through all the lines and splits them, then assigns them positions in the new 2D array
        cord = (line.split()) #splits the line into seperate strings, so you can assign the varible to the proper position
        row = (cord[0])
        col = (cord[1])
        tempList = [row,col] #turns temporary 1D list into 2D list 
        data.append(tempList) #appeneding the list, with the templist as a clone 
      
    for i in range(len(data)): #loops through the data as a 2D list, 
        try:
            row = data[i][0] # uses the row and col temp variable again
            col = data[i][1]
            board[int(row)][int(col)] = MARK_LIVE #uses the two temp variables as indexs and sets the positions to alive 
            
        except ValueError:  #when the current value at i index is not an int this errow is thrown
            print("EXCEPTION: The token '"+ row + "' or ' " + col + " could not be parsed from the data file.")
        
        except IndexError: #when the data list legnth is greater than the board length it throws this error
            print("EXCEPTION: The coordinate (" + row +", "+ col + ") cannot be accessed on the board.")
   
def DisplayBoard(board, generationLabel):
    print("+----------------------+")
    print("| GENERATION # "+ str(generationLabel)+"       |") #sets up formating
    print("+----------------------+")
 
    for i in board: #loops through rows
        for j in i: #loops through columns
            print("",j, "|", end='') #every time j loops it prints this
        print("\n"+"---+---+---+---+---+---+---+---+---+----") #every time i loops it prints this
        
def GenerationalShift(board):
    shiftedList = copy.deepcopy(board)
    for x in range(len(board)): #loops through the data as a 2D list   
        for y in range(len(board)):
                ALIVE = int(0)
             
                if board[x][y] == MARK_LIVE: 

                    if board[x - 1][y + 1] == MARK_LIVE: #neighbor 1
                        ALIVE += 1

                    if board[x][y + 1] == MARK_LIVE: #neighbor 2
                        ALIVE += 1
                                                        
                    if board[x + 1][y + 1] == MARK_LIVE: #neighbor 3
                        ALIVE += 1
                                                            
                    if board[x - 1][y] == MARK_LIVE: #neighbor 4
                        ALIVE += 1
                                        
                    if board[x + 1][y] == MARK_LIVE: #neighbor 5
                        ALIVE += 1
                                                            
                    if board[x - 1][y - 1] == MARK_LIVE: #neighbor 6
                        ALIVE += 1
                    
                    if board[x][y - 1] == MARK_LIVE: #neighbor 7
                        ALIVE += 1
                                                                
                    if board[x + 1][y + 1] == MARK_LIVE: #neighbor 8
                        ALIVE += 1
                        
                board[x][y] = ALIVE
                ALIVE = 0

    for x in range(len(shiftedList)): #loops through the data as a 2D list   
        for y in range(len(shiftedList)):             

                if shiftedList[x][y] == MARK_LIVE:

                    if board[x][y] == 1:
                        shiftedList[x][y] = MARK_DEAD
                        #print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                        
                    elif board[x][y] == 4:
                        shiftedList[x][y] = MARK_DEAD
                        #print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                        
                    elif board[x][y] == 5:
                        shiftedList[x][y] = MARK_DEAD
                       # print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                        
                    elif board[x][y] == 6:
                        shiftedList[x][y] = MARK_DEAD
                        #print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                        
                    elif board[x][y] == 7:
                        shiftedList[x][y] = MARK_DEAD
                        #print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                        
                    elif board[x][y] == 8:
                        shiftedList[x][y] = MARK_DEAD
                       # print("The cell at (" + str(x) +", " + str(y)+ ") becomes DEAD as a result of Rule #3")
                    

                if shiftedList[x][y] == MARK_DEAD:
                    if board[x][y] == 3:
                        shiftedList[x][y] = MARK_LIVE
                       
    
    return shiftedList    

def TestGenerationalShift(board):
    #print(board)
    shiftedList = copy.deepcopy(board)
    shiftedList[5][5] = "TEST"
    
    return shiftedList



     
main()