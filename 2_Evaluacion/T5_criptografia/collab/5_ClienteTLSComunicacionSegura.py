import socket
import ssl

# Crear un contexto SSL/TLS para el cliente
context = ssl.create_default_context()

# Conectar al servidor
with socket.create_connection(("localhost", 8443)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as tls_sock:
        print("Conectado al servidor TLS.")

        # Enviar datos al servidor
        mensaje = "Hola servidor, soy un cliente seguro."
        tls_sock.sendall(mensaje.encode())

        # Recibir respuesta del servidor
        respuesta = tls_sock.recv(1024)
        print("Respuesta del servidor:", respuesta.decode())
