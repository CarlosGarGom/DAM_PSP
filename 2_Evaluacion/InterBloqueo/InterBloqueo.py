import threading
import time

# Creamos dos locks como recursos y un lock intermediario
recurso_1 = threading.Lock()
recurso_2 = threading.Lock()
lock_intermediario = threading.Lock()

def hilo_a():
    with lock_intermediario:  # Coordinamos el acceso a los recursos
        with recurso_1:
            print("Hilo-A ha bloqueado Recurso-1")
            time.sleep(1)
            with recurso_2:
                print("Hilo-A ha bloqueado Recurso-2")
                time.sleep(1)

def hilo_b():
    with lock_intermediario:  # Coordinamos el acceso a los recursos
        with recurso_2:
            print("Hilo-B ha bloqueado Recurso-2")
            time.sleep(1)
            with recurso_1:
                print("Hilo-B ha bloqueado Recurso-1")
                time.sleep(1)

# Crear e iniciar los hilos
hilo1 = threading.Thread(target=hilo_a)
hilo2 = threading.Thread(target=hilo_b)

hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()
