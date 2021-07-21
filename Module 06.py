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
    # create a file with a random number of random integers
    

    # read the numbers from the file with a while loop
    ReadFileWithWhile()



    # generate the random number file

    GenerateRandomNumberFile(NUM_ELEMENTS)

    # determine the average value in the file

     #elementCount, averageValue = DetermineAverageValue(FILE_NAME)

    # display the results
   

    #print ('There were %d elements found in the file.') % (elementCount)

    #print ('The average value of the elements was determined to be %.3f.') % (averageValue)



def GenerateRandomNumberFile(numberOfElements):
    x = numberOfElements

    # open the file for writing
    outHandle = open(FILE_NAME, 'w')

    # generate random numbers and write them to the file
    for x in range(1, random.randrange(1, x + 1)):
        outHandle.write(str(random.randrange(LOWER_BOUND, UPPER_BOUND)) + '\n')

    # close the file
    outHandle.close()


def ReadFileWithWhile():
    # open the file for reading
    inHandle = open(FILE_NAME, 'r')

    # read the numbers from the file with a while loop
    # priming read
    temp = inHandle.readline()
    temp = temp.rstrip('\n')
    while temp != '':
        # display the number that was read
        print (temp, 'was read from the file.')

        # read the next number.
        # Note: After the last number in the file has been read, the
        #    readline method will return an empty string.  This value
        #    will be used to detect the end of the input file.
        temp = inHandle.readline()
        temp = temp.rstrip('\n')



# Begin MAIN()
main()
