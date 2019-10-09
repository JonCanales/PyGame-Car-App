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

x = (display_width * 0.45)
y = (display_width * 0.8)
x_change = 0
car_speed = 0
#Defines starting points for the car.
x = (display_height * 0.45)
y = (display_height *0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
         ###################   #################################
        #Asks if event is a KeyDown type Event. Which means if there is any key being pressed?
        #IF so is that key a LEFT arrow Key? If it is then our x_change is -5
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                x_change = -5
                #If it is a K_RIGHT event then our c_Change is 5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        #If event is a KEYUP then means we released a key so x_change is 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ############################################
        #changes our x variable
        x += x_change
        
        #Fills display with color white.
        gameDisplay.fill(white)
        car(x,y)

        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()