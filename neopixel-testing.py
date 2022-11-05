def neoAnimation(animation, red, green, blue, colour):
    text = "Testing " + colour
    mouth = Runtime.getService("MarySpeech")
    mouth.speakBlocking(text)
    neoPixel = Runtime.getService("NeoPixel")
    neoPixel.setAnimation(animation, red, green, blue, 1)
    sleep(2)
    neopixel.animationStop()
    
attachHead()
mouth = Runtime.getService("MarySpeech")
mouth.speakBlocking("Testing my neopixel")

neoAnimation(2, 255, 0, 0, "Red")
neoAnimation(2, 255, 50, 0, "Orange")
neoAnimation(2, 255, 121, 0, "Yellow")
neoAnimation(2, 0, 255, 0, "Green")
neoAnimation(2, 0, 0, 255, "Blue")
neoAnimation(2, 255, 0, 255, "Purple")
mouth.speakBlocking("Testing complete")
detachHead()