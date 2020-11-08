import time

# Serial ports
leftPort = ""
rightPort = ""
nanoPort = ""

# Robot configuration
#
# Body Part           Controller   Pin   MinPos   MaxPost   StartPos
# -------------------------------------------------------------------------------
# eyesX               right        47
# eyesY               right        45
# jaw                 right        53
# neckRotate          right        51
# neckTilt            right        49    45(up)   135(down) 90
# rightSholderTilt    right
# rightShoulderPivot  right
# rightSholderRotate  right
# rightBicep          right
# rightWrist          right
# rightThumb          right
# rightIndex          right
# rightMajeur         right
# rightRingFinger     right
# rightPinky          right
# pir                 right
# leftSholderTilt     left
# leftShoulderPivot   left
# leftSholderRotate   left
# leftBicep           left
# leftWrist           left
# leftThumb           left
# leftIndex           left
# leftMajeur          left
# leftRingFinger      left
# leftPinky           left
# stomach             left
# neopixel            nano
    

# Arduino services
print("Connecting Arduino controllers...")
leftController = Runtime.start("leftController", "Arduino")
rightController = Runtime.start("rightController", "Arduino")
nanoController = Runtime.start("nanoController", "Arduino")
leftController.connect(leftPort)
rightController.connect(rightPort)
nanoController.connect(nanoPort)
time.sleep(3);

print("Initialising all servos...")
jaw = Runtime.start("jaw", "Servo")
neckRotate = Runtime.start("neckRotate", "Servo")
neckTilt = Runtime.start("neckTilt", "Servo")
eyesX = Runtime.start("eyesX", "Servo")
eyesY = Runtime.start("eyesY", "Servo")

def attachHead():
    jaw.attach(rightController, 53, 174) # closed
    neckRotate.attach(rightController, 51, 95, 60) # forward
    neckTilt.attach(rightController, 49, 95, 60) # forward
    eyesX.attach(rightController, 47, 90) # unkown
    eyesY.attach(rightController, 45, 70, 50) # forward

def detachHead():
    print("Detaching servos...")
    jaw.detach()
    neckRotate.detach()
    neckTilt.detach()
    eyesX.detach()
    eyesY.detach()
    
def neckTiltDemo():
    print("Neck tilt demo...")
    neckTilt.moveTo(45) # look up
    time.sleep(1)
    neckTilt.moveTo(135) # look down
    time.sleep(2)
    neckTilt.moveTo(95) # look forward
    time.sleep(2)
    
def eyesDemo():
    print("Eyes demo...")
    eyesY.moveTo(50)
    time.sleep(1)
    eyesY.moveTo(90)
    time.sleep(1)
    eyesY.moveTo(70)
    time.sleep(1)

def lookAround():
    print("look around...")
    neckRotate.moveTo(165)
    neckTilt.moveTo(50)
    time.sleep(2)
    neckRotate.moveTo(95)
    time.sleep(2)
    neckTilt.moveTo(90)
    time.sleep(2)

def lookAroundDown():
    neckRotate.moveTo(45)
    neckTilt.moveTo(135)
    time.sleep(2)
    neckRotate.moveTo(95)
    time.sleep(2)
    neckTilt.moveTo(90)
    time.sleep(1)

def jawDemo():
    print("talk...")
    jaw.moveTo(128)
    sleep(0.3)
    jaw.moveTo(174)
    sleep(0.3)

def shakeHead():
    print("Shake head...")
    neckRotate.moveTo(70)
    sleep(1)
    neckRotate.moveTo(120)
    sleep(1)
    neckRotate.moveTo(95)
    sleep(1)

def headDemo():
    attachHead()
    print("Head demo.")
    for i in range(5):
        eyesDemo()
        jawDemo()
        neckTiltDemo()
        lookAround()
        lookAroundDown()
    detachHead()
   
time.sleep(4)
headDemo()

