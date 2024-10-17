import os
import psutil


try:
    print("Dime el pid de un proceso")
    pid = input()
    p = psutil.Process(pid)
    p.terminate()



except:
    print("error")