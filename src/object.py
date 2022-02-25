from utils import objectSystemUtils
import pygame
from utils import globalInfo

blocked = False
loaded = {}


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

def checkColission(data):
    pass


def drawObject(screen, x, y, typeID, rotation="up", verbose=False, bypassSideScroll=False, actualRotation=0):
    if not blocked or typeID == 4:
        if ((not x * globalInfo.gridCellSize - (globalInfo.sideScrollSpeed * globalInfo.currentframe) < -globalInfo.gridCellSize) and not (globalInfo.screenWidth - (x * globalInfo.gridCellSize - (globalInfo.sideScrollSpeed * globalInfo.currentframe)) < 0)) or bypassSideScroll:
            if rotation + str(typeID) in loaded:
                returnY = 720 - y * globalInfo.gridCellSize - globalInfo.gridCellSize
                if bypassSideScroll:
                    returnX = x * globalInfo.gridCellSize
                else:
                    returnX = x * globalInfo.gridCellSize - (globalInfo.sideScrollSpeed * globalInfo.currentframe)
                
                texture = pygame.image.load(loaded[rotation+str(typeID)]).convert_alpha()
                
                texture = pygame.transform.scale(
                    texture, (globalInfo.gridCellSize, globalInfo.gridCellSize)
                )
                screen.blit(pygame.transform.rotate(texture, actualRotation), (returnX, returnY))
                if verbose:
                    print("drawing object from cached texture")
            else:
                returnObject = gridCell(
                    x, y, typeID, rotation, bypassSideScroll=bypassSideScroll
                )
                texture = pygame.image.load(returnObject.texture).convert_alpha()
                texture = pygame.transform.scale(
                    texture, (globalInfo.gridCellSize, globalInfo.gridCellSize)
                )
                screen.blit(texture, (returnObject.x, returnObject.y))
                if verbose:
                    print("drawing: {}, {} from texture {}".format(
                        returnObject.x, returnObject.y, returnObject.texture))

                loaded[rotation +str(typeID)] = returnObject.texture
                return returnObject

        else:  # Object is offscreen
            if verbose:
                print("object of type {} was not drawn, due to not beeing visible".format(typeID))
            return None
        
    else:
        if verbose:
            print("Skip drawing object, due to experimental object drawing system beeing enabled")
