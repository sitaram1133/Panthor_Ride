
class Mains:
    ##import RPi.GPIO as GPIO
    from time import sleep
    import time, math

    import sys
    def init_GPIO(val = None):  # initialize GPIO
        ## GPIO.setmode(GPIO.BOARD)
        ## GPIO.setwarnings(False)
        ## GPIO.setup(sensor,GPIO.IN)
        print(".");

    def init_interrupt(val = None):
        # GPIO.add_event_detect(sensor, GPIO.RISEING, callback=calculate_elapse, bouncetime=20)
        print("GPIO received")
        while True:
            print('.')



