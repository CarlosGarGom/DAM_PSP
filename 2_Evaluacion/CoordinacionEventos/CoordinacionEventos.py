import threading
import time

# Crear un evento
señal_salida = threading.Event()

def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posición, esperando señal de la salida...")
    señal_salida.wait()  # Espera a que la señal se active
    print(f"Corredor {id_corredor} ha llegado a la meta!")

def activar_salida():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)  # Simular tiempo antes de activar la salida
    señal_salida.set()  # Activa el evento, permitiendo que todos los corredores continúen
    print("¡Salida! Los corredores han comenzado.")

# Crear e iniciar hilos para 5 corredores
corredores = []
for i in range(5):
    t = threading.Thread(target=corredor, args=(i,))
    corredores.append(t)
    t.start()

# Activar la salida después de un tiempo
salida = threading.Thread(target=activar_salida)
salida.start()

# Esperar a que todos los hilos/corredoresw terminen
for t in corredores:
    t.join()
salida.join()

print("Todos los corredores han terminado.")