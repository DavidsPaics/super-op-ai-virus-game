# imports
import sys


verbose = True


if verbose:
    print("importing")
# pygame setup
import pygame
from utils import objectSystemUtils  # Skatīt aprakstu pašā failā.

if verbose:
    print("initialize pygame")

pygame.init()
win = pygame.display.set_mode((1080, 720))

# variables

run = True
clock = pygame.time.Clock()

# mainloop

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
pygame.quit()
