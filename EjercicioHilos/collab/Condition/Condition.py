import threading

# Contador compartido para controlar la secuencia
contador = 1  # 1: Preparación, 2: Procesamiento, 3: Empaque
cond = threading.Condition()

def preparacion():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 1)
            print(f"Preparación {i} completada")
            contador = 2
            cond.notify_all()

def procesamiento():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 2)
            print(f"Procesamiento {i} completado")
            contador = 3
            cond.notify_all()

def empaque():
    global contador
    for i in range(1, 6):
        with cond:
            cond.wait_for(lambda: contador == 3)
            print(f"Empaque {i} completado")
            contador = 1
            cond.notify_all()

# Creación de hilos
t1 = threading.Thread(target=preparacion)
t2 = threading.Thread(target=procesamiento)
t3 = threading.Thread(target=empaque)

# Inicia los hilos
t1.start()
t2.start()
t3.start()

# Espera a que todos los hilos terminen
t1.join()
t2.join()
t3.join()


