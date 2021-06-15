#set_mode to determine the size of the rectangle, maybe two inputs?

#rect objects for the actual game board and for the goal

#rect object to hold our robot

#robot image must move to the goal


import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (50, 50, 255)

print('Enter a Width: ')
width = int(input())
print('Enter a Height: ')
length = int(input())

#center of screen
robotX = width / 2
robotY = length / 2

initialGoalX = random.randint(0, width)
initialGoalY = random.randint(0, length)

gameDisplay = pygame.display.set_mode((width, length)) #setting the window size
pygame.display.set_caption('Robot goal game!')

robot = pygame.image.load('robot.jpg').convert() 
gameDisplay.blit(robot, (robotX, robotY))
pygame.display.update()


gameExit = False
xCoordReached = False
yCoordReached = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #handles exit button
            gameExit = True
        #print(event)  #for testing events

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, blue, [initialGoalX, initialGoalY, 10, 10]) #start x, start y, width, height

    #here we loop and move toward our goal
    if (robotX > initialGoalX):
        robotX -= 1
    elif (robotX < initialGoalX):
        robotX += 1
    else:
        xCoordReached = True

    if (robotY > initialGoalY):
        robotY -= 1
    elif (robotY < initialGoalY):
        robotY += 1
    else:
        yCoordReached = True


    gameDisplay.blit(robot, (robotX, robotY)) #updates the location each time
    if (xCoordReached == True and yCoordReached == True):
        pygame.display.set_caption('Goal Reached!!!')

    pygame.display.update()

pygame.quit()
quit()
