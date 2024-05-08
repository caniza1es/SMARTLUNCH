"""
SmartLunch: gestión de usuarios.
"""

from flask import Flask, request, redirect, url_for
from vista_usuario import inicio_sesion, registro, panel_usuario
from controlador_usuario import *

app = Flask(__name__)

@app.route('/')
def inicio_sesion_route():
    """
    Ruta para la página de inicio de sesión.

    :return: Página de inicio de sesión.
    """
    return inicio_sesion()

@app.route('/registro', methods=['GET', 'POST'])
def registro_route():
    """
    Ruta para el registro de usuarios.

    Permite registrar nuevos usuarios a través de un formulario POST.

    :return: Redirige a la página de inicio de sesión después del registro.
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        email = request.form['email']
        
        registrar_usuario(nombre, usuario, contraseña, email)
        
        return redirect(url_for('inicio_sesion_route'))

    return registro()

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion_route():
    """
    Ruta para iniciar sesión.

    Permite a los usuarios iniciar sesión a través de un formulario POST.

    :return: Redirige al panel de usuario si la autenticación es exitosa, de lo contrario, muestra la página de inicio de sesión.
    """
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        user = autenticar_usuario(usuario, contraseña)
        if user:
            return redirect(url_for('panel_usuario_route', usuario=usuario))

    return inicio_sesion()

@app.route('/panel_usuario/<usuario>', methods=['GET', 'POST'])
def panel_usuario_route(usuario):
    """
    Ruta para el panel de usuario.

    Permite a los usuarios ver y actualizar su información.

    :param usuario: Nombre de usuario.
    :type usuario: str
    :return: Panel de usuario con la información del usuario especificado.
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        email = request.form['email']
        
        actualizar_usuario(usuario, nombre, contraseña, email)
        
        return redirect(url_for('panel_usuario_route', usuario=usuario))

    return panel_usuario(obtener_usuario_por_usuario(usuario))

if __name__ == "__main__":
    app.run(debug=True)
