import json
from PIL import Image
import os.path
from os import path

# imoprtē šo kā bibliotēku, izmanto funkciju getObjectType(n, rotation) lai dabūtu png attrašanās vietu, ja "name" sadaļa types.json failā iekļaus "inverted", fails tiks automātiski apgriests
# Tiek izvadīti šādi dati: pngPath(String), returnCode(Int)
# Ja kods ir 0 - viss ok, 1 - png tekstūra nav atrasta, tiek izmantota error.png


def getObjectByType(typeID, rotation):
    with open("./data/types.json", encoding="utf8") as f:
        types = json.load(f)

    type = types[str(typeID)]
    pngPath = type["src"]

    if path.exists("./sprites/{}".format(pngPath)):
        pngPath = "./sprites/{}".format(pngPath)
        returnCode = 0
    else:
        pngPath = "./sprites/error.png"
        returnCode = 1

    if rotation == "left":
        if not path.exists("./sprites/temp/rotated90_{}.png".format(typeID)):
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.ROTATE_90)
            imageObject.save("./sprites/temp/rotated90_{}.png".format(typeID))
            pngPath = "./sprites/temp/rotated90_{}.png".format(typeID)
    elif rotation == "down":
        if not path.exists("./sprites/temp/rotated180_{}.png".format(typeID)):
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.ROTATE_180)
            imageObject.save("./sprites/temp/rotated180_{}.png".format(typeID))
            pngPath = "./sprites/temp/rotated180_{}.png".format(typeID)
    elif rotation == "right":
        if not path.exists("./sprites/temp/rotated170_{}.png".format(typeID)):
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.ROTATE_270)
            imageObject.save("./sprites/temp/rotated270_{}.png".format(typeID))
            pngPath = "./sprites/temp/rotated270-_{}.png".format(typeID)

    return pngPath, returnCode


if __name__ == "__main__":
    print("This is a library, not a script")
    print(getObjectByType(1, "right"))
