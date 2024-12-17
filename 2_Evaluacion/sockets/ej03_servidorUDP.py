import socket

def servidor_udp():
    # Crear socket UDP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("10.196.55.95", 5000))  # Enlazar a localhost:5000
    print("[SERVIDOR] Esperando mensajes en el puerto 5000...")

    while True:
        # Recibir datos del cliente
        datos, addr = s.recvfrom(1024)  # Buffer de 1024 bytes
        print(f"[SERVIDOR] Mensaje recibido de {addr}: {datos.decode()}")

        # Enviar respuesta al cliente
        respuesta = f"Hola, cliente desde {addr}. Mensaje recibido."
        s.sendto(respuesta.encode(), addr)
        print(f"[SERVIDOR] Respuesta enviada a {addr}")

# Ejecuta esta celda para iniciar el servidor.
servidor_udp()