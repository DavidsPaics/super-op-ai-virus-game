import pygame
currentframe = 0


class variables(object):
    def __init__(self):
        self.gridCellSize = 85
        self.worldHeightCells = 20
        self.worldHeightPx = self.worldHeightCells * self.gridCellSize
        self.sideScrollSpeed = 10
