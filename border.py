#Here in this file we are able to create a border that if crossed the game will crash.
#Also holding down the left and right keys will keep on moving instead of just pressing it once at a time like the display.py program.
import pygame
import time

pygame.init()
#Here we created our constants we dont intend to change
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#This variable tells where the cars edges will be. The location
#just means the top left pixel of the car. This tells the right side as well.
car_width = 73
############################################################################
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#Made own function to display text onto screen.
#Defines Text and Rectangle that will encompass it.Centers the text.THen blits onto surface. Then updates it.
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)
        #The logic for whether or not the car has crossed any boundaries left or right.
        if x > display_width - car_width or x < 0:
            crash()
            
        
        pygame.display.update()
        clock.tick(60)
#Runs Gameloop and once its done it will run the pygame.quit and crash and quit the game.
game_loop()
pygame.quit()
quit()


