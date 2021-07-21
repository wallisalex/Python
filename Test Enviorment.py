# Author: Mark Dencler
# Description: This program demonstrates techniques used to read data
#    from arbitrary sized files.

# IMPORTS
import random

# GLOBALS
FILE_NAME = 'W06-05-DataFile.txt'
ELEMENT_CAP = 1000

# FUNCTION DEFINITIONS
def main():
    # create a file with a random number of random integers
    GenerateRandomNumbersFile()

    # read the numbers from the file with a while loop
    #ReadFileWithWhile()

    # read the numbers from the file with a for loop
    ReadFileWithFor()


def GenerateRandomNumbersFile():
    # open the file for writing
    outHandle = open(FILE_NAME, 'w')

    # generate random numbers and write them to the file
    for x in range(1, random.randrange(1, ELEMENT_CAP + 1)):
        outHandle.write(str(random.randrange(1, 10001)) + '\n')

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

def ReadFileWithFor():
    # open the file for reading
    inHandle = open(FILE_NAME, 'r')

    # read the numbers from the file with a for loop
    for temp in inHandle:
        temp = temp.rstrip('\n')
        print (temp, 'was read from the file.')
    

# Begin MAIN()
main()
