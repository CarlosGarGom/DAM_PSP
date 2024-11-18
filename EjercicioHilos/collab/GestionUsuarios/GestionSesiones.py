import threading
import time


# Clase que maneja la sesión de usuario
class SesionUsuario:
    def __init__(self):
        self.nombre_usuario = None

    def iniciar_sesion(self, nombre_usuario):
        """Almacena el nombre de usuario en la sesión."""
        self.nombre_usuario = nombre_usuario
        print(f"Sesión iniciada para el usuario: {self.nombre_usuario}")

# Objeto threading.local para almacenar datos específicos del hilo
datos_sesion = threading.local()


# Función que simula la gestión de la sesión en cada hilo
def gestionar_sesion(nombre_usuario):
    # Crear una instancia de SesionUsuario específica para este hilo
    datos_sesion.sesion = SesionUsuario()

    # Iniciar sesión con el nombre de usuario proporcionado
    datos_sesion.sesion.iniciar_sesion(nombre_usuario)

    # Simular procesamiento con una pausa aleatoria
    time.sleep(1)


def main():
    # Lista de nombres de usuarios
    usuarios = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

    # Crear e iniciar un hilo para cada usuario
    hilos = []
    for usuario in usuarios:
        hilo = threading.Thread(target=gestionar_sesion, args=(usuario,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Todas las sesiones han sido terminadas.")


if __name__ == "__main__":
    main()
