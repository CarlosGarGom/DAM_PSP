import socket
import threading
import struct
import time
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Configuración
HOST = "0.0.0.0"
PORT = 12345
BUFFER_SIZE = 4096
LOG_FILE = "log_servidor.txt"

def registrar_log(ip, puerto, archivo):
    """Registra la conexión en un archivo de log"""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - Conexión desde {ip}:{puerto} - Archivo: {archivo}\n")

def descifrar_archivo(datos_cifrados, key, iv):
    """Descifra los datos con AES-CBC"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    datos_padded = decryptor.update(datos_cifrados) + decryptor.finalize()

    # Eliminar el relleno PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    datos = unpadder.update(datos_padded) + unpadder.finalize()

    return datos

def manejar_cliente(cliente_socket, direccion):
    """Maneja la comunicación con un cliente"""
    print(f"Conexión establecida desde {direccion}")

    # Recibir clave AES y IV
    key_iv = cliente_socket.recv(48)
    key, iv = key_iv[:32], key_iv[32:]

    # Recibir nombre del archivo
    nombre_size = struct.unpack("I", cliente_socket.recv(4))[0]
    nombre_archivo = cliente_socket.recv(nombre_size).decode()

    # Recibir tamaño del archivo
    tamaño_archivo = struct.unpack("Q", cliente_socket.recv(8))[0]

    # Recibir datos cifrados
    datos_cifrados = b""
    while len(datos_cifrados) < tamaño_archivo:
        datos_cifrados += cliente_socket.recv(BUFFER_SIZE)

    # Descifrar el archivo
    datos_descifrados = descifrar_archivo(datos_cifrados, key, iv)

    # Guardar archivo descifrado
    with open(f"recibido_{nombre_archivo}", "wb") as archivo:
        archivo.write(datos_descifrados)

    print(f" Archivo '{nombre_archivo}' recibido y descifrado con éxito.")

    # Registrar en el log
    registrar_log(direccion[0], direccion[1], nombre_archivo)

    cliente_socket.close()

def iniciar_servidor():
    """Inicia el servidor y espera conexiones de clientes"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen(5)
        print(f" Servidor escuchando en {HOST}:{PORT}")

        while True:
            cliente_socket, direccion = servidor.accept()
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
            hilo_cliente.start()

if __name__ == "__main__":
    iniciar_servidor()
