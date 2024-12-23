import socket


def servidor_tcp():
    # Crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 5000))
    s.listen(1)  # Aceptar una conexión
    print("[SERVIDOR] Esperando conexiones...")
    conn, addr = s.accept()
    print("[SERVIDOR] Conexión establecida con", addr)


    # Recibir respuesta del cliente
    datos = conn.recv(1024)

    print("[SERVIDOR] Datos recibidos:", datos.decode())
    datoModificado=datos.decode().upper()
    print("[SERVIDOR] Modificamos datos:", datoModificado)
    # Enviar un mensaje al cliente
    conn.send(datoModificado.encode())

    # cerrar conexion y socket
    conn.close()
    s.close()
    print("[SERVIDOR] Conexión cerrada.")

# Ejecutar el servidor
servidor_tcp()



