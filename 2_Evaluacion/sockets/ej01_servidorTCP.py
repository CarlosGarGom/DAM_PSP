import socket

def servidor_tcp():
    # Crear socket TCP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.196.55.95", 5095))
    s.listen(1)  # Aceptar una conexión
    print("[SERVIDOR] Esperando conexiones...")
    conn, addr = s.accept()
    print("[SERVIDOR] Conexión establecida con", addr)

    # Enviar un mensaje al cliente
    mensaje = "Soy el servidor de Carlos!"
    conn.send(mensaje.encode())

    # Recibir respuesta del cliente
    datos = conn.recv(1024)
    print("[SERVIDOR] Datos recibidos:", datos.decode())

    conn.close()
    s.close()
    print("[SERVIDOR] Conexión cerrada.")

# Ejecuta esta celda para iniciar el servidor.
# Luego, en otra terminal o en otro notebook, puedes conectar con un cliente.
servidor_tcp()