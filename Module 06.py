# Author Alexander Wallis
# Written for Python 3.9.6

# IMPORTS

import random

# GLOBALS

FILE_NAME = 'A06S-DataFile.dat' # the name of the file in which to write the data

LOWER_BOUND = 0 # the lowest number that can go in the data file

UPPER_BOUND = 10000 # the highest number that can go in the data file

NUM_ELEMENTS = 1000

def main():

    # generate the random number file

    GenerateRandomNumberFile(NUM_ELEMENTS)
    test()

    # determine the average value in the file

    elementCount, averageValue = DetermineAverageValue(FILE_NAME)

    # display the results

    print ('There were %d elements found in the file.') % (elementCount)

    print ('The average value of the elements was determined to be %.3f.') % (averageValue)

def GenerateRandomNumberFile(numberOfElements):

    outHandle = open('A06S-DataFile.dat', 'w')

    rand = random.rand(LOWER_BOUND,UPPER_BOUND)
    print(rand)

    outHandle.close()

def DetermineAverageValue(fileName):

    # IMPLEMENT ME! 
     print

def test():
    inHandle = open('A06S-DataFile.dat', 'r')
    # READ all of the data from the file and store it in a buffer.
    buffer = inHandle.read()

    # display the file contents on the screen
    print (buffer)