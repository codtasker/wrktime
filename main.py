#importando as classes que vou usar
import classes as c


#perguntando o modo que o usuario deseja
while True:
    op = input('alarme ou modo trabalho(a = alarme r = rotina): ')
    if op == "a" or op == "r":break


#modo alarme
if op == "a":
    
    while True:
        inic = c.ultilitarios.esctimer()

        if inic == 'a':
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
        else:break

#modo trabalho
else:
    while True:
        inic = c.ultilitarios.esctrab()

        if inic == "p":
            nome = input("digite o nome da nova rotina: ")
            t1 = int(input("digite o tempo da primeira tarefa: "))
            t2 = int(input("digite o tempo da segunda tarefa: "))
            c.trabalho.adicionatimer(nome,t1,t2)

        elif inic == "i":
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
        elif inic == "d":
            c.trabalho.deleta()
        else:break