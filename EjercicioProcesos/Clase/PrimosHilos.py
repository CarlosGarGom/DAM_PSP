import threading


def es_primo(num):
    """Determina si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primeros_n_primos(n, resultado, indice):
    """Devuelve los primeros n números primos y los almacena en la lista resultado."""
    primos = []
    num = 2  # El primer número primo
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    resultado[indice] = primos  # Almacena el resultado en el índice correspondiente


def main():
    cantidad = input("Dime la cantidad de números primos para calcular: ")
    cantidad = int(cantidad)

    # Lista para almacenar los resultados de cada hilo
    resultados = [None] * 10  # 10 hilos
    hilos = []

    # Crear y lanzar 10 hilos
    for i in range(10):
        hilo = threading.Thread(target=primeros_n_primos, args=(cantidad // 10, resultados, i))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Combinar y mostrar todos los resultados
    primos_totales = [primo for sublista in resultados for primo in sublista if sublista is not None]

    print("Los primeros", cantidad, "números primos son:")
    print(primos_totales[:cantidad])  # Imprimir solo la cantidad solicitada


if __name__ == "__main__":
    main()
