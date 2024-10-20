import os
import psutil


try:
    print("Dime el pid de un proceso")
    pid_ingresado = input()
    pid=int(pid_ingresado)
    p = psutil.Process(pid)
    p.terminate()



except:
    print("error")