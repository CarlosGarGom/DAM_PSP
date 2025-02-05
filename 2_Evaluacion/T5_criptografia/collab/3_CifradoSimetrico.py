from cryptography.fernet import Fernet
import os

# 1. Generar y guardar la clave
def generar_clave():
    if not os.path.exists("clave.key"):  # Comprueba si el archivo ya existe
        clave = Fernet.generate_key()  # Genera una clave nueva
        with open("clave.key", "wb") as clave_file:
            clave_file.write(clave)  # Guarda la clave en un archivo
        print("[INFO] Clave generada y guardada en 'clave.key'")
    else:
        print("[INFO] La clave ya existe. No se ha generado una nueva.")

# 2. Cargar la clave desde el archivo
def cargar_clave():
    with open("clave.key", "rb") as clave_file:
        return clave_file.read()  # Lee la clave almacenada

# 3. Cifrar un mensaje y guardarlo en un archivo
def cifrar_mensaje(mensaje):
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_cifrado = fernet.encrypt(mensaje.encode())  # Cifra el mensaje
    with open("mensaje_cifrado.txt", "wb") as file:
        file.write(mensaje_cifrado)  # Guarda el mensaje cifrado

# 4. Leer y descifrar el mensaje
def descifrar_mensaje():
    clave = cargar_clave()
    fernet = Fernet(clave)
    with open("mensaje_cifrado.txt", "rb") as file:
        mensaje_cifrado = file.read()  # Lee el mensaje cifrado
    mensaje_descifrado = fernet.decrypt(mensaje_cifrado).decode()  # Descifra
    return mensaje_descifrado


generar_clave()

mensaje_original = input("Introduce el mensaje a cifrar: ")
cifrar_mensaje(mensaje_original)
print("\nMensaje cifrado guardado en 'mensaje_cifrado.txt'")

mensaje_descifrado = descifrar_mensaje()
print("\n✅ Mensaje descifrado:", mensaje_descifrado)
