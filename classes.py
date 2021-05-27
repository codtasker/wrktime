import time
from playsound import playsound
class tempo:
    def timer(timer):
        minu = 0
        while True:
            if minu != timer:
                time.sleep(60)
                minu = minu + 1
                print(minu," min")
            else:
                playsound('alarme/alarme.mp3')
                break
    def timercomparador(timer1,timer2):
        tempo.timer(timer1)
        tempo.timer(timer2)
    def timercr(timer1,timer2,r):
        for i in range(r):
            tempo.timer(timer1)
            tempo.timer(timer2)