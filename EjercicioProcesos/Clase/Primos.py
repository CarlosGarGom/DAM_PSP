import threading
# 0-1000 primos con 10 hilos
#calcular los numeros primos que hay del 0-n con  10 hilos
   #
hilos = []
lock = threading.Lock()

def calcularPrimo():
    global primo
def main():
    cantidad=input("Dime la cantidad de numeros primos para calcular")
    cantidad = int(cantidad)
    for _ in range(10):
        hilo = threading.Thread(target=primeros_n_primos(cantidad))

    print(primeros_n_primos(cantidad))


def es_primo(num):
    """Determina si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeros_n_primos(n):
    """Devuelve una lista con los primeros n números primos."""
    primos = []
    num = 2  # El primer número primo
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos



if __name__ == "__main__":
    main()


