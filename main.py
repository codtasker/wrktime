#importando as classes que vou usar
import classes as c


#perguntando o modo que o usuario deseja
while True:
    op = input('alarme ou modo trabalho(a = alarme t = trabalho): ')
    if op == "a" or op == "t":break

#modo alarme
if op == "a":
    while True:
        inic = input("qual a opção que voce deseja:\ns = alarme simples\nd = alarme duplo\ndr = alarme duplo com repetição\nR: ")
        if inic == "s" or inic == "d" or inic == "dr":break
    c.ultilitarios.linha()
    if inic == 's':
        t = int(input('quanto tempo voce quer: '))
        c.tempo.timer(t)
    elif inic == 'd':
        t = int(input('digite o tempo 1: '))
        t2 = int(input('digite o tempo 2: '))
        c.tempo.timercomparador(t,t2)
    elif inic == 'dr':
        t = int(input('digite o tempo 1: '))
        t2 = int(input('digite o tempo 2: '))
        repet = int(input('digite quantas vezes deve ser repetido: '))
        c.tempo.timercr(t,t2,repet)

#modo trabalho
else:
    while True:
        inic = input("qual a opção que voce deseja:\np = programar nova rotina\na = programados anteriormente\nR: ")
        if inic == "p" or inic == "a":break
    c.ultilitarios.linha()
    if inic == "p":
        pass
    else:
        timers = c.trabalho.retornatimer()
        print("lista de rotinas")
        for t in timers:
            print("[",t["i"],"] nome do timer: "+t["nome"]+" /primeira rotina: ",t["tempo1"]," /segunda rotina: ",t["tempo2"])
        c.ultilitarios.linha()
        while True:    
            try:
                i = int(input("qual o indice da rotina desejada: "))
                r = int(input("quantas repeticoes: "))
                c.trabalho.iniciarTimer(i,r)
                break
            except:print("digite novamente (erro)")