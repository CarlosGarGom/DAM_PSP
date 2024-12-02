import os
import sys

fd_padre_a_hijo = os.pipe()
fd_hijo_a_padre = os.pipe()

saludo_padre = 10
pid = os.fork()

if pid < 0:
    sys.exit(1)
elif pid == 0:
    os.close(fd_padre_a_hijo[1])
    os.close(fd_hijo_a_padre[0])
    Int = os.read(fd_padre_a_hijo[0])
    mensaje_modificado = Int

    os.write(fd_hijo_a_padre[1], mensaje_modificado)
    print(f"{mensaje_modificado}")
    os.close(fd_padre_a_hijo[0])
    os.close(fd_hijo_a_padre[1])
else:
    os.close(fd_padre_a_hijo[0])
    os.close(fd_hijo_a_padre[1])
    os.write(fd_padre_a_hijo[1], saludo_padre)
    mensaje_recibido = os.read(fd_hijo_a_padre[0])
    print(f"{mensaje_recibido}")
    os.close(fd_padre_a_hijo[1])
    os.close(fd_hijo_a_padre[0])
    os.wait()