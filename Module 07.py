

# GLOBALS

FILE_NAME = 'A07S-Genesis.txt'
TEST_FILE = 'this is test.txt'


def main():
       
                        
   with open(FILE_NAME, "r") as new: # opens the file and names the list my_file then splits each line into singular strings
        
           
        temp = new.readline() #setting up read file 
        temp = temp.rstrip('\n')


        while temp != '': #while that keeps repeating if there is not a space
            temp = new.readline()
            str = temp.split()
            
            for index in range(len(str) ):
                if (str[index].isalpha()):
                    str[index] = (str[index].upper())
                    print (str[index])
                



main()