import time
from playsound import playsound

def timer(timer):
    minu = 0
    while True:
        if minu != timer:
            time.sleep(60)
            minu = minu + 1
            print(minu," min")
        else:
            playsound('classes/alarme/alarme.mp3')
            break
def timercomparador(timer1,timer2):
        timer(timer1)
        timer(timer2)
def timercr(timer1,timer2,r):
        for i in range(r):
            timer(timer1)
            timer(timer2)