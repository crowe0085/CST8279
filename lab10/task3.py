import csv
import re
from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


# takes in the object, x and y coordinates then displays it on the gfxhat
def displayObject(obj, x, y):
    clearScreen(lcd)
    oldX = x

    for i in range(len(obj)):  # outer index
        for j in range(len(obj[i])):  # inner index
            # setting the pixel to either 1 or 0 based on the objects index value
            pix = int(obj[i][j])
            lcd.set_pixel(oldX, y, pix)
            oldX += 1
        y += 1
        lcd.set_pixel(x, y, pix)
        oldX = x
    lcd.show()


def openFile(filePath):
    try:
        return open(filePath, 'r+')
    except:
        print('error opening file')


def generateDictionary(file):
    myDictionary = {}
    for line in file:
        nLine = re.split(',', line.strip())
        key = nLine[1]
        pair = convertToBinary(nLine[0])
        myDictionary[key] = pair
    return myDictionary


def convertToBinary(value):
    lst = [
        value[2]+''+value[3],
        value[4]+''+value[5],
        value[6]+''+value[7],
        value[8]+''+value[9],
        value[10]+''+value[11],
        value[12]+''+value[13],
        value[14]+''+value[15],
        value[16]+''+value[17]
    ]

    for i in range(len(lst)):
        lst[i] = bin(int(lst[i], 16))[2:].zfill(8)  # converting each element to binary

    return lst


def main():
    myFile = openFile('font3.txt')
    myDictionary = generateDictionary(myFile)

    inp = input('enter a key >> ')

    try:
        displayObject(myDictionary[inp], 62, 40)
    except:
        print('Error couldnt find character')

    print('press any key to quit')
    getchar()
    clearScreen(lcd)


main()
