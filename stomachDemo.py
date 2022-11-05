
# Attach
attachStomach()
neoStart("Theater Chase", PURPLE)

# Move one way
stomachTilt.moveTo(105)
stomachRotate.moveTo(110)
sleep(2)

# Move the other way
stomachTilt.moveTo(75)
stomachRotate.moveTo(70)
sleep(4)

# return to center
stomachTilt.moveTo(90)
stomachRotate.moveTo(90)
sleep(2)

# Detach
neoStop()
neoColour(GREEN)
detachStomach()
