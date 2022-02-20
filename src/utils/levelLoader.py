from PIL import Image

def loadLevel(level):
    levelFile = open("level{}.txt".format(level))
    