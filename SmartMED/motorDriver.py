import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# Set the pins
L1, L2  = 15, 16
R1, R2 = 17, 18
SL, SR = 6, 8

# Left wheel pins
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
# Right wheel pins
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
# Left Sensor pin
GPIO.setup(SL, GPIO.OUT)
# Right Sensor pin
GPIO.setup(SR, GPIO.OUT)

def moveForward():
    GPIO.output(L1, True) #Left
    GPIO.output(L2, False)
    GPIO.output(R1, False) #Right
    GPIO.output(R2, True)

def leftTurn():
    GPIO.output(L1, True)
    GPIO.output(L2, True)
    GPIO.output(R1, False)
    GPIO.output(R2, True)

def rightTurn():
    GPIO.output(L1, True)
    GPIO.output(L2, False)
    GPIO.output(R1, True)
    GPIO.output(R2, True)

def stop():
    GPIO.output(L1, True)
    GPIO.output(L2, True)
    GPIO.output(R1, True)
    GPIO.output(R2, True)

def runMotor():
    #running loop for 10-sec
    t1 = time.time()
    t2 = time.time()+3
    while t1 < t2:
        t1 = time.time()
        if sense(SL) == 0 and sense(SR) == 0:# Move forward
            moveForward()
        elif sense(SL) == 1 and sense(SR) == 0:# Left Turn (Stop Left Motor)
            leftTurn()
        elif sense(SL) == 0 and sense(SR) == 1:# Right Turn (Stop Right Motor)
            rightTurn()
        else sense(SL) == 1 and sense(SR) == 1:# Stop for 5 sec
            stop()
            sleep(5)# RFID or glow led or do anything to signal to take medicine
            moveForward()

def sense(pin):
    sensor = GPIO.input(S1)
    if sensor  == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    runMotor()