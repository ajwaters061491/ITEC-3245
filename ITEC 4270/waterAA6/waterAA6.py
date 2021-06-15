#model 1 global map no sensors

class Robot:
  def __init__(self, startPosX, startPosY, startDir, goalX, goalY):
    self.startPosX = startPosX #initial point on the global map
    self.startPosY = startPosY
    self.startDir =  startDir #starting direction
    self.currentDir = startDir #will change based on turning
    self.currentPosX = startPosX #will begin at start location and
    self.currentPosY = startPosY #increment or decrement
    self.goalX = goalX
    self.goalY = goalY
    
    def Move(self):
        print("Moving forward...")

    def TurnLeft(self):
        print("turning left...")
        self.currentDir += 90       
        
    def TurnRight(self):
        print("turning right...")
        self.currentDir -= 90

    def CheckGoal(self):
        if (self.currentPosX < goalX):
            while (self.currentPosX != 90):
                self.turnLeft()
            self.Move()

        elif (self.currentPosX > goalX):
            while (self.currentPosX != 270):
                self.turnLRight()
            self.Move()

        elif (self.currentPosY < goalY):
            while (self.currentPosY != 0):
                self.turnLeft()
            self.Move()
        elif (self.currentPosY > goalY):
            while (self.currentPosY != 0):
                self.turnRight()
            self.Move()
        else:
            self.Move()







#model 2 no global map with sensors

import random

class Robot2:
  def __init__(self, startPosX, startPosY, startDir, goalX, goalY):
    self.startPosX = startPosX #initial point on the global map
    self.startPosY = startPosY
    self.startDir =  startDir #starting direction
    self.currentDir = startDir #will change based on turning
    self.currentPosX = startPosX #will begin at start location and
    self.currentPosY = startPosY #increment or decrement
    self.sensor = False

    
    def Move(self):
        print("Moving forward...")

    def TurnLeft(self):
        print("turning left...")
        self.currentDir += 90       
        
    def TurnRight(self):
        print("turning right...")
        self.currentDir -= 90

    def CheckDistance(self):
        while (self.sensor == True):
            ran = random.randint(1,2)
            if (ran == 1):
                self.TurnLeft()
            elif (ran == 2):
                self.TurnRight()
