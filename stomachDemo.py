
# Attach
attachStomach()
neoStart("Theater Chase", PURPLE)

# Move one way
stomachTilt.moveTo(115)
stomachRotate.moveTo(115)
sleep(2)

# Move the other way
stomachTilt.moveTo(75)
stomachRotate.moveTo(75)
sleep(4)

# return to center
stomachTilt.moveTo(97)
stomachRotate.moveTo(90)
sleep(2)

# Detach
neoStop()
neoColour(GREEN)
detachStomach()
