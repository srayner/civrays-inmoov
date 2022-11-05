attachHead()
neckRotate.moveTo(90)
mouth = Runtime.getService("MarySpeech")
mouth.speakBlocking("Hello George.")
sleep(3)

mouth.speakBlocking("What do you have there")
sleep(12)

mouth.speakBlocking("A hat. Is it for me?")
sleep(4)

mouth.speakBlocking("Thank you George and air a lot for the hat.")
detachHead()


