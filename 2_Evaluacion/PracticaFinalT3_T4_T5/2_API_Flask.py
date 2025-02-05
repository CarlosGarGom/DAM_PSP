from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3
import bcrypt
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

def init_db():
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            mensaje TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


def encrypt_message(key, plaintext):
    iv = os.urandom(16)  # Vector de inicialización aleatorio
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Aplicar PKCS7 Padding para que el mensaje tenga un tamaño múltiplo de 16
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(plaintext.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_text) + encryptor.finalize()

    # Convertir IV + ciphertext a base64 para evitar problemas de almacenamiento
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_message(key, encrypted):
    try:
        # Decodificar de base64 antes de separar IV y ciphertext
        raw_data = base64.b64decode(encrypted)

        iv, ciphertext = raw_data[:16], raw_data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

        # Eliminar el padding PKCS7
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted.decode()
    except Exception as e:
        print(f"Error al descifrar: {e}")
        return None
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"].encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")
    try:
        conn = sqlite3.connect("mensajes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except:
        return jsonify({"message": "Error: Usuario ya existe"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"].encode("utf-8")
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password, user[0].encode("utf-8")):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Credenciales incorrectas"}), 401

@app.route("/send", methods=["POST"])
@jwt_required()
def send_message():
    data = request.get_json()
    sender = get_jwt_identity()
    receiver = data["receiver"]
    message = data["message"]
    key = b"abcdefghijklmnop"  # Clave AES de 16 bytes
    encrypted_message = encrypt_message(key, message)
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensajes (sender, receiver, mensaje) VALUES (?, ?, ?)", (sender, receiver, encrypted_message))
    conn.commit()
    conn.close()
    return jsonify({"message": "Mensaje enviado"})

@app.route("/messages", methods=["GET"])
@jwt_required()
def get_messages():
    username = get_jwt_identity()
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT sender, mensaje FROM mensajes WHERE receiver = ?", (username,))
    messages = cursor.fetchall()
    conn.close()
    key = b"abcdefghijklmnop"  # Clave AES de 16 bytes
    decrypted_messages = [{"sender": sender, "message": decrypt_message(key, msg)} for sender, msg in messages]
    return jsonify(decrypted_messages)

if __name__ == "__main__":
    app.run(debug=True)
