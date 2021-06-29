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
        timers['times'].append({"i": local,"nome":f"{nome}","tempo1": t1,"tempo2": t2})
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
    
    def esctrab():
        ultilitarios.linha()
        while True:
            inic = input("qual a opção que voce deseja:\np = programar nova rotina\ni = iniciar uma rotina pre programada\ns = sair\nR: ")
            if inic == "p" or inic == "i" or inic == "s":break
        ultilitarios.linha()
        return inic
    
    def esctimer():
        ultilitarios.linha()
        while True:
            inic = input("qual a opção que voce deseja:\na = alarme simples\nd = alarme duplo\ndr = alarme duplo com repetição\ns = sair\nR: ")
            if inic == "s" or inic == "d" or inic == "dr" or inic == "a":break
        ultilitarios.linha()
        return inic


