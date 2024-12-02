import threading

# Lista compartida para almacenar los números primos
primos = []

# Definir un lock para asegurar acceso exclusivo a la lista compartida
lock = threading.Lock()

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función que cada hilo ejecutará para encontrar números primos
def encontrar_primos(rango_inicio, cantidad_primos_deseada):
    global primos
    num = rango_inicio
    while True:
        # Salir si ya se han encontrado suficientes primos
        with lock:
            if len(primos) >= cantidad_primos_deseada:
                break

        if es_primo(num):
            with lock:
                if len(primos) < cantidad_primos_deseada:
                    primos.append(num)
        num += 1

# Solicitar al usuario la cantidad de números primos que desea calcular
cantidad_primos_deseada = int(input("Introduce la cantidad de números primos que deseas calcular: "))

# Determinar el número de hilos a usar
cantidad_hilos = min(10, cantidad_primos_deseada)

# Crear y lanzar los hilos
hilos = []
for i in range(cantidad_hilos):
    # Dividir el trabajo de forma equitativa entre los hilos
    rango_inicio = 2 + i  # Empiezan en 2 (primer número primo)
    hilo = threading.Thread(target=encontrar_primos, args=(rango_inicio, cantidad_primos_deseada))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Ordenar y mostrar los números primos
primos.sort()
print("Números primos calculados:", primos[:cantidad_primos_deseada])
