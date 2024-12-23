import socket

def servidor_udp_broadcast():
    # Configurar el socket UDP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Enlace al puerto específico en todas las interfaces disponibles
    puerto = 5000
    servidor.bind(("", puerto))
    print(f"[SERVIDOR] Escuchando en el puerto {puerto}...")

    while True:
        # Recibir datos
        mensaje, addr = servidor.recvfrom(1024)
        print(f"[SERVIDOR] Mensaje recibido de {addr}: {mensaje.decode()}")

        # Responder al cliente con un mensaje directo
        respuesta = "Mensaje recibido"
        servidor.sendto(respuesta.encode(), addr)  # Responde directamente al cliente
        print(f"[SERVIDOR] Respuesta enviada a {addr}: {respuesta}")

# Ejecutar el servidor
servidor_udp_broadcast()
