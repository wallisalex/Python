#Alex Wallis
#Python 3.9.x

from sys import base_exec_prefix


def main():

    FORGERYCOEFFICIENT = [0,0,0,0,0,0,0,0,0,0]
    
    def BenfordCalc(fileName): #this function open the files and reads it for values and puts them in a list to be analyzed
        BaseTenCount=[0,0,0,0,0,0,0,0,0] #1,2,3,4,5,6,7,8,9
        EmpiricalProbability=[0,0,0,0,0,0,0,0,0] 
        BenfordProbability=[0.301,0.176,0.124,0.097,0.079,0.076,0.058,0.051,0.046]
        BefordOffset=[0,0,0,0,0,0,0,0,0] 
        tempCounter = 0
        numberOfEntries = 0
        BENSUM = 0

        inHandle = open(fileName, "r") #opening the file for read 
                            
        for line in inHandle.readlines(): #goes through all the lines and splits them, then assigns them positions in the new 2D array
            cord = (line.split()) #splits the line into seperate strings, so you can assign the varible to the proper position
            countX = cord[0][0] #checks the first index's first character  
            countX = int(countX) - 1 
            tempCounter =  BaseTenCount[int(countX)]  #sets a temp variable equal CountX's value
            tempCounter += 1 #temp variable counts up
            numberOfEntries  += 1 #calulating total entries in list
            BaseTenCount[int(countX)] = tempCounter #
            tempCounter = 0 #resets the temp counter so the loops doesnt break

        for i in range(len(BaseTenCount)): #loop though the indexs to calculate emp prob for each set of numbers
            EmpiricalProbability[i] = BaseTenCount[i] / numberOfEntries
            EmpiricalProbability[i] = abs(round(EmpiricalProbability[i],3))

        for i in range(len(EmpiricalProbability)): #looping to calculate the benford offset of the numbers
            BefordOffset[i] = EmpiricalProbability[i] -BenfordProbability[i] 
            BefordOffset[i] = abs(round(BefordOffset[i],3))
        
        for i in range(len(BefordOffset)): #calculating the total sum of the offsets of that dataset 
            BENSUM += BefordOffset[i]
        
        print(str(numberOfEntries) + " integer elements were encountered and analyzed in: ") #prints the counting variable
        print(fileName) #prints the name of the input file
        print("FREQUENCY TOTALS")
        #prints the number frequency for the current dataset 
        print("FREQ_01 =   " + str(BaseTenCount[0]) + ", " +"FREQ_02 =  " + str(BaseTenCount[1]) +", " + "FREQ_03 =  " + str(BaseTenCount[2]) +", "+"FREQ_04 =  " + str(BaseTenCount[3]))
        print("FREQ_05 =   " + str(BaseTenCount[4]) + ", " +" FREQ_06 =  " + str(BaseTenCount[5]) +", " + " FREQ_07 =  " + str(BaseTenCount[6]) +", "+" FREQ_08 =  " + str(BaseTenCount[7]))
        print("FREQ_09 =   " + str(BaseTenCount[8]))
        print()
        print("RELATIVE FREQUENCY TOTALS")
        #prints the RELATIVE FREQUENCY for the current dataset 
        print("RELA_01 =   " + str(EmpiricalProbability[0]) + ", " +"RELA_02 =  " + str(EmpiricalProbability[1]) +", " + "RELA_03 =   " + str(EmpiricalProbability[2]) +", "+"RELA_04 =  " + str(EmpiricalProbability[3]))
        print("RELA_05 =   " + str(EmpiricalProbability[4]) + ", " +"RELA_06 =  " + str(EmpiricalProbability[5]) +", " + "RELA_07 =   " + str(EmpiricalProbability[6]) +", "+"RELA_08 =  " + str(EmpiricalProbability[7]))
        print("RELA_09 =   " + str(EmpiricalProbability[8]))

        print()
        print("BENFORD OFFSET VALUES")
        #prints the BENFORD OFFSET VALUES for the current dataset 
        print("BOFF_01 =   " + str(BefordOffset[0]) + ", " +"BOFF_02 =  " + str(BefordOffset[1]) +", " + "BOFF_03 =   " + str(BefordOffset[2]) +", "+"BOFF_04 =  " + str(BefordOffset[3]))
        print("BOFF_05 =   " + str(BefordOffset[4]) + ", " +"  BOFF_06 =  " + str(BefordOffset[5]) +", " + "BOFF_07 =   " + str(BefordOffset[6]) +", "+"BOFF_08 =  " + str(BefordOffset[7]))
        print("BOFF_09 =   " + str(BefordOffset[8]))
        BENSUM = abs(round(BENSUM,3))
        print("The sum of the Benford Offsets is: " + str(BENSUM))
        
        return BENSUM

    print()  
    for i in range(10):
        BENSUM = BenfordCalc("P02_DataFile_" + str(i) + ".dat") #FIGURED OUT RETURN VARIABLES
        FORGERYCOEFFICIENT[i] = BENSUM
       
        print()
    
    print()
    print("FILE NAME           | Forgery Coeffecient")
    print("--------------------+---------------------")

    for i in range(10):
        print("P02_DataFile_" + str(i) + ".dat "  +" |  "+ str(FORGERYCOEFFICIENT[i]))   
    
    
main()