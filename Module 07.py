
# GLOBALS
FILE_NAME = 'A07S-Genesis.txt'
TEST_FILE = 'TEST'


def main():
    
    with open(FILE_NAME,'r') as f:
        listl = [] #creates list to fill with strings
        for line in f: #for loops strips down the string and breaks it into seperate strings
            strip_lines = line.strip()
            listli = strip_lines.split()
            #print(listli)
            #https://www.w3schools.com/python/python_lists_comprehension.asp 
            listli = [item for item in listli if item.isalpha()] #Return's characters in the string are alphabetic
            listli = [each_string.upper() for each_string in listli] #uses list comprehension to create a new list which coverts all letters to uppercase
            #listli = [each_string.split() for each_string in listli] 
            #Attempting to remove duplicates with comprehension
            
            [listli.append(b) for b in listli if b not in listli]  #https://www.guru99.com/python-howto-remove-duplicates.html

            
            m = listl.append(listli)
        
    listli.sort()
    
    for index in range( len(listli) ):
    
        print (listli[index])
        
        
    

main()