import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
#Defines colors in RGB formatt.
black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
#Loads racecar.png into the carImg variable
carImg = pygame.image.load('racecar.jpeg')

#defines car funciton. Puts car to the display
#Blit draws the image to the screen
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#Defines starting points for the car.
x = (display_height * 0.45)
y = (display_height *0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #Fills display with color white.
        gameDisplay.fill(white)
        car(x,y)

        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()