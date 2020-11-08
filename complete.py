import time

# Serial ports
leftPort = ""
rightPort = ""
nanoPort = ""

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
# stomach             left         TBC
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
time.sleep(3);

print("Initialising all servos...")
jaw = Runtime.start("jaw", "Servo")
neckRotate = Runtime.start("neckRotate", "Servo")
neckTilt = Runtime.start("neckTilt", "Servo")
eyesX = Runtime.start("eyesX", "Servo")
eyesX = Runtime.start("eyesY", "Servo")

print("Initialising pir")
pir = Runtime.start('pir', 'Pir')
pir.attach(rightController, 12)
pir.isVerbose = True
pir.enable(1) # 1 is how many time / second we poll the pir

def attachHead():
    jaw.attach(rightController, 53, 174) # closed
    neckRotate.attach(rightController, 51, 95, 60) # forward
    neckTilt.attach(rightController, 49, 95, 60) # forward
    eyesX.attach(rightController, 47, 90) # unkown
    eyesY.attach(rightController, 45, 70, 50) # forward

def attachArms():
    print("Attaching arms...")
    rightOmoplate.attach(rightController, 9, 80)
    rightShoulder.attach(rightController, 10, 0, 80)
    rightRotate.attach(rightController, 11, 90, 80)
    rightElbow.attach(rightController, 8, 0, 80)
    rightWrist.attach(rightController, 7, 170, -1.0)
    rightThumb.attach(rightController, 5, 170, 90)
    rightIndex.attach(rightController, 6, 170, 90)
    rightMajeure.attach(rightController, 4, 170, 90)
    rightRingFinger.attach(rightController, 3, 170, 90)
    rightPinky.attach(rightController, 2, 170, 90)

def attachNeopixel():
    neopixel.attach(nano, 3, 16)
    
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
    
def neopixelStart():
    red = ["red", 255, 0, 0]
    green = ["green", 0, 255, 0]
    blue = ["blue", 0, 0, 255]
    colours = [red, green, blue]
    animations = ["Color Wipe", "Larson Scanner", "Theater Chase", "Theater Chase Rainbow", "Rainbow", "Rainbow Cycle", "Flash Random", "Ironman"]
    speed = 1
    for colour in colours:
        for animation in animations:
            neopixel.setAnimation(animation, colour[1], colour[2], colour[3], speed)
            print "Running neopixel animation: " + animation + " in " + colour[0]

def neopixelStop():
    neopixel.animationStop()

def neoColour(colour):
  print colour
  if (colour == "Red"):
    for pixel in range (1, neopixel.numPixel + 1):
      neopixel.setPixel(pixel, 255, 0, 0)
    neopixel.writeMatrix()
  if (colour == "Green"):
    for pixel in range (1, neopixel.numPixel + 1):
      neopixel.setPixel(pixel, 0, 255, 0)
    neopixel.writeMatrix()
    
def publishSense(event):
  if event:
    print "Human detected !!!"
    neoColour("Red")
  else:
    neoColour("Green")

pir.addListener("publishSense", python.name, "publishSense")

time.sleep(4)

# complete demo
neopixelStart()
headDemo()
neopixelStop()

