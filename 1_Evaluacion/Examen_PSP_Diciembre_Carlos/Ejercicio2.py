import threading
import time

contador = 1 # contador para saber a que corredor le toca
cond=threading.Condition()
# funcion para corredor
def corredor1():
    global contador
    #vueltas que va a dar
    for i in range(1,5):
        with cond:
            cond.wait_for(lambda: contador==1)
            print(f"Corredor 1 corriendo vuelta {i}")
            #notifica que el siguiente corredor salga
            contador = 2
            cond.notify_all()

def corredor2():
    global contador
    for i in range(1,5):
        with cond:
            cond.wait_for(lambda:contador==2)
            print(f"Corredor 2 corriendo vuelta {i}")
            contador = 3
            cond.notify_all()

def corredor3():
    global contador
    for i in range(1,5):
        with cond:
            cond.wait_for(lambda:contador==3)
            print(f"Corredor 3 corriendo vuelta {i}")
            contador = 4
            cond.notify_all()

def corredor4():
    global contador
    for i in range(1,5):
        with cond:
            cond.wait_for(lambda:contador==4)
            print(f"Corredor 4 corriendo vuelta {i}")
            contador = 1
            cond.notify_all()


t1=threading.Thread(target=corredor1)
t2=threading.Thread(target=corredor2)
t3=threading.Thread(target=corredor3)
t4=threading.Thread(target=corredor4)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()