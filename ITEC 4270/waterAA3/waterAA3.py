#robot arm class
#has a base, an 'elbow' and a 'wrist'
#simple claw mechanism for grabbing
#a sensor that picks up distance and grabs an object when it is close

#robot class
class ClawRobot:
    def __init__(self, sensor, servoController, servo, claw):
        self.servocontroller = servoController
        self.sensor = sensor
        self.servo = servo
        self.claw = claw

    def activate(self):
        self.sensor.getData()
        while self.sensor.sensordata > 1:
            self.sensor.closeDistance()
            self.sensor.getData()
        self.servocontroller.signal(self.servo, self.claw)


            


#Sensor
class Sensor:
    def __init__(self, thetype):
        self.sensortype = thetype
        self.sensordata = 5 #default distance in cm

    def getData(self):
        print(self.sensortype, ' is currently: ', self.sensordata)
    
    def closeDistance(self):
        self.sensordata = self.sensordata - 1
        print('Closing distance to target...')


#Controller
class ServoController:
    def __init__(self, thetype):
        self.etype = thetype

    def signal(self, servo, claw):
        print(self.etype, ' receiving signal from Sensor...')
        servo.receiveSignal(claw)

#Actuator
class Servo:
    def __init__(self, thetype):
        self.sensortype = thetype

    #function to simulate receiving a signal
    def receiveSignal(self, claw):
        print(self.sensortype, ' receiving signal from ServoController...')
        claw.closeclaw()

#EndEffector
class Claw:
    def __init__(self, thetype):
        self.description = thetype
    
    def closeclaw(self):
        print('Closing claw: ', self.description,' on target!')



Clawbot = ClawRobot(Sensor('Distance'), ServoController('Servo Controller'), Servo('Claw Servo'), Claw('Robotic Claw'))
Clawbot.activate()


