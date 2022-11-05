attachHead()
neckTilt.moveTo(140)
sleep(1)
mouth = Runtime.getService("MarySpeech")
mouth.speakBlocking("Hello George.")
sleep(1)
mouth.speakBlocking("What do you have there?")
sleep(20)

mouth.speakBlocking("Hello friend! What is your name?")
sleep(20)

mouth.speakBlocking("Hello air a lot.")
neckTilt.moveTo(95)
detachHead()

