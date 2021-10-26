import json

def linha():
        print("<------------------------------------------------------------------------------->")
    
def esctrab():
    linha()
    while True:
        inic = input("qual a opção que voce deseja:\np = programar nova rotina\ni = iniciar uma rotina pre programada\nd = deletar rotina\ns = sair\nR: ")
        if inic == "p" or inic == "i" or inic == "s" or inic == "d":break
    linha()
    return inic
    
def esctimer():
    linha()
    while True:
        inic = input("qual a opção que voce deseja:\na = alarme simples\nd = alarme duplo\ndr = alarme duplo com repetição\ns = sair\nR: ")
        if inic == "s" or inic == "d" or inic == "dr" or inic == "a":break
    linha()
    return inic
    
def escrita(timers):
    with open('timer.json','w') as t:
        json.dump(timers,t)