#Implementa un programa que cifre un mfrom cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# **1. Generar par de claves**
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# **2. Guardar claves en archivos**
with open("clave_privada.pem", "wb") as priv_file:
    priv_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("clave_publica.pem", "wb") as pub_file:
    pub_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Claves guardadas en archivos.")

# **3. Cifrar mensaje con clave pública**
mensaje = b"Este es un mensaje secreto"
mensaje_cifrado = public_key.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Mensaje cifrado:", mensaje_cifrado.hex())

# **4. Descifrar con clave privada**
mensaje_descifrado = private_key.decrypt(
    mensaje_cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Mensaje descifrado:", mensaje_descifrado.decode())
