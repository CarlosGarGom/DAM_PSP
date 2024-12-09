import threading
import queue
import time
import random

# Tamaño máximo de la cola
tamano_cola = 5
cola_pedidos = queue.Queue(maxsize=tamano_cola)

# Variable compartida para contar los pedidos generados
pedidos_totales = 0
pedidos_totales_lock = threading.Lock()
MAX_PEDIDOS = 15

def cliente(id_cliente):
    global pedidos_totales

    while True:
        with pedidos_totales_lock:
            if pedidos_totales >= MAX_PEDIDOS:
                break

            pedidos_totales += 1
            id_pedido = f"Pedido-{pedidos_totales}"

        cola_pedidos.put(id_pedido)
        print(f"Cliente {id_cliente}: Generó {id_pedido}")

        # Pausa entre 1 y 2 segundos
        time.sleep(random.uniform(1, 2))

def empleado(id_empleado):
    while True:
        try:
            pedido = cola_pedidos.get()  # Espera por un pedido
        except queue.Empty:
            with pedidos_totales_lock:
                if pedidos_totales >= MAX_PEDIDOS and cola_pedidos.empty():
                    break
                continue

        print(f"Empleado {id_empleado}: Procesó {pedido}")
        cola_pedidos.task_done()

        # Pausa entre 2 y 3 segundos
        time.sleep(random.uniform(2, 3))

# Crear y lanzar hilos de forma mas breve y a la vez
clientes = [threading.Thread(target=cliente, args=(i,)) for i in range(1, 4)]
empleados = [threading.Thread(target=empleado, args=(i,)) for i in range(1, 3)]


for hilo in clientes + empleados:
    hilo.start()

for hilo in clientes + empleados:
    hilo.join()

print("Todos los pedidos han sido procesados.")
