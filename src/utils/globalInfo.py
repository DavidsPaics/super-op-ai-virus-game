import pygame
currentframe = 0
realCurrentFrame = 0


class variables(object):
    def __init__(self):
        self.gridCellSize = 90
        self.worldHeightCells = 5
        self.worldHeightPx = self.worldHeightCells * self.gridCellSize
        self.sideScrollSpeed = 10
        self.sideScrollSpeed = 2
        self.screenWidth = 1080