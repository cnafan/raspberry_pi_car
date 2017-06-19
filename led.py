import RPi.GPIO
import time

# 正常呼吸为3s一次，深呼吸6s一次
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18, RPi.GPIO.OUT)

pwm = RPi.GPIO.PWM(18, 50)
pwm.start(0)
try:
    while True:
        for i in range(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.01)
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.01)
except KeyboardInterrupt:
    pass

pwm.stop()

RPi.GPIO.cleanup()
