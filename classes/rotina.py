import classes.ultilitario as ultilitario
import json
import classes.tempo as tempo

with open('timer.json') as t:
    timers = json.load(t)

def adicionatimer(nome,t1,t2):
    local = timers['end']+1
    timers['times'].append({"i": local,"nome":f"{nome}","tempo1": t1,"tempo2": t2})
    timers['end'] = local
    ultilitario.escrita(timers)
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
    ultilitario.escrita(timers)
    print("feito!")