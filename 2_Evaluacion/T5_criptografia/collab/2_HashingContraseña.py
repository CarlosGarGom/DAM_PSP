#Usa la librería hashlib para crear una función que guarde una contraseña de forma segura (hash).
import hashlib

def cifrar_password(password):
    """Genera un hash seguro para la contraseña utilizando SHA-256."""
    hash_mensaje = hashlib.sha256(password.encode()).hexdigest()
    return hash_mensaje



password = input("Introduce tu contraseña: ")
hash_guardado = cifrar_password(password)
print("Contraseña cifrada: ",hash_guardado)
