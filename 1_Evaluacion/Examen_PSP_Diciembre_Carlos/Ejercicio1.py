import random
import threading
import time

semaforo = threading.Semaphore(2)

def festivaleros(numFestivalero):

        print(f"Festivalero {numFestivalero} esta esperando un cajero")
        semaforo.acquire()
        print(f" Festivalero {numFestivalero} esta usando el cajero")
        time.sleep(random.uniform(1,3))
        print(f" Festivalero {numFestivalero} ha terminado y ha liberado el cajero")
        semaforo.release()

hilos = []
for i in range(1,5):
    t1=threading.Thread(target=festivaleros, args=(i,))
    hilos.append(t1)
    t1.start()

for t in hilos:
    t.join()


