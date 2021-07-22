

# GLOBALS

FILE_NAME = 'A07S-Genesis.txt'
TEST_FILE = 'this is test.txt'


def main():
       
                        
   with open(FILE_NAME, "r") as new: # opens the file and names the list my_file then splits each line into singular strings

        temp = new.readline() #setting up read file 
        temp = temp.rstrip('\n')


        while temp != '': #while that keeps repeating if there is not a space
            temp = new.readline() #to make sure the loop goes through the entire list and doesnt print the same line endlessly 
            TheList = temp.split()
            
            for index in range(len(TheList) ):
                if (TheList[index].isalpha()): #checking the list for alphanumeric characters and avoiding numbers
                    TheList[index] = (TheList[index].upper()) #converting strings in list to UPPERCASE letters
                    TheList.sort()
                    
                    print(TheList[index])

                    
                    #myset = set(TheList[index]) # Atempted making a set, couldnt figure it out 
                    #mynewlist = list(myset)
                    
                           
                    
                    
                    
main()