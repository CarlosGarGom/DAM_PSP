# Escribe un programa que solicite al usuario un nombre de usuario y contraseña.
# Valida que el nombre no contenga caracteres peligrosos (por ejemplo, ;, --, <, >).
import re


def nombre_valido(nombre):
    """ Valida que el nombre de usuario no contenga caracteres peligrosos. """
    caracteres_peligrosos = r"[;<>-]" # Expresion regular que contiene los caracteres peligrosos
    if re.search(caracteres_peligrosos,nombre): # busca en el nombre si tiene contenido de la RE
        return False
    return True

def pedir_datos():
    """ Solicita al usuario un nombre de usuario y contraseña con validación. """
    while True:
        usuario=input("Introduzca el nombre de usuario: ")
        if nombre_valido(usuario):
            break;
        else:
            print("Error: el nombre de usuario contioene caracteres no permitidos. Intentelo de nuevo")
    password = input("Introduzca su contraseña: ")

    print("\nRegistro exitoso.")
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {'*' * len(password)}")

pedir_datos()