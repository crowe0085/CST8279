import re


def openFile(filePath):
    try:
        return open(filePath, 'r+')
    except Exception as e:
        print(e)


def convertToDictionary(file):
    myDictionary = {}
    for line in file:
        nLine = re.split(' |,', line.strip())
        
        if len(nLine) == 1: # check to see if the new line list has only one element. then check if its a number to see if its the name or count
            if nLine[0].isdigit():
                amount = nLine [0]
                name = 'unkown'
            else:
                name = nLine[0]
                amount = 'unkown'
        else: # if the list has 2 elements then i can properly assign the key pairs
            name = nLine[0]
            amount = nLine[1]
        
        myDictionary[name] = amount

    return myDictionary


def writeToCSV(dictionary, csvName):
    try:
        with open(csvName, 'w') as csvFile:
            csvFile.write('First Names,Count\n')
            for key in dictionary.keys():
                csvFile.write("%s,%s\n" % (key, dictionary[key]))
    except Exception as e:
        print(e)


def main():

    myFile = openFile('2000_BoysNames.txt')
    myFile2 = openFile('2000_GirlsNames.txt')

    newDictionary = convertToDictionary(myFile)
    newDictionary2 = convertToDictionary(myFile2)

    writeToCSV(newDictionary, 'boysNames.csv')
    writeToCSV(newDictionary2, 'girlsNames.csv')

    print('successfully created boysNames.csv and girlsNames.csv')


main()
