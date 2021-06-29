import time
from playsound import playsound
import json

with open('timer.json') as t:
    timers = json.load(t)

class ultilitarios:
    def linha():
        print("<------------------------------------------------------------------------------->")
    
    def esctrab():
        ultilitarios.linha()
        while True:
            inic = input("qual a opção que voce deseja:\np = programar nova rotina\ni = iniciar uma rotina pre programada\nd = deletar rotina\ns = sair\nR: ")
            if inic == "p" or inic == "i" or inic == "s" or inic == "d":break
        ultilitarios.linha()
        return inic
    
    def esctimer():
        ultilitarios.linha()
        while True:
            inic = input("qual a opção que voce deseja:\na = alarme simples\nd = alarme duplo\ndr = alarme duplo com repetição\ns = sair\nR: ")
            if inic == "s" or inic == "d" or inic == "dr" or inic == "a":break
        ultilitarios.linha()
        return inic
    
    def escrita():
        with open('timer.json','w') as t:
            json.dump(timers,t)


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
    def adicionatimer(nome,t1,t2):
        local = timers['end']+1
        timers['times'].append({"i": local,"nome":f"{nome}","tempo1": t1,"tempo2": t2})
        timers['end'] = local
        ultilitarios.escrita()
        print("feito!")
    def iniciarTimer(i,r):
        for t in timers["times"]:
            if i == t["i"]:
                tempo.timercr(t["tempo1"],t["tempo2"],r)
    def retornatimer():
        return timers["times"]
    def deleta():
        nomes = []
        for nome in timers['times']:
            nomes.append(nome['nome'])
        print("lista para escolher o que deletar")
        for t in range(len(nomes)):
            print("i:",t,"nome: ",nomes[t])
        while True:
            print("obs: as opções ate 2 são protegidas e não são deletaveis")
            selection = int(input("qual o indice do deletado: "))
            if selection > 2: break
        timers['times'].pop(selection)
        ultilitarios.escrita()