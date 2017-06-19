import RPi.GPIO as GPIO
import time


def initcar():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Left
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    # Right
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)


def forward():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(2, True)
    GPIO.output(3, True)
    GPIO.output(4, False)

    GPIO.output(10, True)
    GPIO.output(9, True)
    GPIO.output(11, False)


def test():
    pwm = GPIO.PWM(2, 80)
    pwm.start(90)
    GPIO.output(3, True)
    GPIO.output(4, True)
    while True:
        pwm.ChangeDutyCycle(90)
        time.sleep(3)
        pwm.ChangeDutyCycle(30)
        time.sleep(3)


def right_light():
    GPIO.setmode(GPIO.BCM)
    pwm = GPIO.PWM(2, 80)
    pwm.start(100)
    GPIO.output(3, True)
    GPIO.output(4, False)

    GPIO.output(10, True)
    GPIO.output(9, True)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(10)


def backward():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(4, True)

    GPIO.output(10, True)
    GPIO.output(9, False)
    GPIO.output(11, True)


def stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.output(2, True)
    GPIO.output(3, True)
    GPIO.output(4, True)

    GPIO.output(10, True)
    GPIO.output(9, True)
    GPIO.output(11, True)


def Right():
    GPIO.setmode(GPIO.BCM)

    GPIO.output(2, True)
    GPIO.output(3, True)
    GPIO.output(4, True)

    GPIO.output(10, True)
    GPIO.output(9, True)
    GPIO.output(11, False)


def Left():
    GPIO.output(2, True)
    GPIO.output(3, True)
    GPIO.output(4, False)

    GPIO.output(10, True)
    GPIO.output(9, True)
    GPIO.output(11, True)


def init_hy():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo_Pin, GPIO.IN)


def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 / 2


def test():
    pwm_r = GPIO.PWM(2, 80)
    pwm_r.start(50)
    pwm_l = GPIO.PWM(10, 80)
    pwm_l.start(50)
    GPIO.output(9, True)
    GPIO.output(11, False)
    GPIO.output(3, True)
    GPIO.output(4, False)
    pwm_r.ChangeDutyCycle(90)
    pwm_l.ChangeDutyCycle(30)
    time.sleep(3)


if __name__ == '__main__':

    carren = 2
    carrin1 = 3
    carrin2 = 4

    carlen = 10
    carlin1 = 9
    carlin2 = 11

    Trig_Pin = 23
    Echo_Pin = 24
    initcar()

    init_hy()
    while True:
        command = input('1.前进 2.后退 3.停止 4.左转 5.右转 6.右小转')
        if command == "1":
            while True:
                time.sleep(0.5)
                if checkdist() < 0.4:
                    forward()
                else:
                    stop()
                    break
        elif command == '2':
            backward()
            print(command)
        elif command == '3':
            stop()
            print(command)
        elif command == '4':
            Left()
            print(command)
        elif command == '5':
            Right()
            print(command)
        elif command == '6':
            test()
            print(command)
        else:
            print(command)
