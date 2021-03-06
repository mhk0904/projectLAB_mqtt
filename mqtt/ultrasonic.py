import RPi.GPIO as GPIO 
import time
TRIG_PIN = 20 
ECHO_PIN = 21

def initUltrasonic():
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def controlUltrasonic():
    distance = 0.0
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.5)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    while GPIO.input(ECHO_PIN) == 0 :
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1 :
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    return distance

def main():
    GPIO.setmode(GPIO.BCM)
    distance = 0.0
    initUltrasonic()
    print ("Ultrasonic Operating ...")
    try:
        while True:
            distance = controlUltrasonic()
            print("Distance:%.2f cm"%distance)
    except KeyboardInterrupt: GPIO.cleanup()
    GPIO.cleanup()

if __name__ == '__main__':
    main()