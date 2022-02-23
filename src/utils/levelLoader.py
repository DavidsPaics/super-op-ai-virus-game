from PIL import Image
import object

def startLoader():
    object.blocked = True

def loadLevel(level):
    levelFile = open("level{}.txt".format(level))
    levelData = []
