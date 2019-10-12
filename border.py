#Here in this file we are able to create a border that if crossed the game will crash.
#Also holding down the left and right keys will keep on moving instead of just pressing it once at a time like the display.py program.
import pygame
import time
import random

pygame.font.init()
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

#Takes x and Y starting points,wifth and height variables and a color
def things(thingx,thingy,thingw,thingh,color):
    #Then draws the polygon. The parameters are where,what color,and x and y locations
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


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
######
    #Starting position is random if its in x range between 0 and width of display
    thing_startx = random.randrange(0, display_width)
    #starting position for starty. GIves player time to get situated before it comes into view
    thing_starty = -600
    #Object Speed(How many pixels at a time it will move). 7 pixels it will move.
    thing_speed = 7
    
    #Blocks width and height
    thing_width = 100
    thing_height = 100
######
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
        
        
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty += thing_speed
        car(x,y)
        #The logic for whether or not the car has crossed any boundaries left or right.
        if x > display_width - car_width or x < 0:
            crash()
        #WHen thingy's location is greater then the display hight it will create another block
        if thing_starty > display_height:
            
            #Reassign a yvalue to the block where we use 0 -thing_height.
            thing_starty = 0 - thing_height
            
            #Refine the x-position of the block with a range between 0 and entire width of display
            thing_startx = random.randrange(0,display_width)

        if y < thing_starty + display_height:
            print('y crossover')
        
        if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx+thing_width:
            print('x crossover')
            crash()

        pygame.display.update()
        clock.tick(60)
#Runs Gameloop and once its done it will run the pygame.quit and crash and quit the game.
game_loop()



