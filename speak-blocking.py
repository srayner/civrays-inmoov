attachHead()
mouth = Runtime.getService("MarySpeech")
mouth.speakBlocking("This is an example of the speak blocking method.")
mouth.speakBlocking("See how the script waits for me to finish speaking.")
print('finished')
