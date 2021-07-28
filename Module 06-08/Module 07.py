

# GLOBALS
INPUT_FILE = 'A07S-Genesis.txt'
OUTPUT_FILE = 'A07S-Genesis-Sorted.txt'


def main():

    #creates list to fill with strings found in the file 
    listOfWords = []

    inHandle = open(INPUT_FILE, "r") #opening the file for read 

    lineBuffer = inHandle.readline() #reading the first line in the file 
    
    #using the idea from Module 06 to read through all the lines of the file
    while lineBuffer != "":
        splitStrings = lineBuffer.split()  # split the strings located in the line inputed 
        
        #splits the string in seperate strings 
        for index in range( len(splitStrings) ):
            splitStrings[index] = exportWord(splitStrings[index])
           

            if splitStrings[index] not in listOfWords: #determines if the string is already in the sortedList, if not add it 
                if splitStrings[index] != "": #if the string is also not a blank, then append the postion and add the new string
                    listOfWords.append(splitStrings[index])

        #reads in the next line
        lineBuffer = inHandle.readline() 

    inHandle.close() #stops the reading of the file

    listOfWords.sort() #sorts the unsorted list from A-Z                    listOfWords = listOfWords.sort() cause the program to crash
    
    outHandle = open(OUTPUT_FILE, 'w') #Creating a new file for the sorted words to write to

    #takes the words from the sorted list and writes them to the file

    for element in listOfWords:
        outHandle.write(element + '\n') #takes the elements in the list and prints them line by line and creates a new line per element

    outHandle.close() #stops writing to the file

#creating functions to do the hard work for me rather than over complicating it

def exportWord(inputString):
    
    if str(inputString).isalpha(): #if the input string contains numbers leave it be 
        inputString = str(inputString).upper()   #makes all the letters in the string uppercase #added the (str) to fix the error 

        exportString = inputString #sets the export string equal the the 

        return str(exportString) #ensures the exportString is actually a string when returning

    else:   
        return "" #return a blank which will not be added to the final list

        
main()


    