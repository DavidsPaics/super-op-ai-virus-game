import json
from PIL import Image
import os.path
from os import path

# imoprtē šo kā bibliotēku, izmanto funkciju getObjectType(n) lai dabūtu png attrašanās vietu, ja "name" sadaļa types.json failā iekļaus "inverted", fails tiks automātiski apgriests
# Tiek izvadīti šādi dati: pngPath(String), returnCode(Int)
# Ja kods ir 0 - viss ok, 1 - png tekstūra nav atrasta, tiek izmantota error.png


def getObjectByType(typeID):
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

    if "inverted" in type["name"]:
        imageObject = Image.open(pngPath)
        imageObject = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
        imageObject.save("./sprites/temp/flipped{}.png".format(typeID))
        pngPath = "./sprites/temp/flipped{}.png".format(typeID)

    return pngPath, returnCode
