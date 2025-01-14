# Importamos las librerías necesarias de Flask:
# - Flask: para crear la aplicación web.
# - jsonify: para devolver respuestas en formato JSON.
# - request: para manejar las solicitudes HTTP y obtener parámetros enviados por el cliente.
from flask import Flask, jsonify, request

# Inicializamos la aplicación Flask.
# `__name__` indica el nombre del módulo actual, lo que ayuda a Flask a localizar recursos y rutas.
app = Flask(__name__)

# Definimos la ruta principal ('/') del servidor.
# Cuando un cliente acceda a esta ruta con un método GET, se ejecutará la función `home`.
@app.route('/')
def home():
    # Retornamos un mensaje de bienvenida como respuesta de la ruta principal.
    return "¡Bienvenido a mi servidor Flask!"

# Definimos otra ruta ('/api/saludo') que responde a solicitudes GET.
# Este endpoint espera recibir un parámetro opcional llamado 'nombre'.
@app.route('/api/saludo', methods=['GET'])
def saludo():
    # Obtenemos el parámetro 'nombre' de la solicitud (GET).
    # Si no se envía el parámetro, se usará 'Invitado' como valor por defecto.
    nombre = request.args.get('nombre', 'Invitado')

    # Construimos una respuesta en formato JSON con el mensaje de saludo y un estado de éxito.
    return jsonify({
        "mensaje": f"Hola, {nombre}!",
        "status": "éxito"
    })

# Nuevo endpoint para manejar peticiones POST en /api/data
@app.route('/api/data', methods=['POST'])
def recibir_datos():
    # Obtenemos el JSON enviado en la solicitud
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    # Procesamos los datos recibidos
    key = data.get("key", "Valor no proporcionado")

    return jsonify({
        "mensaje": f"Se recibió la clave con el valor: {key}",
        "status": "éxito"
    })

# Punto de entrada del programa.
# La condición `if __name__ == "__main__"` asegura que este bloque de código
# solo se ejecuta si este archivo se ejecuta directamente (no si es importado como módulo).
if __name__ == "__main__":
    # Iniciamos el servidor Flask:
    # - debug=True: activa el modo depuración, útil para desarrollo (recarga automática).
    # - host='127.0.0.1': el servidor escuchará solo en localhost.
    # - port=5000: especifica el puerto en el que el servidor estará disponible.
    app.run(debug=True, host='127.0.0.1', port=5000)
