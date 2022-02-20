import pygame
from utils import globalInfo

variables = globalInfo.variables()

from utils import objectSystemUtils


class gridCell(object):
    def __init__(self, x, y, typeID, rotation="up"):
        self.type = typeID
        self.rotation = rotation
        (
            self.texture,
            self.x,
            self.y,
            self.hitboxType,
            _,
        ) = objectSystemUtils.getObjectByType(x, y, typeID, rotation)


def drawObject(screen, x, y, typeID, rotation="up", verbose=False):
    returnObject = gridCell(x, y, typeID, rotation)
    texture = pygame.image.load(returnObject.texture)
    texture = pygame.transform.scale(
        texture, (variables.gridCellSize, variables.gridCellSize)
    )
    screen.blit(texture, (returnObject.x, returnObject.y))
    if verbose:
        print("drawing: {}, {} from texture {}".format(returnObject.x, returnObject.y, returnObject.texture))
    return returnObject
