attachHead()
neckTilt = Runtime.getService("neckTilt")
neckRotate = Runtime.getService("neckRotate")
mouth = Runtime.getService("MarySpeech")

mouth.speakBlocking("Welcome friends.")
mouth.speakBlocking("My Name is Ralph. Let me give to a demo of what I can do.")

mouth.speakBlocking("Look up")
neckTilt.moveTo(45)
sleep(3)

mouth.speakBlocking("Look forward")
neckTilt.moveTo(90)
sleep(3)

mouth.speakBlocking("Look down")
neckTilt.moveTo(135)
sleep(3)

mouth.speakBlocking("Look forward")
neckTilt.moveTo(90)
sleep(3)

mouth.speakBlocking("Look right")
neckRotate.moveTo(15)
sleep(3)

mouth.speakBlocking("Look forward")
neckRotate.moveTo(90)
sleep(3)

mouth.speakBlocking("Look left")
neckRotate.moveTo(170)
sleep(3)

mouth.speakBlocking("That is all for now. Thank you")
detachHead()
print("Finished")
