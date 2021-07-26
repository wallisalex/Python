

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
                    #listli = [item for item in listli if item.isalpha()] #Return's characters in the string are alphabetic
                    #listli = [each_string.upper() for each_string in listli] #uses list comprehension to create a new list which coverts all letters to uppercase
            #listli = [each_string.split() for each_string in listli] 
            #Attempting to remove duplicates with comprehension
            
                    [TheList[index].append(b) for b in TheList[index] if b not in TheList[index]]  #https://www.guru99.com/python-howto-remove-duplicates.html

                    #TheList.sort()
                    
                    m = TheList.append(TheList)
                    
                    print(TheList)

                    
                    #myset = set(TheList[index]) # Atempted making a set, couldnt figure it out 
                    #mynewlist = list(myset)
                    
                           
                    
                    
                    
main()