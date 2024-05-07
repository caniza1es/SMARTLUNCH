from flask import Flask, render_template, request, redirect, url_for,send_from_directory
import os
import sys

app = Flask(__name__)


@app.route('/')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        email = request.form['email']
        
        # Simulación de inserción en la base de datos
        print("Insertar usuario:", nombre, usuario, contraseña, email,file=sys.stdout)
        
        return redirect(url_for('inicio_sesion'))  # Redirect to the login page

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        # Simulación de autenticación en la base de datos
        print("Usuario inició sesión:", usuario, contraseña,file=sys.stdout)
        
        return redirect(url_for('inicio_sesion'))  # Redirect to the login page

    return render_template('inicio_sesion.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
