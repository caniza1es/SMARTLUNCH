from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash 
from controlador_usuario import *
app = Flask(__name__)

# Simulación de datos de usuario almacenados en una lista
usuarios = [
    {"nombre": "Ejemplo Usuario", "usuario": "ejemplo", "contraseña": "123456", "email": "ejemplo@example.com"}
]


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


        usuariox.agregar_usuario(nombre,usuario,contraseña,email)
        #  inserción en la base de usuarios
        
        
        return redirect(url_for('inicio_sesion'))  # Redirige a la página de inicio de sesión

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
                # Consulta el usuario en la base de datos
        user_data = usuariox.consultar_usuario(usuario)
        
        if user_data[2] == usuario and user_data[3] == contraseña:
            # Autenticación exitosa
            return redirect(url_for('panel_usuario', usuario=usuario))
        else:
            flash("Usuario o contraseña incorrectos", "error")
            return redirect(url_for('inicio_sesion'))
    



@app.route('/panel_usuario/<usuario>', methods=['GET', 'POST'])
def panel_usuario(usuario):
    user = None
    # Busca el usuario en la lista de usuarios
    for u in usuarios:
        if u["usuario"] == usuario:
            user = u
            break
    
    if request.method == 'POST':
        # Actualiza los datos del usuario
        user["nombre"] = request.form['nombre']
        user["contraseña"] = request.form['contraseña']
        user["email"] = request.form['email']
        
        return redirect(url_for('panel_usuario', usuario=usuario))  # Redirige de nuevo al panel de usuario

    return render_template('panel_usuario.html', usuario=user)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "_main_":
    app.run(debug=True)