import threading
import time

# Crear un evento
señal_salida = threading.Event()

class Corredor(threading.Thread):
    def __init__(self,num):
        super().__init__()
        self.num=num

    def run(self):
        print(f"Corredor {self.num} en posición, esperando señal de la salida...")
        señal_salida.wait()  # Espera a que la señal se active
        print(f"Corredor {self.num} ha llegado a la meta!")



def activar_salida():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)  # Simular tiempo antes de activar la salida
    señal_salida.set()  # Activa el evento, permitiendo que todos los corredores continúen
    print("¡Salida! Los corredores han comenzado.")

# Activar la salida después de un tiempo
salida = threading.Thread(target=activar_salida)
salida.start()

# Crear e iniciar un hilo para cada archivo en la lista
hilos = []
for i in range(1,5):
    hilo = Corredor(i)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()




print("Todos los corredores han terminado.")
