#THIS CODE RUNS PERFECT FOR THE DISPLAY FOR SOME REASON COMPARE IT TO OTHER CODE


import pygame
pygame.init()

import pygame
white = (255,255,255)
(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

            