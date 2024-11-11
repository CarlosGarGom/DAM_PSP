import threading

# Lista compartida para almacenar los números primos
primos = []

# Definir un lock para asegurar que los hilos no accedan simultáneamente a la lista compartida
lock = threading.Lock()

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función que cada hilo ejecutará para encontrar números primos en un sub-rango
def encontrar_primos(rango_inicio, rango_fin):
    global primos
    for num in range(rango_inicio, rango_fin + 1):
        if es_primo(num):
            # Asegurar acceso exclusivo a la lista compartida
            with lock:
                primos.append(num)

# Crear y dividir el rango 0-1000 en 10 sub-rangos
rango_total = 1000
cantidad_hilos = 10
rango_por_hilo = rango_total // cantidad_hilos
hilos = []

# Crear 10 hilos para cada sub-rango
for i in range(cantidad_hilos):
    rango_inicio = i * rango_por_hilo
    rango_fin = (i + 1) * rango_por_hilo - 1 if i != cantidad_hilos - 1 else rango_total
    hilo = threading.Thread(target=encontrar_primos, args=(rango_inicio, rango_fin))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Ordenar los números primos y mostrarlos
primos.sort()
print("Números primos entre 0 y 1000:", primos)
