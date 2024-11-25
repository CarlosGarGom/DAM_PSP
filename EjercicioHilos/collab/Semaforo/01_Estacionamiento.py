import random
import threading
import time

# Crear un semáforo con capacidad de 3
semaforo = threading.Semaphore(3)

def acceder_estacionamiento(id_vehiculo):
    print(f"Vehiculo {id_vehiculo} intentando entrar al estacionamiento...")
    semaforo.acquire()  # Adquirir el semáforo para entrar al aparcamiento
    print(f"Vehiculo {id_vehiculo} ha entrado al estacionamiento.")
    time.sleep(random.uniform(1, 3))  # Simular tiempo en el aparcamiento
    print(f"Vehiculo {id_vehiculo} ha salido del estacionamiento.")
    semaforo.release()  # Liberar el semáforo para permitir que otro entre

# Crear e iniciar varios hilos (vehiculos)
vehiculos = []
for i in range(10):  # Simulamos 10 vehiculos intentando entrar al estacionamiento
    t = threading.Thread(target=acceder_estacionamiento, args=(i,))
    vehiculos.append(t)
    t.start()

# Esperar a que todos los hilos terminen
for t in vehiculos:
    t.join()

print("Todos han pasado por la sala.")