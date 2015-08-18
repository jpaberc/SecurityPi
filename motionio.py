import RPi.GPIO as GPIO
import time
import pygame

print "PIR Module Test (CTRL+C to exit)"

GPIO.setmode(GPIO.BCM)

PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

pygame.mixer.init()
pygame.mixer.music.load('./sounds/alert.mp3')

def MOTION(PIR_PIN):
    print "Motion Detected!!"
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


try:
    print "Ready!"
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)

    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print ("Quitting")
    GPIO.cleanup()

