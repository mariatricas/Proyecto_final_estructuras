import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS bienestar_db;")
cursor.execute("USE bienestar_db;")

# Tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    usuario VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    password VARCHAR(255)
);
""")

# Tabla entradas diarias
cursor.execute("""
CREATE TABLE IF NOT EXISTS entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    fecha DATE,
    estado_animo INT,
    estres INT,
    horas_sueno FLOAT,
    ejercicio VARCHAR(100),
    FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
);
""")

conexion.commit()
conexion.close()

print("¡Base de datos y tablas creadas correctamente!")