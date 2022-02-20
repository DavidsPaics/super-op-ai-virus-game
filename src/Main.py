verbose = True
if verbose:
    print("importing")

# essential imports
from utils import globalInfo
import object as objectUtil
import pygame
import shutil
import os





# Clear temporary files
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
font = pygame.font.SysFont("Arial", 18)


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


vel = [2, 0]
ypos = 0
smallest_y = 0

# mainloop
while run:
    # update background
    screen.blit(background, (0, 0))

    # create ground (13 tiles long (see cell size in utils/globalInfo.py))
    for i in range(13):
        objectUtil.drawObject(screen, i, 0, 1, verbose=True)

    objectUtil.drawObject(screen, 4, 1, 3, verbose=True)
    objectUtil.drawObject(screen, 5, 1, 3, rotation="flipped", verbose=True)
    objectUtil.drawObject(screen, 7, 1, 3, verbose=True, rotation="down")
    objectUtil.drawObject(
        screen, 8, 1, 3, rotation="flipped down", verbose=True)

    screen.blit(update_fps(), (10, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    objectUtil.drawObject(screen, 5, 1-ypos, 5, verbose=True)
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE] and smallest:
    #    vel[1]=10
    globalInfo.currentframe += 1
    clock.tick(60)
    pygame.display.update()
pygame.quit()
