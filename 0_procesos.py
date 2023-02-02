from time import sleep
form random import random

from multiprocessing import Process

def f():
    for i in range(5) :
        print ("hola", i)
        sleep(random())

if __name__ == "_main_":
    p = Process(target=f)
    q = Process(target=f)
    p.start()
    q.start()
    print("fin")
    
