from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import controlador_usuario as ctrl

app = Flask(__name__)

@app.route('/')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        email = request.form['email']

        print(f"Datos recibidos: {nombre}, {usuario}, {contrasena}, {email}")

        try:
            ctrl.agregar_usuario(nombre, usuario, contrasena, email)
            print("Usuario agregado correctamente")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")

        return redirect(url_for('inicio_sesion'))

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        print(f"Intento de inicio de sesión: {usuario}, {contrasena}")

        user_data = ctrl.consultar_usuario(usuario)
        if user_data and user_data[3] == contrasena:  # Asegúrate de que el índice sea correcto para la contraseña
            print(f"Usuario {usuario} autenticado correctamente")
        else:
            print(f"Fallo en la autenticación para el usuario {usuario}")

        return redirect(url_for('inicio_sesion'))

    return render_template('inicio_sesion.html')

@app.route('/actualizar', methods=['POST'])
def actualizar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        nuevo_usuario = request.form['nuevo_usuario']
        nueva_contrasena = request.form['nueva_contrasena']
        nuevo_email = request.form['nuevo_email']

        print(f"Datos recibidos para actualizar: {usuario}, {nombre}, {nuevo_usuario}, {nueva_contrasena}, {nuevo_email}")

        try:
            ctrl.actualizar_usuario(usuario, nombre, nuevo_usuario, nueva_contrasena, nuevo_email)
            print("Usuario actualizado correctamente")
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")

        return redirect(url_for('inicio_sesion'))

if __name__ == "__main__":
    app.run(debug=True)
