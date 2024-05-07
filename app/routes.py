from flask import Flask, render_template, request, redirect, url_for, send_from_directory

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
        
        # Simulación de inserción en la lista de usuarios
        usuarios.append({"nombre": nombre, "usuario": usuario, "contraseña": contraseña, "email": email})
        
        return redirect(url_for('inicio_sesion'))  # Redirige a la página de inicio de sesión

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        # Simulación de autenticación comparando con la lista de usuarios
        for user in usuarios:
            if user["usuario"] == usuario and user["contraseña"] == contraseña:
                return redirect(url_for('panel_usuario', usuario=usuario))  # Redirige al panel de usuario

    return render_template('inicio_sesion.html')

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

if __name__ == "__main__":
    app.run(debug=True)
