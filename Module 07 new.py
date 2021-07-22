
# GLOBALS
FILE_NAME = 'A07S-Genesis.txt'
TEST_FILE = 'TEST'


def main():
    
    with open(FILE_NAME,'r') as f:
        listl = []
        for line in f:
            strip_lines = line.strip()
            listli = strip_lines.split()
           # print(listli)
            m = listl.append(listli)
        #print(listl)
        
    for index in range( len(listl) ):
            print ("wordList[%2d] contains: %s" % (index, listl[index]))

main()