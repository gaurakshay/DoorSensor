# Write your code here :-)
from pygame import mixer

mixer.init()
file = "/home/pi/Documents/doorDetector/test.mp3"
#file = "test.wav"
sfile = mixer.Sound(file)
sfile.play()
while mixer.get_busy():
    print("playing music file")

print("music file ended")