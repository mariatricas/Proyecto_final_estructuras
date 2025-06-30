import tkinter as tk
from tkinter import messagebox
from backend1 import registrar_usuario, login_usuario, guardar_entrada
import re
from PIL import Image, ImageTk

# COLORES Y FUENTE
COLOR_FONDO = "#f5e9f5"  # lila claro
COLOR_BOTON1 = "#f9aff4"  # rosa
COLOR_BOTON2 = "#d4c3f9"  # fucsia
FUENTE = ("Segoe UI", 11)

ventana = tk.Tk()
ventana.title("Bienestar Mental")
ventana.geometry("1280x720")
ventana.configure(bg=COLOR_FONDO)

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def solo_letras(texto):
    return texto.isalpha()

def solo_letras_numeros(texto):
    return texto.isalnum()

# ---------- MENÚ PRINCIPAL ----------
def menu_inicio():
    limpiar_ventana()

    fondo = ImageTk.PhotoImage(Image.open("cielo1.jpg").resize((1280, 720)))
    fondo_label = tk.Label(ventana, image=fondo)
    fondo_label.image = fondo  # evitar que lo borre el garbage collector
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(ventana, bg=COLOR_FONDO)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Bienvenido/a", font=("Segoe UI", 24, "bold"), bg=COLOR_FONDO).pack(pady=70, padx=70)
    tk.Button(frame, text="Registrarse", font=FUENTE, bg=COLOR_BOTON1, command=registrarse).pack(pady=20, ipadx=20)
    tk.Button(frame, text="Iniciar sesión", font=FUENTE, bg=COLOR_BOTON2, command=iniciar_sesion).pack(pady=20, ipadx=20)

# ---------- MENÚ APP TRAS LOGIN ----------
def menu_app(usuario):
    limpiar_ventana()

    tk.Label(ventana, text=f"Hola, {usuario} 👋", font=("Segoe UI", 20, "bold"), bg=COLOR_FONDO).pack(pady=40)

    tk.Button(ventana, text="📔 Entrada diaria", font=("Segoe UI", 12), bg="#dda0dd", command=lambda: entrada_diaria(usuario)).pack(pady=10)
    tk.Button(ventana, text="📊 Estadísticas", font=("Segoe UI", 12), bg="#98fb98").pack(pady=10)
    tk.Button(ventana, text="💬 Mensajes", font=("Segoe UI", 12), bg="#ffb6c1").pack(pady=10)
    tk.Button(ventana, text="Salir", font=("Segoe UI", 10), bg="#d3d3d3", command=ventana.destroy).pack(pady=30)

# ---------- REGISTRO ----------
def registrarse():
    limpiar_ventana()

    def registrar(): 
        usuario = entry_usuario.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        edad = entry_edad.get()
        password = entry_password.get()

        if not solo_letras(nombre) or not solo_letras(apellido):
            messagebox.showerror("Error", "Nombre y apellido deben tener solo letras.")
            return
        if not solo_letras_numeros(usuario):
            messagebox.showerror("Error", "Usuario solo debe tener letras y números.")
            return

        resultado = registrar_usuario(usuario, nombre, apellido, edad, password)

        if resultado == "ok":
            messagebox.showinfo("Éxito", "¡Usuario registrado correctamente!")
            menu_inicio()
        elif resultado == "usuario_existente":
            messagebox.showerror("Error", "El usuario ya existe.")
        elif resultado == "edad_invalida":
            messagebox.showerror("Edad no válida", "Debés tener al menos 15 años.")
        elif resultado == "password_invalida":
            messagebox.showerror("Contraseña inválida", "Debe tener una mayúscula y un número.")
        else:
            messagebox.showerror("Error", "Algo salió mal.")

    tk.Label(ventana, text="Registro", font=("Segoe UI", 14, "bold"), bg=COLOR_FONDO).pack(pady=10)

    tk.Label(ventana, text="Usuario", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_usuario = tk.Entry(ventana, font=FUENTE)
    entry_usuario.pack(pady=3)

    tk.Label(ventana, text="Nombre", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_nombre = tk.Entry(ventana, font=FUENTE)
    entry_nombre.pack(pady=3)

    tk.Label(ventana, text="Apellido", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_apellido = tk.Entry(ventana, font=FUENTE)
    entry_apellido.pack(pady=3)

    tk.Label(ventana, text="Edad", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_edad = tk.Entry(ventana, font=FUENTE)
    entry_edad.pack(pady=3)

    tk.Label(ventana, text="Contraseña", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_password = tk.Entry(ventana, font=FUENTE, show="*")
    entry_password.pack(pady=3)

    tk.Button(ventana, text="Registrar", bg=COLOR_BOTON1, font=FUENTE, command=registrar).pack(pady=10, ipadx=10)
    tk.Button(ventana, text="Volver", bg=COLOR_BOTON2, font=FUENTE, command=menu_inicio).pack()

# ---------- LOGIN ----------
def iniciar_sesion():
    limpiar_ventana()

    def login():
        usuario = entry_usuario_login.get()
        password = entry_password_login.get()

        resultado = login_usuario(usuario, password)
        if resultado == "no_existe":
            if messagebox.askyesno("No registrado", "Ese usuario no existe. ¿Querés registrarte?"):
                registrarse()
            else:
                menu_inicio()
        elif resultado is True:
            messagebox.showinfo("Login exitoso", f"Bienvenido/a, {usuario}")
            menu_app(usuario)
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")

    tk.Label(ventana, text="Iniciar sesión", font=("Segoe UI", 14, "bold"), bg=COLOR_FONDO).pack(pady=10)

    tk.Label(ventana, text="Usuario", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_usuario_login = tk.Entry(ventana, font=FUENTE)
    entry_usuario_login.pack(pady=5)

    tk.Label(ventana, text="Contraseña", font=FUENTE, bg=COLOR_FONDO).pack()
    entry_password_login = tk.Entry(ventana, font=FUENTE, show="*")
    entry_password_login.pack(pady=5)

    tk.Button(ventana, text="Ingresar", bg=COLOR_BOTON2, font=FUENTE, command=login).pack(pady=10, ipadx=10)
    tk.Button(ventana, text="Volver", bg=COLOR_BOTON1, font=FUENTE, command=menu_inicio).pack()

# ---------- ENTRADA DIARIA ----------
def entrada_diaria(usuario):
    nueva = tk.Toplevel()
    nueva.title("Entrada Diaria")
    nueva.geometry("400x500")
    nueva.configure(bg="#f7f0fa")

    tk.Label(nueva, text="Registrar tu día", font=("Segoe UI", 16), bg="#f7f0fa").pack(pady=10)

    tk.Label(nueva, text="Estado de ánimo (1-10):", bg="#f7f0fa").pack()
    estado = tk.Scale(nueva, from_=1, to=10, orient=tk.HORIZONTAL)
    estado.pack()

    tk.Label(nueva, text="Nivel de estrés (1-5):", bg="#f7f0fa").pack()
    estres = tk.Scale(nueva, from_=1, to=5, orient=tk.HORIZONTAL)
    estres.pack()

    tk.Label(nueva, text="Horas de sueño:", bg="#f7f0fa").pack()
    sueno = tk.Spinbox(nueva, from_=0, to=14)
    sueno.pack()

    tk.Label(nueva, text="Ejercicio realizado:", bg="#f7f0fa").pack()
    ejercicio = tk.Entry(nueva)
    ejercicio.pack()

    def guardar():
        guardar_entrada(usuario, estado.get(), estres.get(), float(sueno.get()), ejercicio.get())
        messagebox.showinfo("Éxito", "Entrada guardada correctamente")
        nueva.destroy()

    tk.Button(nueva, text="Guardar", bg="#ce9fc9", fg="white", command=guardar).pack(pady=20)

menu_inicio()
ventana.mainloop()