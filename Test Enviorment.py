def main():
    
# make a string that contains multiple words

    manyWordString = "This is a string that has many words in it."

    print ("Before Splitting:")

    print (manyWordString)

    print ("")

# split the string into a list of words

    wordList = manyWordString.split()

# iterate through the wordList with an index to

# visualize what the split function did

    print ("After Splitting:")

    for index in range( len(wordList) ):

        print ("wordList[%2d] contains: %s" % (index, wordList[index]))

main()