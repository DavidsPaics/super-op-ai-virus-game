from PIL import Image
from utils import globalInfo
import object

def startLoader():
    object.blocked = True
    loadLevel(1)

def loadLevel(level):
    with open("./data/level{}.txt".format(level), "r") as levelFile:
        levelLenght = levelFile.readline().replace("\n", "")
        print (levelLenght)
        levelData = []
        for i in range(globalInfo.worldHeightCells)


def drawLevelFromData(data, outputDir="data/temp/loadedLevel.png"):
    #TODO
    print("LEVEL LOADER NOT FINISHED, ABORTING")
    quit()
