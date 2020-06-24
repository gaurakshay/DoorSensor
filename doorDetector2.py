import RPi.GPIO as GPIO
import time
from pygame import mixer

mixer.init()
file = "/home/pi/Documents/doorDetector/test.wav"
#file = "test.wav"
sfile = mixer.Sound(file)
# sfile.play()
# while mixer.get_busy():
#     print("playing music file")
# 
# print("music file ended")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

name = "Test"
print("Hello " + name)

while True:
    if GPIO.input(18):
        if mixer.get_busy():
            # if busy, don't do anything
            pass
        else:
            sfile.play()
        print("Door is open")
        time.sleep(2)
    if GPIO.input(18) == False:
        if mixer.get_busy():
            # stop file if playing
            sfile.stop()
        print("Door is closed")
        time.sleep(2)