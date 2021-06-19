from os import times
import time
from playsound import playsound
import json

with open('timer.json') as t:
    timers = json.load(t)


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

class trabalho:
    def alterartimers(nome,t1,t2):
        timers["times"].append({"i":len(timers[times])+1,"nome":nome,"tempo1":t1,"tempo2":t2})
        print(timers["times"])
    def iniciarTimer(i,r):
        for t in timers["times"]:
            if i == t["i"]:
                tempo.timercr(t["tempo1"],t["tempo2"],r)
    def retornatimer():
        return timers["times"]

class ultilitarios:
    def linha():
        print("<------------------------------------------------------------------------------->")

print(len(timers["times"]))
print(type(timers["times"]))
trabalho.alterartimers("normie",1,2)