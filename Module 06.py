#Author Alexander Wallis
#Written for Python 3.9.6

# IMPORTS
import random

# GLOBALS

FILE_NAME = 'A06S-DataFile.dat' # the name of the file in which to write the data

LOWER_BOUND = 0 # the lowest number that can go in the data file

UPPER_BOUND = 10000 # the highest number that can go in the data file

NUM_ELEMENTS = 1000

# FUNCTION DEFINITIONS
def main():
    
    # generate the random number file

    GenerateRandomNumberFile(NUM_ELEMENTS)

    # determine the average value in the file

    elementCount, averageValue = DetermineAverageValue(FILE_NAME)

    # display the results
   

    #print ('There were %d elements found in the file.') % (elementCount)
    print("There were " + str(elementCount) + " elements found in the file.")

    #print ('The average value of the elements was determined to be %.3f.') % (averageValue)
    print("The average value of the elements was determined to be " + str(averageValue))

    #DetermineAverageValue(FILE_NAME)



def GenerateRandomNumberFile(numberOfElements):
    x = numberOfElements

    # open the file for writing
    outHandle = open(FILE_NAME, 'w')

    # generate random numbers and write them to the file
    for x in range(1, x + 1):
        outHandle.write(str(random.randrange(LOWER_BOUND, UPPER_BOUND)) + '\n')

    # close the file
    outHandle.close()


def DetermineAverageValue(filename):
    x = filename

    # open the file for reading
    inHandle = open(x, 'r')

    # read the numbers from the file with a while loop

    total = 0
    elementCount = 0
    temp = inHandle.readline()
    temp = temp.rstrip('\n')
    

    while temp != '':
        elementCount += 1
        total = total + int(temp)
        temp = inHandle.readline()

    averageValue = total / float(elementCount)

    return int(elementCount),float(averageValue)
    #print("Avg: " + str(averageValue) +" ele: " + str(elementCount))

# Begin MAIN()
main()

