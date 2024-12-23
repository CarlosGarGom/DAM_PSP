import socket


def cliente_tcp():
    """Cliente TCP para interactuar con el servidor de eco."""
    servidor_host = "127.0.0.1"  # Dirección del servidor
    servidor_puerto = 5000  # Puerto del servidor

    try:
        # Crear socket TCP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((servidor_host, servidor_puerto))
        print(f"[CLIENTE] Conectado al servidor en {servidor_host}:{servidor_puerto}")

        # Recibir mensaje inicial del servidor
        bienvenida = cliente.recv(1024).decode()
        print(f"[SERVIDOR] {bienvenida}")

        while True:
            # Pedir al usuario un mensaje para enviar
            mensaje = input("[CLIENTE] Escribe un mensaje ('QUIT' para salir): ").strip()

            # Enviar mensaje al servidor
            cliente.send(mensaje.encode())

            if mensaje.upper() == "QUIT":
                print("[CLIENTE] Cerrando conexión con el servidor.")
                break

            # Recibir respuesta del servidor
            respuesta = cliente.recv(1024).decode()
            print(f"[SERVIDOR] {respuesta.strip()}")

    except Exception as e:
        print(f"[CLIENTE] Error: {e}")
    finally:
        cliente.close()
        print("[CLIENTE] Conexión cerrada.")


# Ejecutar el cliente
cliente_tcp()
