def main():
     # DELETING THINGS USING SPLICES
 # create a list that contains all of the integers between -10 and 10
    myList = range(-10, 11)
    
    # display the list
    print ("INITIAL LIST:")
    print (myList)
    print ("")
    
    # use a splice to delete all of the negative elements
    del myList[0:10]
    
    # display the list
    print("AFTER DELETING myList[0:10]")
    print (myList)
    print ("")
    
    # use a splice to delete all of the even elements in the list
    del myList[0:11:2]
    
    # display the list
    print ("AFTER DELETING myList[0:11:2]")
    print (myList)
    print ("")
    
    # DELETING THINGS USING THE INDEX METHOD
    # create a list of random letters between A and C
    letterList = ['A', 'C', 'B', 'C', 'A', 'C', 'A', 'B', 'B', 'C', 'A']
    
    # display the list
    print ("INITIAL LETTER LIST:")
    print (letterList)
    print('')
    
    # use the index operator to delete all instances of the letter A
    targetFound = True
    while targetFound == True:
    # assume there are no As left in the array to delete
        targetFound = False
    try:
        deleteIndex = letterList.index('A')
        targetFound = True
        del letterList[deleteIndex]
    
    except ValueError:
        print ("The last instance of 'A' was deleted...")
    
    # display the list
    print ("AFTER DELETING 'A's LETTER LIST:")
    print (letterList)
    print ()
    
    # Begin MAIN()
main()
 