import classes as c
inic = input("qual a opção que voce deseja:\ns = alarme simples\nd = alarme duplo\ndr = alarme duplo com repetição\nR: ")
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