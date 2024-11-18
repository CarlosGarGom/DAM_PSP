import threading
import time
import random

# Gestión de Usuarios en Hilos con args y kwargs
# Doble asterisco para que espere dos parametros
def procesar_usuario(user_id, **user_info):
    """Simula el procesamiento de un usuario con args y kwargs."""
    nombre = user_info.get('nombre', 'Desconocido')
    edad = user_info.get('edad', 'No especificada')
    print(f"Usuario ID {user_id}: Nombre: {nombre}, Edad: {edad}")

    # Pausa aleatoria para simular procesamiento
    tiempo = random.uniform(0.5, 2.0)
    time.sleep(tiempo)
    print(f"Usuario ID {user_id} procesado en {tiempo:.2f} segundos")


def main():
    # Lista de usuarios con ID, nombre y edad
    usuarios = [
        (1, {"nombre": "Beatriz", "edad": 25}),
        (2, {"nombre": "Ana", "edad": 30}),
        (3, {"nombre": "Carlos", "edad": 35}),
        (4, {"nombre": "Diana", "edad": 28}),
        (5, {"nombre": "David", "edad": 22}),
    ]

    # Crear e iniciar un hilo para cada usuario
    hilos = []
    for user_id, user_info in usuarios:
        hilo = threading.Thread(target=procesar_usuario, args=(user_id,), kwargs=user_info)
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Todos los usuarios han sido procesados.")


if __name__ == "__main__":
    main()
