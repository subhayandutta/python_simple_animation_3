# Ref: https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html

from PIL import Image, ImageDraw
import sys

indirectory = '/Users/subhayan/Projects/python/orig/'
outdirectory = '/Users/subhayan/Projects/python/edited/'

origImag = indirectory + "Screenshot.png"

BLUE = "#0000ff"
GREEN = "#00ff00"
RED = "#ff0000"

def main():
    try:
        im = Image.open(origImag)
        filenamecounter = 1
        outImage = ''

        x1 = 120
        y1 = 180
        x3 = 880

        for i in range(x1, x3, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 + filenamecounter*40
            draw.line([x1, y1, x4, y1], width=5, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1

        x1 = 878
        y1 = 180
        y3 = 580
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(y1, y3, 40):
            draw = ImageDraw.Draw(im)
            y4 = y1 + anothercounter*40
            draw.line([x1, y1, x1, y4], width=5, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 880
        y1 = 580
        x3 = 120
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(x3, x1, 40):
            draw = ImageDraw.Draw(im)
            x4 = x1 - anothercounter*40
            draw.line([x1, y1, x4, y1], width=5, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        x1 = 122
        y1 = 580
        y3 = 180
        anothercounter = 1
        im = Image.open(outImage)

        for i in range(y3, y1, 40):
            draw = ImageDraw.Draw(im)
            y4 = y1 - anothercounter*40
            draw.line([x1, y1, x1, y4], width=5, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

    except IOError as e:
        print("IO Error ")
        print(e)
        pass


if __name__ == "__main__":
    main() 
