import RPi.GPIO as GPIO
import time

# trig 23
# echo 24
Trig_Pin = 23
Echo_Pin = 24


def init_hy():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo_Pin, GPIO.IN)


def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 / 2


if __name__ == '__main__':
    init_hy()
    GPIO.setwarnings(False)
    try:
        while True:
            print((checkdist() < 0.5))
            print('Distance:%0.2f m' % checkdist())
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
