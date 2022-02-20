# essential imports
import shutil
import os


verbose = True


if verbose:
    print("importing")
# pygame setup
import pygame
from utils import objectSystemUtils  # Skatīt aprakstu pašā failā.
import object as objectUtil
from utils import globalInfo

#Clear temporary files
try:
    shutil.rmtree("./sprites/temp/")
except:
    pass
os.mkdir("./sprites/temp/")

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



currentframe = 0
y_vel=0
y_pos=0
smallest_y=0

# mainloop
while run:
    # update background
    screen.blit(background, (0, 0))

    # create ground (13 tiles long (see cell size in utils/globalInfo.py))
    for i in range(13):
       objectUtil.drawObject(screen, i, 0, 1, verbose=False)

    objectUtil.drawObject(screen, 4, 1, 3, verbose=True)
    objectUtil.drawObject(screen, 5, 1, 3, rotation="flipped", verbose=True)
    objectUtil.drawObject(screen, 7, 1, 3, verbose=True, rotation="down")
    objectUtil.drawObject(screen, 8, 1, 3, rotation="flipped down", verbose=True)

    if globalInfo.currentframe % 2 == 0:
        objectUtil.drawObject(screen, 6, 3, 5, verbose=False)
    else:
        objectUtil.drawObject(screen, 5, 3, 5, verbose=False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    objectUtil.drawObject(screen,4,1-y_pos,4, verbose=False)
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE] and smallest:
    #    vel[1]=
    pygame.display.flip()
    globalInfo.currentframe += 1
    clock.tick(100)
pygame.quit()
