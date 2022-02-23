import json
from PIL import Image
import os.path
from os import path
from utils import globalInfo

import pygame

cellSize = globalInfo.gridCellSize
existingPaths = []
with open("./data/types.json", encoding="utf8") as f:
    types = json.load(f)


def getObjectByType(x, y, typeID, rotation, bypassSideScroll=False):

    try:
        type = types[str(typeID)]
        pngPath = type["src"]
    except KeyError:
        pngPath = "./sprites/error.png"
    

    if path.exists("./sprites/{}".format(pngPath)):
        pngPath = "./sprites/{}".format(pngPath)
        returnCode = 0
    else:
        pngPath = "./sprites/error.png"
        returnCode = 1

    if rotation == "down":
        if not "./sprites/temp/down_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
            imageObject.save("./sprites/temp/down_{}.png".format(typeID))
            existingPaths.append("./sprites/temp/down_{}.png".format(typeID))
        pngPath = "./sprites/temp/down_{}.png".format(typeID)
    elif rotation == "flipped":
        if not "./sprites/temp/flipped_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
            imageObject.save("./sprites/temp/flipped_{}.png".format(typeID))
            existingPaths.append(
                "./sprites/temp/flipped_{}.png".format(typeID))
        pngPath = "./sprites/temp/flipped_{}.png".format(typeID)

    elif rotation == "flipped down":
        if not "./sprites/temp/flipped_down_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
            imageObject = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
            imageObject.save(
                "./sprites/temp/flipped_down_{}.png".format(typeID))
            existingPaths.append(
                "./sprites/temp/flipped_down_{}.png".format(typeID))
        pngPath = "./sprites/temp/flipped_down_{}.png".format(typeID)

    returnY = 720 - y * cellSize - cellSize
    if bypassSideScroll:
        returnX = x * cellSize
    else:
        returnX = x * cellSize - \
            (globalInfo.sideScrollSpeed * globalInfo.currentframe)

    try:
        hitboxType = type["type"]
    except UnboundLocalError:
        hitboxType = "block"

    return pngPath, returnX, returnY, hitboxType, returnCode


if __name__ == "__main__":
    print(
        "This is a library, not a script, strting test, this could take a few microseconds"
    )
    for i in range(1000):
        print(getObjectByType(0, 0, 1, "right"))
