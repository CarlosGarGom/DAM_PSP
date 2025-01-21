# **Instalación de Flask
# !pip install flask

# **Importación de librerías**
# Flask: Framework para crear aplicaciones web.
# jsonify: Permite convertir datos en formato JSON.
# request: Permite acceder a los datos enviados en las solicitudes HTTP (como POST o PUT).
from flask import Flask, jsonify, request
from flask_cors import CORS

# **Inicialización de la aplicación Flask**
# Creamos una instancia de Flask que será nuestra aplicación web.
app = Flask(__name__)
CORS(app)
# **Base de datos simulada**
# Usamos una lista como una "base de datos" en memoria para almacenar información de usuarios.
# Cada usuario es representado como un diccionario con las claves 'id', 'nombre' y 'edad'.
usuarios = [
    {"id": 1, "nombre": "Pepe", "edad": 25},
    {"id": 2, "nombre": "Ana", "edad": 30}
]

# **Ruta principal (GET)**
@app.route('/')
def home():
    """
    Ruta principal de la API.
    Cuando un usuario accede a esta ruta ('/'), se devuelve un mensaje de bienvenida.
    """
    return "¡Bienvenido a la API de usuarios en local!"

# **Endpoint para obtener todos los usuarios (GET)**
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    """
    Este endpoint devuelve la lista completa de usuarios almacenados en la base de datos simulada.
    """
    return jsonify(usuarios)

# **Endpoint para obtener un usuario por ID (GET)**
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    """
    Este endpoint busca un usuario específico por su ID.
    - Si encuentra el usuario, devuelve su información en formato JSON.
    - Si no lo encuentra, devuelve un error 404 con un mensaje apropiado.
    """
    # Buscamos el usuario en la lista por su ID.
    # Utilizamos next() para obtener el primer elemento que cumple la condición.
    # Si no se encuentra ningún usuario con ese ID, se devuelve None.
    # Es un generador, NO una lista.
    # for u in usuarios recorre la lista de usuarios.
    # u es el usuario actual en cada iteración generada por el for.
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if usuario:
        return jsonify(usuario)  # Devolvemos el usuario encontrado.
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404  # Usuario no encontrado.

# **Endpoint para crear un nuevo usuario (POST)**
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    # TODO Actualizar como se generan los ids, que recoja el id mas alto y le sume 1
    """
    Este endpoint permite agregar un nuevo usuario a la base de datos simulada.
    El cliente debe enviar un JSON con los datos del nuevo usuario ('nombre' y 'edad').
    """
    if usuarios:
        nuevo_id = max(usuario["id"] for usuario in usuarios) + 1
    else:
        nuevo_id = 1  # Si la lista está vacía, asignamos el ID 1.
    # Obtenemos los datos enviados en la solicitud.
    datos = request.get_json()
    nuevo_usuario = {
        "id": nuevo_id,  # Generamos un nuevo ID basado en el tamaño de la lista.
        "nombre": datos["nombre"],  # Nombre del usuario.
        "edad": datos["edad"]  # Edad del usuario.
    }
    usuarios.append(nuevo_usuario)  # Añadimos el nuevo usuario a la lista.
    return jsonify(nuevo_usuario), 201  # Devolvemos el usuario creado con el código 201 (Created).

# **Endpoint para actualizar un usuario existente (PUT)**
@app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    """
    Este endpoint permite actualizar los datos de un usuario existente.
    El cliente debe enviar un JSON con los campos que desea modificar.
    """
    # Buscamos el usuario por su ID.
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if usuario:
        # Obtenemos los datos enviados en la solicitud.
        datos = request.get_json()
        # Actualizamos solo los campos proporcionados en el JSON.
        usuario["nombre"] = datos.get("nombre", usuario["nombre"])
        usuario["edad"] = datos.get("edad", usuario["edad"])
        return jsonify(usuario)  # Devolvemos el usuario actualizado.
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404  # Usuario no encontrado.

# **Endpoint para eliminar un usuario (DELETE)**
@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    # TODO Si no se encuentra el ID COMUNICARLO
    """
    Este endpoint permite eliminar un usuario específico por su ID.
    """
    global usuarios  # Indicamos que vamos a modificar la lista global.
    # Filtramos la lista de usuarios para eliminar el que coincide con el ID.
    usuarios = [u for u in usuarios if u["id"] != usuario_id]
    return jsonify({"mensaje": "Usuario eliminado"}), 200  # Confirmamos la eliminación.

# **Endpoint para eliminar usuarios (DELETE)**
@app.route('/api/usuarios', methods=['DELETE'])
def eliminar_usuarios():

    """
    Este endpoint permite eliminar todos los usuarios
    """
    global usuarios  # Indicamos que vamos a modificar la lista global.

    usuarios.clear()
    return jsonify({"mensaje": "Usuarios eliminados"}), 200  # Confirmamos la eliminación.

# **Ejecución de la aplicación**
if __name__ == '__main__':
    """
    Arranca el servidor Flask en el puerto 5000 con modo debug activado.
    Esto permite ver los errores y recargar automáticamente los cambios en el código.
    """
    app.run(debug=True, port=5000)  # Ejecuta el servidor en http://127.0.0.1:5000