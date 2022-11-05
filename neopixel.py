nanoPort = "/dev/ttyUSB0"
nanoController = Runtime.start("nanoController", "Arduino")
nanoController.connect(nanoPort);

neopixel = Runtime.start("NeoPixel", "NeoPixel")
neopixel.attach(nanoController, 3, 16, 4)
print(neopixel.numPixel)
neopixel.setAnimation(2, 255, 0, 0, 1)