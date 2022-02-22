import json
from PIL import Image
from utils import globalInfo
from utils import objectSystemUtils
import object

with open("./data/types.json", encoding="utf8") as f:
    types = json.load(f)


def startLoader():
    object.blocked = True
    loadLevel(1)


def loadLevel(level):
    levelData = []
    with open("./data/level{}.txt".format(level), "r") as levelFile:
        rawData = levelFile.read()
    levelData = list(map(str, rawData.split("\n")))
    drawLevelFromData(levelData)


def drawLevelFromData(data, output="./data/temp/loadedLevel.png"):
    backplate = Image.new("RGBA", (globalInfo.gridCellSize * int(data[0]) // 2, globalInfo.gridCellSize * (len(data) - 1)), (255, 0, 0, 0))

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

                drawX = (x - 1) * globalInfo.gridCellSize
                drawY = yIndex * globalInfo.gridCellSize

                loadedImage = Image.open(path)
                loadedImage = loadedImage.resize(
                    (globalInfo.gridCellSize, globalInfo.gridCellSize))
                Image.Image.paste(backplate, loadedImage, (drawX, drawY))

                pass
    backplate.save(output)
    print("Loaded level")
    return 
