import socket
import time

def cliente_udp_broadcast():
    # Configurar el socket UDP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Configurar tiempo de espera para recibir respuestas
    cliente.settimeout(3)

    # Dirección de broadcast y puerto
    broadcast_direccion = ("<broadcast>", 5000)
    mensaje = "Hola desde el cliente!"

    try:
        # Enviar mensaje de broadcast
        print(f"[CLIENTE] Enviando mensaje: {mensaje}")
        cliente.sendto(mensaje.encode(), broadcast_direccion)

        # Esperar respuestas de los servidores
        print("[CLIENTE] Esperando respuestas...")
        while True:
            try:
                respuesta, addr = cliente.recvfrom(1024)
                print(f"[CLIENTE] Respuesta recibida de {addr}: {respuesta.decode()}")
            except socket.timeout:
                print("[CLIENTE] Tiempo de espera agotado, no se recibieron más respuestas.")
                break
    finally:
        cliente.close()
        print("[CLIENTE] Conexión cerrada.")

# Ejecutar el cliente
cliente_udp_broadcast()
