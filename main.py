# ATTENTION! IT WORKS ONLY WITH SQUARE PICTURES! IN CASE OF RECTANGULAR IMAGES, IT CREATES SQUARE AND CUT OFF EXCESS!
from PIL import Image
import sys

def generateImage(data):
    # first, we create "broken" variable, that is a table of of ASCII symbols
    broken = data.split("\n")
    # then we get size of our "image"
    sizeY = len(broken)
    sizeX = len(broken[0])
    #print(sizeX, sizeY)
    # next, we create new, empty image, that is 16 times bigger than the oryginal "image":
    # we do that, because oryginal "image" is list of pixel, and our letters are 16 pixels each
    # DUE TO PROBLEM WITH SQUARE ONLY, WE CREATE SQUARE NOT ORYGINAL ASPECT!
    if sizeX > sizeY:
        newImage = Image.new('RGB', ((sizeY - 1)* 16, (sizeY - 1)* 16), (255, 255, 255, 255))
    else: newImage = Image.new('RGB', (sizeX * 16, (sizeX - 1) * 16), (255, 255, 255, 255))    
    # the correct way is:
    # newImage = Image.new('RGB', (sizeX * 16, (sizeY) * 16), (255, 255, 255, 255))
    # but due to issues it cant be used :<
    # and now, we loop for every pixel of the oryginal "image"
    for x in range(sizeX - 1):
        for y in range(sizeY - 1):
            print(x,y)
            # then, we check what ASCII symbol is at x,y position and then paste correct image to correct position
            # the position is multiplied by 16 - remember, our images - building blocks - are 16 pixels each 
            try: 
                symbol = broken[x][y]
                # here, possible symbols are: ".", ":", "o", "0", "#", but remember - you can swap them out or even add / remove them
                if symbol == ".": newImage.paste(p20, (16 * y, 16 * x))
                if symbol == ":": newImage.paste(p40, (16 * y, 16 * x))
                if symbol == "o": newImage.paste(p60, (16 * y, 16 * x))
                if symbol == "0": newImage.paste(p80, (16 * y, 16 * x))
                if symbol == "#": newImage.paste(p100, (16 * y, 16 * x))
                #print(x,y)
            except: pass
    # at last, we return the "newImage" variable
    return newImage


if __name__ == "__main__":
    # first we check if input is correct
    if len(sys.argv) == 2:
        # if so, we import images that will be used as bulding blocks for our image
        # note: you can construct our image with different pieces: just swap out file names
        p20 = Image.open("assets/20.png")
        p40 = Image.open("assets/40.png")
        p60 = Image.open("assets/60.png")
        p80 = Image.open("assets/80.png")
        p100 = Image.open("assets/100.png")
        # next we get path to our .txt data file
        path = sys.argv[1]
        # after that we open our datafile and get it's contents
        with open(path, "r") as f: data = f.read()
        # next we convert the text to image
        image = generateImage(data)
        # at last, we save the image as "output.png"
        image.save('output.png')
