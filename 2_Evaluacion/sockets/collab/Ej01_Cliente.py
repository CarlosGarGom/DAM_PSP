import socket

def cliente_tcp():
    # Crear socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 5000))
    print("[CLIENTE] Conectado al servidor.")



    # Enviar un mensaje al servidor
    msg = "mensaje desde el cliente"
    c.send(msg.encode())

    # Recibir mensaje del servidor
    msg = c.recv(1024)
    print("[CLIENTE] Mensaje del servidor:", msg.decode())

    c.close()
    print("[CLIENTE] Conexión cerrada.")

# Ejecutar el cliente
cliente_tcp()