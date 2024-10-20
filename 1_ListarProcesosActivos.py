
import psutil


try:
    notas = False
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        print(processName, ' ::: ', processID)
        if processName=="Notepad.exe":
            notas= True
            notasPID=proc.pid




    if notas == True:
        print("El Bloc de notas esta en ejecución ",notasPID)



except:
    print("error")