from playsound3 import playsound
from networktables import NetworkTables
import time

if False:
    NetworkTables.initialize(server='roboRIO-3200-FRC.local')
else:
    NetworkTables.initialize(server='127.0.0.1')

nt = NetworkTables.getTable('RobotState')
soundPlayed = False

time.sleep(0.5)
while True:
    if nt.getBoolean("disabled", "Not Found"):
        if soundPlayed == False:
            playsound("im disabled-Audio (High).mp3")
            soundPlayed = True
        else:
            print("Disabled")
    else:
        print("Not Disabled")
        soundPlayed = False
