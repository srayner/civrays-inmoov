
# Attach
attachStomach()
neoStart("Theater Chase", PURPLE)

# Move one way
stomachTilt.moveTo(110)
stomachRotate.moveTo(110)
sleep(2)

# Move the other way
stomachTilt.moveTo(75)
stomachRotate.moveTo(70)
sleep(4)

# return to center
stomachTilt.moveTo(97)
stomachRotate.moveTo(97)
sleep(2)

# Detach
neoStop()
neoColour(GREEN)
detachStomach()
