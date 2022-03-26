import json
from PIL import Image
import pygame
from utils import globalInfo
from utils import objectSystemUtils
import object

with open("./data/types.json", encoding="utf8") as f:
    types = json.load(f)


def startLoader(screen):
    object.blocked = True
    texture = loadLevel(1, screen)
    return texture


def loadLevel(level, screen):
    levelData = []
    with open("./data/level{}.txt".format(level), "r") as levelFile:
        rawData = levelFile.read()
    levelData = list(map(str, rawData.split("\n")))
    globalInfo.levelData = levelData
    drawLevelFromData(levelData, output="./data/temp/loadedLevel{}.png".format(level))
    texture = pygame.image.load("./data/temp/loadedLevel{}.png".format(level)).convert_alpha()
    return texture



def drawLevelFromData(data, output="./data/temp/loadedLevel.png"):
    backplate = Image.new("RGBA", (90 * int(data[0]) // 2, 90 * (len(data) - 1)), (255, 0, 0, 0))

    yIndex = -1
    for y in data[1:]:
        yIndex += 1
        for x in range(1, int(data[0]) // 2 + 1):
            rotation = y[x * 2 - 2]
            type = y[x * 2 - 1]

            if rotation == "1":
                rotation = "down"
            elif rotation == "2":
                rotation = "flipped"
            elif rotation == "3":
                rotation = "flipped down"

            if not type == "0":
                path, _, _, _, _ = objectSystemUtils.getObjectByType(
                    0, 0, type, rotation, bypassSideScroll=True)

                drawX = (x - 1) * 90
                drawY = yIndex * 90

                loadedImage = Image.open(path)
                loadedImage = loadedImage.resize(
                    (90, 90))
                Image.Image.paste(backplate, loadedImage, (drawX, drawY))

                pass
    backplate.save(output)
    print("Loaded level")

def chopLevel(level, width):
    im = Image.open("./data/temp/loadedLevel{}.png")

    width, height = im.size
    
    # Setting the points for cropped image
    left = 5
    top = height
    right = 164
    bottom = height
    
    # Cropped image of above dimension
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    im1.save("")