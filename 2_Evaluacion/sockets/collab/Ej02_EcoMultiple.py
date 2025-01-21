import socket
import threading

def manejar_cliente(conn, addr):
    """Función para manejar la comunicación con un cliente."""
    print(f"[HILO] Conexión aceptada desde {addr}")
    try:
        # Enviar mensaje de bienvenida al cliente
        conn.send("Bienvenido al servidor eco Escribe algo (escribe QUIT para salir).\n")

        while True:
            # Recibir datos del cliente
            datos = conn.recv(1024)
            if not datos:
                print(f"[HILO] Cliente {addr} desconectado.")
                break

            mensaje = datos.decode("utf-8").strip()
            print(f"[HILO] Mensaje recibido de {addr}: {mensaje}")

            # Responder con el texto en mayúsculas
            if mensaje.upper() == "QUIT":
                conn.send("Conexión cerrada\n")
                print(f"[HILO] Cliente {addr} solicitó cerrar la conexión")
                break
            else:
                respuesta = mensaje.upper()
                conn.send(f"{respuesta}\n")
    except Exception as e:
        print(f"[HILO] Error con el cliente {addr}: {e}")
    finally:
        # Cerrar la conexión
        print(f"[HILO] Cerrando conexión con {addr}")
        conn.close()

def servidor_tcp_hilos():
    """Servidor TCP que maneja múltiples clientes con hilos."""
    # Crear socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 5000))  # IP / PUERTO
    servidor.listen(5)  # Escuchar hasta 5 conexiones en cola
    print("[SERVIDOR] Escuchando en 127.0.0.1:5000")

    while True:
        # Aceptar una conexión
        conn, addr = servidor.accept()
        print(f"[SERVIDOR] Conexión recibida de {addr}")

        # Crear un hilo para manejar al cliente
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()  # Iniciar el hilo
        print(f"[SERVIDOR] Hilo iniciado para {addr}")

# Ejecutar el servidor
servidor_tcp_hilos()
