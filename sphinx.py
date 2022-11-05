from org.myrobotlab.service import Sphinx

ear = Runtime.createAndStart("ear", "Sphinx")
ear.startListening("hello")
ear.addCommand("hello", "python", "respond")

def respond(phrase):
    print "This is the hello function..."
    print phrase

print "Listening..."