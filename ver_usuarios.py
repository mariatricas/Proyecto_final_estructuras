import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bienestar_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios;")
usuarios = cursor.fetchall()

print("Usuarios registrados:")
for u in usuarios:
    print(u)

conn.close()