import psutil
import time


def mostrar_procesos():
    # Encabezado de la tabla
    print(f"{'PID':<10} {'Nombre':<25} {'CPU (%)':<10} {'Memoria (MB)':<15}")
    print("-" * 60)

    # Iterar sobre todos los procesos activos
    for proceso in psutil.process_iter():
        try:
            # Obtenemos los datos del proceso
            pid = proceso.pid
            nombre = proceso.name
            cpu_uso = proceso.cpu_percent(interval=0.5) # intervalo para que la cpu mida el consumo
            memoria_uso = proceso.memory_info().rss / (1024 * 1024)  # Convertir a MB

            # Imprimir la información del proceso, ajustando % y MB
            print(f"{pid:<10} {nombre:<25} {cpu_uso:>7.2f} % {memoria_uso:>10.2f} MB")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Evitar errores
            pass


def main():
    while True:
        # Mostrar la lista de procesos
        mostrar_procesos()

        # Pausa de 2 segundos
        time.sleep(2)

        # Preguntar al usuario si quiere continuar o salir
        continuar = input("\nPresiona Enter para actualizar o 'q' para salir: ").strip().lower()
        if continuar == 'q':
            break


if __name__ == "__main__":
    main()
