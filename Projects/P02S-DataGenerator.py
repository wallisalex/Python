# Author: Mark Dencler
# Description: This program generates data files containing arbitrary
#    numbers of integer values who leading digits conform to the provided
#    probability distribution described in the global constants.

# IMPORTS
import random
import math

# CONSTANTS
EPSILON = 0.000001         # used to compare near zero floats
ELEMENTS_PER_FILE = 10000  # the number of elements to spawn in each file
CUSTOM_FILE_LAST = False   # flag that indicates if the custom file should be
                           # the last file made or hidden among the other
                           # data files

# Probabilities provided by Benford's Law for base-10 integers.
BENFORD_P_01 = 0.301
BENFORD_P_02 = 0.176
BENFORD_P_03 = 0.125
BENFORD_P_04 = 0.097
BENFORD_P_05 = 0.079
BENFORD_P_06 = 0.067
BENFORD_P_07 = 0.058
BENFORD_P_08 = 0.051
BENFORD_P_09 = 0.046

# Custom Probability Table (for making unnatural data)
CUSTOM_P_01 = 0.200
CUSTOM_P_02 = 0.200
CUSTOM_P_03 = 0.100
CUSTOM_P_04 = 0.100
CUSTOM_P_05 = 0.050
CUSTOM_P_06 = 0.050
CUSTOM_P_07 = 0.100
CUSTOM_P_08 = 0.200
CUSTOM_P_09 = 0.000

# MAIN
def main():
    # determine that the provided probability distributions are valid
    if ValidateProbabilityTables() == False:
        print ('The probability tables are bad.  Terminating program.')
        return False

    # use the CUSTOM_FILE_LAST flag to determine where the fraudulent file
    # should be generated in relation to the other data files
    if CUSTOM_FILE_LAST == True:
        # generate 9 Benford Probability compliant files
        for x in range(0, 9):
            fileName = 'P02_DataFile_' + str(x) + '.dat'
            GenerateBenfordFile(fileName)

	# generate 1 Custom Probability compliant file
        fileName = 'P02_DataFile_' + str(9) + '.dat'
        GenerateCustomFile(fileName)
    elif CUSTOM_FILE_LAST == False:
        # generate somewhere between 0 and 8 Benford Probability
        # compliant files
        x = 0
        for x in range(0, random.randint(0, 8)):     
            fileName = 'P02_DataFile_' + str(x) + '.dat'
            GenerateBenfordFile(fileName)

        # generate a single Custom Probability compliant file
        if x != 0:
            x += 1
        fileName = 'P02_DataFile_' + str(x) + '.dat'
        GenerateCustomFile(fileName)
        x += 1

        # generate the rest of the Benford Probability
        # compliant files
        for y in range(x, 10):
            fileName = 'P02_DataFile_' + str(y) + '.dat'
            GenerateBenfordFile(fileName)

    # exit the program
    return True


def ValidateProbabilityTables():
    # assume the discrete probability distributions are invalid
    benfordCheckout = False
    customCheckout = False

    # determine the totals of each distribution
    benfordTotal = BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + BENFORD_P_04 + \
                   BENFORD_P_05 + BENFORD_P_06 + BENFORD_P_07 + BENFORD_P_08 + \
                   BENFORD_P_09
    customTotal =  CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + CUSTOM_P_04 + \
                   CUSTOM_P_05 + CUSTOM_P_06 + CUSTOM_P_07 + CUSTOM_P_08 + \
                   CUSTOM_P_09

    # verify the provided benford probabilities form a valid distribution
    if abs(benfordTotal - 1.0) < EPSILON:
           benfordCheckout = True
    else:
        print ('ERROR: The provided Benford Probabilities do not create a valid')
        print ('discrete probability distribution.')
        print ('')

    # verify the provided custom probabilities form a valid distribution
    if abs(customTotal - 1.0) < EPSILON:
           customCheckout = True
    else:
        print ('ERROR: The provided Custom Probabilities do not create a valid')
        print ('discrete probability distribution.')
        print ('')

    if benfordCheckout == True and customCheckout == True:
        return True
    else:
        return False


def GenerateRandomLeader(leadingDigit):
    return int(str(leadingDigit) + str(random.randint(0, 999999)))


def GenerateBenfordFile(fileName):
    # open the file
    outHandle = open(fileName, 'w')

    # generate a number with a leading digit based on the provided
    # Benford Probability distribution
    for x in range(0, ELEMENTS_PER_FILE):
        # determine the point in the distribution that a number should be
        # generated from
        uniformLanding = random.random()

        # generate a random integer with the appropriate leading digit
        if uniformLanding <= BENFORD_P_01:
            writeMe = GenerateRandomLeader('1')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02:
            writeMe = GenerateRandomLeader('2')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03:
            writeMe = GenerateRandomLeader('3')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04:
            writeMe = GenerateRandomLeader('4')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04 + BENFORD_P_05:
            writeMe = GenerateRandomLeader('5')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04 + BENFORD_P_05 + BENFORD_P_06:
            writeMe = GenerateRandomLeader('6')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04 + BENFORD_P_05 + BENFORD_P_06 + \
                               BENFORD_P_07:
            writeMe = GenerateRandomLeader('7')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04 + BENFORD_P_05 + BENFORD_P_06 + \
                               BENFORD_P_07 + BENFORD_P_08:
            writeMe = GenerateRandomLeader('8')
        elif uniformLanding <= BENFORD_P_01 + BENFORD_P_02 + BENFORD_P_03 + \
                               BENFORD_P_04 + BENFORD_P_05 + BENFORD_P_06 + \
                               BENFORD_P_07 + BENFORD_P_08 + BENFORD_P_09:
            writeMe = GenerateRandomLeader('9')

        # write the generated value to the data file
        outHandle.write( str(writeMe) + '\n' )

    # close the data file
    outHandle.close()

    # display a message indicating the type of file that was made
    print ('"' + fileName + '"' + ' was created.  BENFORD')
    

def GenerateCustomFile(fileName):
    # open the file
    outHandle = open(fileName, 'w')

    # generate a number with a leading digit based on the provided
    # Custom Probability distribution
    for x in range(0, ELEMENTS_PER_FILE):
        # determine the point in the distribution that a number should be
        # generated from
        uniformLanding = random.random()

        # generate a random integer with the appropriate leading digit
        if uniformLanding <= CUSTOM_P_01:
            writeMe = GenerateRandomLeader('1')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02:
            writeMe = GenerateRandomLeader('2')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03:
            writeMe = GenerateRandomLeader('3')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04:
            writeMe = GenerateRandomLeader('4')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04 + CUSTOM_P_05:
            writeMe = GenerateRandomLeader('5')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04 + CUSTOM_P_05 + CUSTOM_P_06:
            writeMe = GenerateRandomLeader('6')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04 + CUSTOM_P_05 + CUSTOM_P_06 + \
                               CUSTOM_P_07:
            writeMe = GenerateRandomLeader('7')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04 + CUSTOM_P_05 + CUSTOM_P_06 + \
                               CUSTOM_P_07 + CUSTOM_P_08:
            writeMe = GenerateRandomLeader('8')
        elif uniformLanding <= CUSTOM_P_01 + CUSTOM_P_02 + CUSTOM_P_03 + \
                               CUSTOM_P_04 + CUSTOM_P_05 + CUSTOM_P_06 + \
                               CUSTOM_P_07 + CUSTOM_P_08 + CUSTOM_P_09:
            writeMe = GenerateRandomLeader('9')

        # write the generated value to the data file
        outHandle.write( str(writeMe) + '\n' )

    # close the data file
    outHandle.close()

    # display a message indicating the type of file that was made
    print ('"' + fileName + '"' + ' was created.  CUSTOM')
        
        
# Begin MAIN()
main()
