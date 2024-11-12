import threading
import time

# Definimos una clase que hereda de Thread para procesar archivos
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre_archivo, texto):
        super().__init__()
        self.nombre_archivo = nombre_archivo
        self.texto = texto
        self.lineas = texto.splitlines()  # Dividimos el texto en líneas

    def run(self):
        """Este método se ejecuta al iniciar el hilo."""
        for i, linea in enumerate(self.lineas, start=1):
            print(f"Procesando {self.nombre_archivo} - Línea {i}: {linea}")
            time.sleep(0.5)  # Simulamos el tiempo de procesamiento con una pausa

# Lista de nombres de archivos y contenido de texto
archivos = [
    ("archivo1.txt", "Esta es la primera línea del archivo 1.\nSegunda línea.\nTercera línea."),
    ("archivo2.txt", "Primera línea del archivo 2.\nSegunda línea."),
    ("archivo3.txt", "Archivo 3, línea 1.\nLínea 2.\nLínea 3.\nLínea 4.")
]

# Crear e iniciar un hilo para cada archivo en la lista
hilos = []
for nombre_archivo, texto in archivos:
    hilo = ProcesadorArchivo(nombre_archivo, texto)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los archivos han sido procesados.")
