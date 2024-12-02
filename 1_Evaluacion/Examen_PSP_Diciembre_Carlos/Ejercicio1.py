import random
import threading
import time

semaforo = threading.Semaphore(2)

def festivaleros():
    for i in range(1,5):
        print(f"Festivalero {i} esta esperando un cajero")
        semaforo.acquire()
        print(f" Festivalero {i} esta usando el cajero")
        time.sleep(random.uniform(1,3))
        print(f" Festivalero {i} ha terminado y ha liberado el cajero")
        semaforo.release()


t1=threading.Thread(target=festivaleros())
t1.start()
t1.join()
