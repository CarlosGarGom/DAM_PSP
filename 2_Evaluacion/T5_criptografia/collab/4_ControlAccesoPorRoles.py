import hashlib

# Simulación de usuarios y roles con contraseñas hasheadas
usuarios = {
    "admin": {"password": hashlib.sha256("admin123".encode()).hexdigest(), "rol": "administrador"},
    "carlos": {"password": hashlib.sha256("carlos123".encode()).hexdigest(), "rol": "usuario"}
}

def autenticar(usuario, password):
    """Verifica si el usuario y la contraseña son correctos."""
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if usuario in usuarios and usuarios[usuario]["password"] == password_hash:
        return True
    return False

def autorizar(usuario, recurso):
    """Verifica si el usuario tiene acceso al recurso solicitado."""
    rol = usuarios[usuario]["rol"]
    # Solo el administrador puede acceder a "config"
    if recurso == "config" and rol == "administrador":
        return True
    elif recurso == "lectura":
        return True
    return False

# Ejemplo de acceso
user = input("Usuario: ")
pwd = input("Contraseña: ")

if autenticar(user, pwd):
    recurso = "config"
    if autorizar(user, recurso):
        print(f"Acceso concedido a {recurso}")
    else:
        print("No tienes permisos para acceder a este recurso.")
else:
    print("Autenticación fallida.")
