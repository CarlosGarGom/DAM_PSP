import threading

# Contador compartido para controlar la secuencia
contador = 1  # 1: Preparación, 2: Procesamiento, 3: Empaque
cond = threading.Condition()

def corredor1():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 1)
            print(f"Corredor 1 Vuelta {i} completada")
            contador = 2
            cond.notify_all()

def corredor2():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 2)
            print(f"Corredor 2 Vuelta {i} completado")
            contador = 3
            cond.notify_all()

def corredor3():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 3)
            print(f"Corredor 3 Vuelta {i} completado")
            contador = 4
            cond.notify_all()
def corredor4():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 4)
            print(f"Corredor 4 Vuelta {i} completado")
            contador = 1
            cond.notify_all()

# Creación de hilos
t1 = threading.Thread(target=corredor1)
t2 = threading.Thread(target=corredor2)
t3 = threading.Thread(target=corredor3)
t4 = threading.Thread(target=corredor4)

# Inicia los hilos
t1.start()
t2.start()
t3.start()
t4.start()
# Espera a que todos los hilos terminen
t1.join()
t2.join()
t3.join()
t4.join()

