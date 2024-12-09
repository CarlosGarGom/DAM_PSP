import os
import sys

fd_padre_a_hijo=os.pipe()
fd_hijo_a_padre=os.pipe()
fd_hijo_a_nieto=os.pipe()
numero_padre= "10"
pid=os.fork()

if pid<0:
    sys.exit(1)
elif pid ==0:
    #proceso hijo
    os.close(fd_padre_a_hijo[1])
    os.close(fd_hijo_a_padre[0])
    buffer= os.read(fd_padre_a_hijo[0],80).decode("utf-8")
    mensaje_modificado=int(buffer) + 5
    mensaje_modificado= str(mensaje_modificado)
    os.write(fd_hijo_a_padre[1],mensaje_modificado.encode("utf-8"))
    print(f"{mensaje_modificado}")
    os.close(fd_padre_a_hijo[0])
    os.close(fd_hijo_a_padre[1])
#    nietoPID=os.fork()

#    if(nietoPID==0):
#        os.close(fd_hijo_a_nieto[1])
#        buffer= os.read(fd_hijo_a_nieto[0],80).decode("utf-8")
#        duplicado=int(buffer) * 2
#        duplicado = str(duplicado)
#        os.write(fd_hijo_a_nieto[1], duplicado.encode("utf-8"))
#        print(f"{duplicado}")


else:
    #proceso padre
    os.close(fd_padre_a_hijo[0])
    os.close(fd_hijo_a_padre[1])
    os.write(fd_padre_a_hijo[1], numero_padre.encode("utf-8"))
    mensaje_recibido=os.read(fd_hijo_a_padre[0],80).decode("utf-8")
    #print(f"{mensaje_recibido}")
    os.close(fd_padre_a_hijo[1])
    os.close(fd_hijo_a_padre[0])
    os.wait()