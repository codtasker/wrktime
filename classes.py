import time
class tempo:
    def timer(tdt,tdd,tdf):
        #tdt = tempo de trabalho tdd = tempo de descanso tdf = final do timer
        minu = 0
        rminu = 0
        c = 0
        h = 0
        while True:
            if h != tdf:
                if minu != tdt and c == 0:
                    print("f")
                    time.sleep(60)
                    minu =+ 1
                    rminu =+ 1
                elif c == 0:
                    c = 1
                    minu = 0
                    print("y")
                elif minu != tdd and c == 1:
                    time.sleep(60)
                    minu =+ 1
                    rminu =+ 1
                elif c == 1:
                    c = 0
                    minu = 0
                    print("n")
            else:
                break
            if rminu == 60:
                h =+ 1

