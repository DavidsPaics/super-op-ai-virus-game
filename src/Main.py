import os
import shutil
import pygame
import object as objectUtil
from utils import globalInfo
verbose = True
if verbose:
    print("importing")


# Clear temporary files
try:
    shutil.rmtree("./sprites/temp/")
except:
    pass
os.mkdir("./sprites/temp/")

if verbose:
    print("initialize pygame")
pygame.init()
# Variables
font = pygame.font.SysFont("Arial", 25)
screen = pygame.display.set_mode((1080, 720))
run = True
clock = pygame.time.Clock()
background = pygame.image.load("./sprites/background.png")
background = pygame.transform.scale(background, (1080, 720))
experimentalLoaderText = font.render(
    "Press L to switch to experimental level loading system (DO NOT USE)", 3, pygame.Color("red"))
alive = True

pygame.mouse.set_visible(False)
pygame.display.set_caption("Geometry shoot")


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


def commit_stop_living():
    # Commits die
    print("you died")
    global alive
    alive = False


currentframe = 0
y_vel = 0
y_pos = 0
smallest_y = 0
airborne = False
# mainloop
while run:
    # update background
    screen.blit(background, (0, 0))

    # create ground (13 tiles long (see cell size in utils/globalInfo.py))
    for i in range(15):
        objectUtil.drawObject(screen, i, 0, 1)

    screen.blit(update_fps(), (10, 0))
    screen.blit(experimentalLoaderText, (200, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Player position and velocity managment

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not airborne:

        y_vel = -43
        airborne = True
    y_pos += y_vel
    if airborne == True:
        if smallest_y < y_pos-50:
            commit_stop_living()
        elif smallest_y <= y_pos:
            airborne = False
            y_pos = smallest_y
            y_vel = 0

        else:
            y_vel += 5  # I tested this, this should give us a nice smooth jump
            if y_vel > 50:
                y_vel = 50
            if y_vel < -50:
                y_vel = -50

    objectUtil.drawObject(screen, 5, 1-(y_pos/100), 4,
                          bypassSideScroll=True)

    if alive:
        globalInfo.currentframe += 1
    globalInfo.realCurrentFrame += 1
    clock.tick(60)
    pygame.display.update()
pygame.quit()
