# imports
import sys

verbose = sys.argv[1]
if verbose:
    print("importing")

import pygame
pygame.init()
win=pygame.display.set_mode((1300,700))
pygame.display.set_caption("tutoring")
run=True
clock=pygame.time.Clock()
x=0
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x+=1
        win.fill((0,0,0))
        pygame.draw.rect(win,(0,80,0),(1300-x,50,x+1,60))
        pygame.display.update()
