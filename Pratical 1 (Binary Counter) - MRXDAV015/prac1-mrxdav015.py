"""
David Moore
MRXDAV015
Practical 1 (Binary Counter)
23/07/2019
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#Pin Declarations
power = 2
ground = 6   
increment = 36
decrement = 38
LED1 = 15
LED2 = 13
LED3 = 11 
presses = 0

#set mode   
GPIO.setmode(GPIO.BOARD)
    #setup output pins
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
    #setup input pins
GPIO.setup(increment, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(decrement, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def initializePins():   
    #set mode   
    GPIO.setmode(GPIO.BOARD)
    #setup output pins
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)
    #setup input pins
    GPIO.setup(increment, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(decrement, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Increment(channel):
    global presses
    if presses == 7:
        presses = 0

    else:
        presses = presses + 1

def Decrement(channel):
    global presses
    if presses == 0:
        presses = 7

    else:
        presses = presses - 1

GPIO.add_event_detect(increment,GPIO.RISING,callback= Increment,bouncetime=300)  

GPIO.add_event_detect(decrement,GPIO.RISING,callback=Decrement,bouncetime=300)  

def main():
    initializePins()

    if presses == 0:
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.LOW)

    elif presses == 1:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.LOW)

    elif presses == 2:
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.LOW)

    elif presses == 3:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.LOW)

    if presses == 4:
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.HIGH)

    if presses == 5:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.HIGH)

    if presses == 6:
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.HIGH)

    if presses == 7:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.HIGH)
        GPIO.output(LED3, GPIO.HIGH)

    
    
if __name__ == "__main__":
    try:
        while 1:
            main()

    except KeyboardInterrupt: 
        GPIO.cleanup()

    except:
        print("shit, something ain't working")
    


	
