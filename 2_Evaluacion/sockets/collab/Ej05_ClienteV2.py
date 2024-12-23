import socket


def cliente_tcp():
    # Solicitar al usuario la dirección IP y el puerto
    ip_servidor = input("Introduce la dirección IP del servidor: ")
    puerto_servidor = int(input("Introduce el puerto del servidor: "))

    # Crear socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor usando la dirección y el puerto proporcionados
        c.connect((ip_servidor, puerto_servidor))
        print("[CLIENTE] Conectado al servidor.")

        # Enviar un mensaje al servidor
        msg = "mensaje desde el cliente"
        c.send(msg.encode())

        # Recibir mensaje del servidor
        msg = c.recv(1024)
        print("[CLIENTE] Mensaje del servidor:", msg.decode())

    except Exception as e:
        print(f"[CLIENTE] Error al conectar con el servidor: {e}")

    finally:
        # Cerrar la conexión
        c.close()
        print("[CLIENTE] Conexión cerrada.")


# Ejecutar el cliente
cliente_tcp()
