import socket

def cliente_udp():
    # Crear socket UDP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dirección del servidor
    servidor = ("10.196.55.97", 5097)

    # Enviar un mensaje al servidor
    mensaje = "¡Hola, servidor Soy Carlos!"
    print(f"[CLIENTE] Enviando mensaje al servidor: {mensaje}")
    s.sendto(mensaje.encode(), servidor)

    # Recibir respuesta del servidor
    datos, addr = s.recvfrom(1024)  # Buffer de 1024 bytes
    print(f"[CLIENTE] Respuesta del servidor: {datos.decode()}")

    # Cerrar el socket
    s.close()

# Ejecuta esta celda para iniciar el cliente.
cliente_udp()