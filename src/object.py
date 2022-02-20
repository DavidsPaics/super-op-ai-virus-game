from utils import objectSystemUtils
import pygame
from utils import globalInfo

variables = globalInfo.variables()
loaded = {""}


class gridCell(object):
    def __init__(self, x, y, typeID, rotation="up", bypassSideScroll=False):
        self.type = typeID
        self.rotation = rotation
        (
            self.texture,
            self.x,
            self.y,
            self.hitboxType,
            _,
        ) = objectSystemUtils.getObjectByType(
            x, y, typeID, rotation, bypassSideScroll=bypassSideScroll
        )


def drawObject(screen, x, y, typeID, rotation="up", verbose=False, bypassSideScroll=False):

    if (not x * variables.gridCellSize - (variables.sideScrollSpeed * globalInfo.currentframe) < -variables.gridCellSize):
        returnObject = gridCell(
            x, y, typeID, rotation, bypassSideScroll=bypassSideScroll
        )
        texture = pygame.image.load(returnObject.texture)
        texture = pygame.transform.scale(
            texture, (variables.gridCellSize, variables.gridCellSize)
        )
        screen.blit(texture, (returnObject.x, returnObject.y))
        if verbose:
            print("drawing: {}, {} from texture {}".format(
                returnObject.x, returnObject.y, returnObject.texture))
        return returnObject

    else:  # Object is offscreen
        if verbose:
            print("object of type {} was not drawn, due to not beeing visible".format(typeID))
        return None
