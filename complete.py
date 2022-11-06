from time import sleep

gui = Runtime.start("gui", "SwingGui")

# Serial ports
leftPort = "/dev/left_mega"
rightPort = "/dev/right_mega"
nanoPort = "/dev/nano"

# Robot configuration
#
# Body Part           Controller   Pin   MinPos   MaxPost        StartPos
# --------------------------------------------------------------------------
# eyesX               right        47
# eyesY               right        45    50          90          70(forward)
# jaw                 right        53    128         174
# neckRotate          right        51    5           180
# neckTilt            right        49    45(up)      135(down)   90(forward)
# rightOmoplate       right        9     10          160(raised)  
# rightShoulder       right        10    0(lowered)  180(raised)
# rightRotate         right        11    0           180
# rightBicep          right        8     0(relaxed)  60(flexed)
# rightWrist          right        7     0           180
# rightThumb          right        6     0(closed)   170
# rightIndex          right        5     0(closed)   170
# rightMajeure        right        4     0(closed)   170
# rightRingFinger     right        3     0(closed)   170
# rightPinky          right        2     0(closed)   170
# pir                 right        12
# leftOmoplate        left         9     10(lowered) 160(raised)
# leftShoulder        left         10    0(lowered)  180(raised)
# leftRotate          left         11    0           180
# leftBicep           left         8     0(relaxed)  60(flexed)
# leftWrist           left         7     0           180
# leftThumb           left         6     0(closed)   170
# leftIndex           left         5     0(closed)   170
# leftMajeure         left         4     0(closed)   170
# leftRingFinger      left         3     0(closed)   170(open)
# leftPinky           left         2     0(closed)   170(open)
# stomachTilt         left         27    75          120            97(center)
# stomachRotate       left         28    70          110            90(center)
# neopixel            nano         3
    
    
# Arduino services
print("Connecting Arduino controllers...")
leftController = Runtime.start("leftController", "Arduino")
leftController.setBoardMega()
leftController.connect(leftPort)
rightController = Runtime.start("rightController", "Arduino")
rightController.setBoardMega()
rightController.connect(rightPort)
nanoController = Runtime.start("nanoController", "Arduino")
nanoController.setBoardNano()
nanoController.connect(nanoPort)
sleep(2);

# All servos
print("Initialising all servos...")
jaw = Runtime.start("jaw", "Servo")
neckRotate = Runtime.start("neckRotate", "Servo")
neckTilt = Runtime.start("neckTilt", "Servo")
eyesX = Runtime.start("eyesX", "Servo")
eyesY = Runtime.start("eyesY", "Servo")
rightOmoplate = Runtime.start("rightOmoPlate", "Servo")
rightShoulder = Runtime.start("rightShoulder", "Servo")
rightRotate = Runtime.start("rightRotate", "Servo")
rightBicep = Runtime.start("rightBicep", "Servo")
rightWrist = Runtime.start("rightWrist", "Servo")
rightThumb = Runtime.start("rightThumb", "Servo")
rightIndex = Runtime.start("rightIndex", "Servo")
rightMajeure = Runtime.start("rightMajeure", "Servo")
rightRingFinger = Runtime.start("rightRingFinger", "Servo")
rightPinky = Runtime.start("rightPinky", "Servo")
leftOmoplate = Runtime.start("leftOmoPlate", "Servo")
leftShoulder = Runtime.start("leftShoulder", "Servo")
leftRotate = Runtime.start("leftRotate", "Servo")
leftBicep = Runtime.start("leftBicep", "Servo")
leftWrist = Runtime.start("leftWrist", "Servo")
leftThumb = Runtime.start("leftThumb", "Servo")
leftIndex = Runtime.start("leftIndex", "Servo")
leftMajeure = Runtime.start("leftMajeure", "Servo")
leftRingFinger = Runtime.start("leftRingFinger", "Servo")
leftPinky = Runtime.start("leftPinky", "Servo")
stomachTilt = Runtime.start("stomachTilt", "Servo")
stomachRotate = Runtime.start("stomachRotate", "Servo")

print("Initialising pir...")
#pir = Runtime.start('pir', 'Pir')
#pir.attach(rightController, 12)
#pir.isVerbose = True
#pir.enable(1) # 1 is how many times per second we poll the pir

print("Initialising neopixel...")
neopixel = Runtime.start("NeoPixel", "NeoPixel")

print("Initialising speech and mouth control...")
speech = Runtime.start("MarySpeech", "MarySpeech")
speech.setVoice("Spike")
mouthControl = Runtime.start("MouthControl", "MouthControl")
mouthControl.mouthClosedPos = 174
mouthControl.mouthOpenedPos = 128
mouthControl.attach(jaw)
mouthControl.attach(speech)

def attachHead():
    print("Attaching head...")
    jaw.attach(rightController, 53, 174) # closed
    neckRotate.attach(rightController, 51, 95, 60) # forward
    neckTilt.attach(rightController, 49, 95, 60) # forward
    eyesX.attach(rightController, 47, 90) # unkown
    eyesY.attach(rightController, 45, 70, 50) # forward

def attachArms():
    print("Attaching arms...")
    #rightOmoplate.attach(rightController, 9, 80)
    rightShoulder.attach(rightController, 10, 0, 80)
    rightRotate.attach(rightController, 11, 90, 80)
    #rightElbow.attach(rightController, 8, 0, 80)
    #rightWrist.attach(rightController, 7, 170, -1.0)
    #rightThumb.attach(rightController, 5, 170, 90)
    #rightIndex.attach(rightController, 6, 170, 90)
    #rightMajeure.attach(rightController, 4, 170, 90)
    #rightRingFinger.attach(rightController, 3, 170, 90)
    #rightPinky.attach(rightController, 2, 170, 90)
    #leftOmoplate.attach(rightController, 9, 80)
    leftShoulder.attach(rightController, 10, 0, 80)
    leftRotate.attach(rightController, 11, 90, 80)
    #leftElbow.attach(rightController, 8, 0, 80)
    #leftWrist.attach(rightController, 7, 170, -1.0)
    #leftThumb.attach(rightController, 5, 170, 90)
    #leftIndex.attach(rightController, 6, 170, 90)
    #leftMajeure.attach(rightController, 4, 170, 90)
    #leftRingFinger.attach(rightController, 3, 170, 90)
    #leftPinky.attach(rightController, 2, 170, 90)

def attachStomach():
    print("Attaching stomach...")
    stomachTilt.attach(leftController, 27, 97, 70) # upright
    stomachRotate.attach(leftController, 28, 90, 70) # forward

def attachNeopixel():
    print("Attaching neopixel...")
    neopixel.attach(nanoController, 3, 16, 4) # pin 3, 16 pixels, 4 channel colour depth
    
def detachHead():
    print("Detaching head...")
    jaw.detach()
    neckRotate.detach()
    neckTilt.detach()
    eyesX.detach()
    eyesY.detach()
    print("Head detached.")

def detachArms():
    print("Detaching arms...")
    #rightOmoplate.detach()
    rightShoulder.detach()
    rightRotate.detach()
    #rightElbow.detach()
    #rightWrist.detach()
    #rightThumb.detach()
    #rightIndex.detach()
    #rightMajeure.detach()
    #rightRingFinger.detach()
    #rightPinky.detach()
    #leftOmoplate.detach()
    leftShoulder.detach()
    leftRotate.detach()
    #leftElbow.detach()
    #leftWrist.detach()
    #leftThumb.detach()
    #leftIndex.detach()
    #leftMajeure.detach()
    #leftRingFinger.detach()
    #leftPinky.detach()

def detachStomach():
    print("Detaching stomach...")
    stomachTilt.detach()
    stomachRotate.detach()
    
def neckTiltDemo():
    print("Neck tilt demo...")
    neckTilt.moveTo(45) # look up
    sleep(1)
    neckTilt.moveTo(135) # look down
    sleep(2)
    neckTilt.moveTo(95) # look forward
    sleep(2)
    
def eyesDemo():
    print("Eyes demo...")
    eyesY.moveTo(50)
    sleep(1)
    eyesY.moveTo(90)
    sleep(1)
    eyesY.moveTo(70)
    sleep(1)

def lookAround():
    print("look around...")
    neckRotate.moveTo(165)
    neckTilt.moveTo(50)
    sleep(2)
    neckRotate.moveTo(95)
    sleep(2)
    neckTilt.moveTo(90)
    sleep(2)

def lookAroundDown():
    neckRotate.moveTo(45)
    neckTilt.moveTo(135)
    sleep(2)
    neckRotate.moveTo(95)
    sleep(2)
    neckTilt.moveTo(90)
    sleep(1)

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

def closeFingers():
    print("close fingers") 
    rightThumb.moveTo(0)
    rightIndex.moveTo(0)
    rightMajeure.moveTo(0)
    rightFinger.moveTo(0)
    rightPinky.moveTo(0)

def openFingers():
    print("open fingers") 
    rightThumb.moveTo(170)
    rightIndex.moveTo(170)
    rightMajeure.moveTo(170)
    rightRingFinger.moveTo(170)
    rightPinky.moveTo(170)

BLACK = ["Black", 0, 0, 0]
BLUE = ["Blue", 0, 0, 255]
CYAN = ["Cyan", 0, 255, 255]
GREEN = ["Green", 0, 255, 0]
MAGENTA = ["Magenta", 255, 0, 255]
RED = ["Red", 255, 0, 0]
WHITE = ["White", 255, 255, 255]
YELLOW = ["Yellow", 255, 255, 0]
PINK = ["Pink", 255, 55, 55]
ORANGE = ["Orange", 255, 55, 0]
PURPLE = ["Purple", 60, 0, 255]

def neoDemo():
    colours = [RED, GREEN, BLUE]
    animations = ["Color Wipe", "Larson Scanner", "Theater Chase", "Theater Chase Rainbow", "Rainbow", "Rainbow Cycle", "Flash Random", "Ironman"]
    speed = 1
    for colour in colours:
        for animation in animations:
            print "Running neopixel animation: " + animation + " in " + colour[0]
            neopixel.setAnimation(animation, colour[1], colour[2], colour[3], speed)
            sleep(2)
    neoStop()

def neoStart(animation, colour, speed = 1):
    neo = Runtime.getService("NeoPixel")
    neo.setAnimation(animation, colour[1], colour[2], colour[3], speed)
    
def neoStop():
    print("stopping neopixel annimation...")
    neopixel.animationStop()
    neoColour(BLACK)

def neoColour(colour):
  print colour[0]
  for pixel in range (1, neopixel.numPixel + 1):
      neopixel.setPixel(pixel, colour[1], colour[2], colour[3])
  neopixel.writeMatrix()

def neoAnimate(animation, colour, time = 2, speed = 1):
    neoStart(animation, colour, speed)
    sleep(time)
    neoStop()
    
def publishSense(event):
  if event:
    print "Human detected !!!"
    neoColour("Red")
  else:
    neoColour("Green")

#pir.addListener("publishSense", python.name, "publishSense")

sleep(1)

# ready status
attachNeopixel()
neoColour(GREEN)
print("Ready")
