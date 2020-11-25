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


def sketch(x, y):

    while True:
        inp = getchar()

        if inp == '\x1b[A': # up
            y -= 1
            if y == 0:
                y = 63
        if inp == '\x1b[B': # down
            y += 1
            if y == 63:
                y = 0
        if inp == '\x1b[C': # right
            x += 1
            if x == 127:
                x = 0
        if inp == '\x1b[D': # left
            x -= 1
            if x == 0:
                x = 127
        if inp == "s":
            clearScreen(lcd)
        elif inp == "q":
            break
        else:
            lcd.set_pixel(x,y,1)
            lcd.show()
          


#main function
def main():
    x = int(input("what coordinates would you like to start the etch a sketch? x : must not be greater than 127 >>"))
    y = int(input("what coordinates would you like to start the etch a sketch? y : must not be greater than 63 >>"))
    if x > 127:
        x = 0
    if y > 63:
        y = 0
    lcd.clear()
    lcd.show()
    bg = "Etch A Sketch"
    displayText(bg, lcd, 20, 20)

    sketch(x, y)


main()
