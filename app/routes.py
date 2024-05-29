from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="123456789",
        database="Proyecto_ADDS"
    )
    return conn

@app.route('/')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contrasena = request.form['contraseña']
        email = request.form['email']
        
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO Usuario (nombre, usuario, contrasena, email) VALUES (%s, %s, %s, %s)",
                (nombre, usuario, contrasena, email)
            )
            conn.commit()
        except psycopg2.IntegrityError as e:
            conn.rollback()
            error_msg = str(e)
            if 'usuario' in error_msg or 'email' in error_msg:
                error = "El nombre de usuario o el correo electrónico ya están en uso."
                return render_template('registro.html', error=error)
            else:
                error = "Error en el registro. Por favor, inténtelo de nuevo más tarde."
                return render_template('registro.html', error=error)
        finally:
            cur.close()
            conn.close()
        
        return redirect(url_for('inicio_sesion'))

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contraseña']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Usuario WHERE usuario = %s AND contrasena = %s",
            (usuario, contrasena)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user:
            return redirect(url_for('panel_usuario', usuario=usuario))
        else:
            error = "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo."
            return render_template('inicio_sesion.html', error=error)

    return render_template('inicio_sesion.html')

@app.route('/panel_usuario/<usuario>', methods=['GET', 'POST'])
def panel_usuario(usuario):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Usuario WHERE usuario = %s", (usuario,))
    user = cur.fetchone()
    
    error = None
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña_actual = request.form['contraseña_actual']
        contraseña_nueva = request.form['contraseña_nueva']
        email = request.form['email']
        
        if contraseña_actual != user[3]:
            error = 'La contraseña actual no es correcta'
        
        if not error and contraseña_nueva:
            contraseña = contraseña_nueva
        else:

            contraseña = user[3]
        cur.execute("SELECT * FROM Usuario WHERE email = %s AND usuario != %s", (email, usuario))
        existing_user = cur.fetchone()
        if existing_user:
            error = 'El correo electrónico ya está en uso'
        
        if not error:

            cur.execute(
                "UPDATE Usuario SET nombre = %s, contraseña = %s, email = %s WHERE usuario = %s",
                (nombre, contraseña, email, usuario)
            )
            conn.commit()
            return redirect(url_for('panel_usuario', usuario=usuario))

    if user:
        user_dict = {
            "nombre": user[1],
            "contraseña": user[3],
            "email": user[4]
        }
        return render_template('panel_usuario.html', usuario=user_dict, error=error)
    
    return "Usuario no encontrado", 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
