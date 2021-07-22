
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
    # create a 2d array that represents the board
    gameBoard = Create2DArray(NUM_ROWS, NUM_COLS)

    # populate the board with dead squares to start
    InitializeBoard(gameBoard)

    # populate the board with live coordinates from the data file
    PopulateBoardFromFile(gameBoard, INPUT_FILE)

    # display the board to see if everything worked
    DisplayBoard(gameBoard, 0)
