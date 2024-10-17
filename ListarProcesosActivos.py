
import psutil


try:
    notas = False
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        print(processName, ' ::: ', processID)
        if processName=="notepad.exe":
            notas= True




    if notas == True:
        print("El Bloc de notas esta en ejecución")



except:
    print("error")