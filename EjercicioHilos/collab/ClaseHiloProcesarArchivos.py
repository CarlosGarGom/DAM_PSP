import threading
import time

lock = threading.Lock()
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre_archivo, texto):
        super().__init__()
        self.nombre_archivo = nombre_archivo
        self.texto = texto
        self.lineas = texto.splitlines()  # Dividimos el texto en líneas

    def run(self):
        """Este método se ejecuta al iniciar el hilo."""
        for i, linea in enumerate(self.lineas, start=1):
            print(f"Procesando {self.nombre_archivo} - Línea {i}")
            time.sleep(0.5)

# Lista de nombres de archivos y contenido de texto
archivos = [
    ("archivo1.txt", "Linea1.\nLinea2.\nLinea3."),
    ("archivo2.txt", "Linea1.\nLinea2."),
    ("archivo3.txt", "Línea1.")
]

# Crear e iniciar un hilo para cada archivo en la lista
hilos = []
for nombre_archivo, texto in archivos:
    hilo = ProcesadorArchivo(nombre_archivo, texto)
    hilos.append(hilo)
    hilo.start()
    hilo.join()



print("Todos los archivos han sido procesados.")
