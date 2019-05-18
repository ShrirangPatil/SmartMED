import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# Set the pins
B1, B2, B3, B4 = 6, 13, 19, 26    # Back wheels (B3, B4) = Right (B1, B2) = Left
F1, F2, F3, F4 = 12, 16, 20, 21  # Front wheels (F3, F4) = Right (F1, F2) = Left
SL, SR, SM = 15, 18, 5

# Back wheels
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)
GPIO.setup(B4, GPIO.OUT)

# Front wheel pins
GPIO.setup(F1, GPIO.OUT)
GPIO.setup(F2, GPIO.OUT)
GPIO.setup(F3, GPIO.OUT)
GPIO.setup(F4, GPIO.OUT)

#Sensors
GPIO.setup(SL, GPIO.IN)
GPIO.setup(SR, GPIO.IN)
GPIO.setup(SM, GPIO.IN)

def moveForward():
	# Back wheels
    GPIO.output(B1, True) #Left
    GPIO.output(B2, False)
    GPIO.output(B3, True) #Right
    GPIO.output(B4, False)
    # Front wheels
    GPIO.output(F1, True)
    GPIO.output(F2, False)
    GPIO.output(F3, True)
    GPIO.output(F4, False)

def moveBack():
	# Back wheels
    GPIO.output(B2, True) #Left
    GPIO.output(B1, False)
    GPIO.output(B4, True) #Right
    GPIO.output(B3, False)
    # Front wheels
    GPIO.output(F2, True)
    GPIO.output(F1, False)
    GPIO.output(F4, True)
    GPIO.output(F3, False)

def leftTurn():
    #stop left wheels
    GPIO.output(F1, False)
    GPIO.output(F2, False)
    GPIO.output(B1, False)
    GPIO.output(B2, False)
    
    #rotate right wheels
    GPIO.output(F3, True)
    GPIO.output(F4, False)
    GPIO.output(B3, True)
    GPIO.output(B4, False)

def rightTurn():
    #rotate right wheels
    GPIO.output(F1, True)
    GPIO.output(F2, False)
    GPIO.output(B1, True)
    GPIO.output(B2, False)
    
    #stop right wheels
    GPIO.output(F3, False)
    GPIO.output(F4, False)
    GPIO.output(B3, False)
    GPIO.output(B4, False)

def stop():
    #back wheels
    GPIO.output(B1, False) #Left
    GPIO.output(B2, False)
    GPIO.output(B3, False) #Right
    GPIO.output(B4, False)
    # Front wheels
    GPIO.output(F1, False)
    GPIO.output(F2, False)
    GPIO.output(F3, False)
    GPIO.output(F4, False)

def runMotor(bedNumbers):
    #running loop for 10-sec
    #t1 = time.time()
    #t2 = time.time()+3
    countBedNumber = 0
    while True:
        #t1 = time.time()
        if sense(SL) == 0 and sense(SM)== 1 and sense(SR) == 0:# Move forward
            moveForward()
        elif sense(SL) == 1 and sense(SR) == 0:# Left Turn (Stop Left Motor)
            leftTurn()
        elif sense(SL) == 0 and sense(SR) == 1:# Right Turn (Stop Right Motor)
            rightTurn()
        elif sense(SL) == 1 and sense(SM) == 1 and sense(SR) == 1:# Stop for 5 sec
            countBedNumber += 1
            if countBedNumber in bedNumbers:
                stop()
                os.system('omxplayer /home/pi/Desktop/V2.mp3')
                sleep(6)
            #sleep(5)# RFID or glow led or do anything to signal to take medicine
            #moveForward()
            

def testMotor():
    while True:
        moveForward()
        sleep(3)
        leftTurn()
        sleep(1.5)
        moveForward()
        sleep(3)
        rightTurn()
        sleep(1.5)
        moveBack()
        sleep(2)
        stop()
        break

def sense(pin):
    sensor = GPIO.input(pin)
    if sensor  == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    runMotor()
