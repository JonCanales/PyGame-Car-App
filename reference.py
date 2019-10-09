import pyGame
from pygame.locals import *

pygame.init()

#Created Display which will be the main display of the game.Also referred to as "Surface"
#600,800 will be the resolution that is 800px wide and 600px tall
gameDisplay = pygame.display.set_mode((800,600))

#set_caption is the title of the window which will say "A bit Racey"
pygame.display.set_caption("A bit Racey")

#Game Clock.Tracks Time within the game.Mostly used for FPS.Can speed game up or down.
clock = pygame.time.Clock()

crashed = False
#Loop will run until we crash
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    #Updates specific areas of the screen.
    pygame.display.update()
    #How many frames per second we are running
    clock.tick(60)

pygmae.quit()
quit()