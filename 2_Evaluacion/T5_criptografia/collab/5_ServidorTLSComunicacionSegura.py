# Implementa un cliente y servidor con sockets TLS. Genera certificados autofirmados para pruebas locales.

import socket
import ssl

# Crear un contexto SSL/TLS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Cargar el certificado y la clave privada
try:
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
except FileNotFoundError:
    print("Error: Certificado o clave no encontrados. Genera los archivos cert.pem y key.pem.")
    exit()

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8443))  # Puerto seguro
server_socket.listen(5)

# Envolver el socket con TLS
with context.wrap_socket(server_socket, server_side=True) as tls_socket:
    print("Servidor TLS escuchando en localhost:8443...")
    while True:
        try:
            conn, addr = tls_socket.accept()
            print("Conexión segura establecida con:", addr)

            data = conn.recv(1024)
            if data:
                print("Mensaje recibido:", data.decode())
                conn.sendall(b"Hola, esta es una conexion segura.\n")

            conn.close()
        except Exception as e:
            print("Error durante la conexión:", e)
