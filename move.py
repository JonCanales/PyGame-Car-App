#blit() function is the main way to change the pixels on a screen that make up the display suface.
#It copies the picels from on image onto another
#It simply changes the colors of the pixels they arent added or moved.

#Seperate List we call background
background = [1,1,2,2,2,1]
#Copy each item from background into the screen
screen = [0]*6
for i in range(6):
    screen[i] = background[i]
print(screen)
playerPos = 3
screen[playerPos] = 8
print(screen)

screen[playerPos] = background[playerPos]
playerPos = playerPos -1
screen[playerPos] = 8
print(screen)