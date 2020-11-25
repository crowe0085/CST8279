from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar


def displayText(text, lcd, x, y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x+w):
        for y1 in range(y, y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


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
            pix = obj[i][j]
            lcd.set_pixel(oldX, y, pix)
            oldX += 1
        y += 1
        lcd.set_pixel(x, y, pix)
        oldX = x
    lcd.show()


#main function
def main():
    while True:
        inp = input("would you like do view 1 or 2? enter q to quit>>")

        if inp == "q":
            clearScreen(lcd)
            break

        x = int(
            input("Please enter the starting coordinates x: must be less than 127 >>"))
        y = int(
            input("Please enter the starting coordinates y: must be less than 127 >>"))

        if inp == "1":
            obj = f1
        elif inp == "2":
            obj = pm
        else:
            print("Invalid choice")

        for i in obj:  # looping in order to find the length of the x and y coordinates of the object so we can see if its too large
            for j in i:
                lenX = len(i)
                lenY = len(obj)

        if lenY + y > 63:
            print("Invalid y coordinate")
        elif lenX + x > 127:
            print("Invalid x coordinate")
        else:
            displayObject(obj, x, y)


f1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

pm = [
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
]

main()
