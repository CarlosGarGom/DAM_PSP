import socket
import os
import struct
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import secrets

# Configuración del servidor
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
BUFFER_SIZE = 4096

# Clave y vector de inicialización para AES
KEY = secrets.token_bytes(32)  # Clave de 256 bits
IV = secrets.token_bytes(16)   # IV de 128 bits

def cifrar_archivo(nombre_archivo):
    """Cifra el contenido del archivo con AES-CBC"""
    if not os.path.exists(nombre_archivo):
        raise FileNotFoundError(f"El archivo {nombre_archivo} no existe.")

    with open(nombre_archivo, "rb") as archivo:
        datos = archivo.read()

    # Relleno (PKCS7) para que el tamaño sea múltiplo de 16
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    datos_padded = padder.update(datos) + padder.finalize()

    # Cifrado AES-CBC
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV))
    encryptor = cipher.encryptor()
    datos_cifrados = encryptor.update(datos_padded) + encryptor.finalize()

    return datos_cifrados

def enviar_archivo(nombre_archivo):
    """Cifra el archivo y lo envía al servidor"""
    try:
        datos_cifrados = cifrar_archivo(nombre_archivo)
    except FileNotFoundError as e:
        print(e)
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((SERVER_IP, SERVER_PORT))

        # Enviar clave e IV al servidor primero
        cliente.send(KEY + IV)

        # Enviar el nombre del archivo
        nombre_bytes = nombre_archivo.encode()
        cliente.send(struct.pack("I", len(nombre_bytes)) + nombre_bytes)

        # Enviar tamaño del archivo
        cliente.send(struct.pack("Q", len(datos_cifrados)))

        # Enviar datos cifrados
        cliente.sendall(datos_cifrados)

        print("Archivo enviado con éxito.")

if __name__ == "__main__":
    archivo = "archivo.txt"  # Nombre del archivo a enviar
    enviar_archivo(archivo)
