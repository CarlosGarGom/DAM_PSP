import threading
import time
# se ejecuta de forma intercalada de no ser por el lock
lock = threading.Lock()
def imprimir_numeros():
    with lock:
        for i in range(1,6):

            print(f"{threading.current_thread().name} - {i}")
            time.sleep(1)

hilo_a = threading.Thread(target=imprimir_numeros, name="Hilo-A")
hilo_b = threading.Thread(target=imprimir_numeros, name="Hilo-B")
hilo_c = threading.Thread(target=imprimir_numeros, name="Hilo-C")

hilo_a.start()
hilo_b.start()
hilo_c.start()

hilo_a.join()
hilo_b.join()
hilo_c.join()

print("Todos los hilos han terminado.")