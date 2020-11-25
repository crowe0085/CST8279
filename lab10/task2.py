import csv


def displayCsvFile(fName):
    try:
        with open(fName, newline='') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='|')
            # for row in reader:
            #     print(', '.join(row))
            lst = list(reader)
            for x in range(len(lst)):
                print(lst[x])

    except Exception as e:
        print(e)


def main():
    while True:
        inp = input('please enter a csv file to read >> ')
        displayCsvFile(inp)

        inp = input('would you like to enter another? any key to continue, q to quit >> ')

        if inp == 'q':
            break


main()
