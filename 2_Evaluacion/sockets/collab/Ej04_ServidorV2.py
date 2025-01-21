import socket


def servidor_tcp():
    # Crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Intentar bindear el socket a la dirección y puerto
        s.bind(("127.0.0.1", 5000))
        s.listen(1)  # Aceptar una conexión
        print("[SERVIDOR] Esperando conexiones...")

        # Aceptar una conexión
        conn, addr = s.accept()
        print("[SERVIDOR] Conexión establecida con", addr)

        try:
            # Recibir datos del cliente
            datos = conn.recv(1024)

            if not datos:
                print("[SERVIDOR] No se recibieron datos del cliente.")
                return  # Terminar si no se reciben datos

            print("[SERVIDOR] Datos recibidos:", datos.decode())
            datoModificado = datos.decode().upper()
            print("[SERVIDOR] Modificamos datos:", datoModificado)

            # Enviar el mensaje modificado al cliente
            conn.send(datoModificado.encode())

        except Exception as e:
            print(f"[SERVIDOR] Error al recibir o enviar datos: {e}")

        finally:
            # Asegurarse de cerrar la conexión
            conn.close()
            print("[SERVIDOR] Conexión cerrada con el cliente.")

    except Exception as e:
        print(f"[SERVIDOR] Error al configurar el servidor: {e}")

    finally:
        # Asegurarse de cerrar el socket del servidor
        s.close()
        print("[SERVIDOR] Socket del servidor cerrado.")


if __name__ == "__main__":
    # Ejecutar el servidor

    servidor_tcp()
