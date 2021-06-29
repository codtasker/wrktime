from os import times
import time
from playsound import playsound
import json

with open('timer.json') as t:
    timers = json.load(t)
timers["times"]

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
        local = len(timers["times"])+1
        timers['times'].append({"i": f"{local}","nome":f"{nome}","tempo1": f"{t1}","tempo2": f"{t2}"})
        with open('timer.json','w') as t:
            json.dump(timers,t)
        print("feito!")
    def iniciarTimer(i,r):
        for t in timers["times"]:
            if i == t["i"]:
                tempo.timercr(t["tempo1"],t["tempo2"],r)
    def retornatimer():
        return timers["times"]

class ultilitarios:
    def linha():
        print("<------------------------------------------------------------------------------->")



