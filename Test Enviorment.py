temp = new.readline() #setting up read file 
    temp = temp.rstrip('\n')
    

    while temp != '': #while that keeps repeating if there is not a space left in the list 
        elementCount += 1 #counter to print number of lines
        total = total + int(temp)
        temp = new.readline()