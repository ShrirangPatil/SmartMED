import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# Set the pins
B1, B2, B3, B4 = 5, 6, 19, 26    # Back wheels (B3, B4) = Right (B1, B2) = Left
F1, F2, F3, F4 = 12, 16, 20, 21  # Front wheels (F3, F4) = Right (F1, F2) = Left
SL, SR = 6, 8

# Back wheels
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)

# Front wheel pins
GPIO.setup(F1, GPIO.OUT)
GPIO.setup(F2, GPIO.OUT)
GPIO.setup(F3, GPIO.OUT)
GPIO.setup(F4, GPIO.OUT)

def moveForward():
	# Back wheels
    GPIO.output(B1, True) #Left
    GPIO.output(B2, False)
    GPIO.output(B3, True) #Right
    GPIO.output(B4, False)
    # Front wheels
    GPIO.output(B1, True)
    GPIO.output(B2, False)
    GPIO.output(B3, True)
    GPIO.output(B4, False)

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
def testMotor():
	while True:
		moveForward()
		sleep(1)
		leftTurn()
		sleep(1)
		rightTurn()
		sleep(1)
		stop()

def sense(pin):
    sensor = GPIO.input(S1)
    if sensor  == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    runMotor()