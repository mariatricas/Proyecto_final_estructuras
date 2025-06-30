import mysql.connector
import bcrypt
import re
from datetime import date

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bienestar_db"
    )

def validar_password(password):
    return bool(re.search(r'[A-Z]', password) and re.search(r'\d', password))

def validar_edad(edad):
    try:
        return int(edad) >= 15
    except ValueError:
        return False

def registrar_usuario(usuario, nombre, apellido, edad, password):
    if not validar_edad(edad):
        return "edad_invalida"
    if not validar_password(password):
        return "password_invalida"

    conn = conectar()
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO usuarios (usuario, nombre, apellido, edad, password) VALUES (%s, %s, %s, %s, %s)",
                       (usuario, nombre, apellido, int(edad), hashed))
        conn.commit()
        return "ok"
    except mysql.connector.IntegrityError:
        return "usuario_existente"
    finally:
        conn.close()

def login_usuario(usuario, password):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE usuario = %s", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and bcrypt.checkpw(password.encode('utf-8'), resultado[0].encode('utf-8')):
        return True
    return False

def guardar_entrada(usuario, estado_animo, estres, horas_sueno, ejercicio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entradas (usuario, fecha, estado_animo, estres, horas_sueno, ejercicio)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (usuario, date.today(), estado_animo, estres, horas_sueno, ejercicio))
    conn.commit()
    conn.close()