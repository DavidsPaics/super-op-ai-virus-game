# imports
import sys


verbose = True


if verbose:
    print("importing")
# pygame setup
import pygame
from utils import objectSystemUtils  # Skatīt aprakstu pašā failā.
import object as objectUtil

if verbose:
    print("initialize pygame")
pygame.init()
screen = pygame.display.set_mode((1080, 720))
run = True
clock = pygame.time.Clock()
background = pygame.image.load("./sprites/background.png")
background = pygame.transform.scale(background, (1080, 720))
pygame.mouse.set_visible(False)
pygame.display.set_caption("Geometry shoot")

# mainloop
while run:
    # update background
    screen.blit(background, (0, 0))

    #create ground (13 tiles long (see cell size in utils/globalInfo.py))
    for i in range(13):
        objectUtil.drawObject(screen, i, 0, 5, verbose=True)
    
    objectUtil.drawObject(screen, 4, 1, 3, rotation="left", verbose=True)
    objectUtil.drawObject(screen, 5, 1, 3, rotation="right", verbose=True)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
