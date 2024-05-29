from flask import render_template, request, redirect, url_for, session, send_from_directory, current_app, flash
from werkzeug.security import check_password_hash, generate_password_hash
from models.user_model import register_user, get_user_by_username, update_user, get_user_by_email

def login():
    """
    Renderiza la plantilla 'inicio_sesion.html' para la página de inicio de sesión.

    Returns:
        str: Contenido HTML de la plantilla 'inicio_sesion.html'.
    """
    return render_template('inicio_sesion.html')

def register():
    """
    Maneja las solicitudes GET y POST para el registro de usuarios.

    Returns:
        str: Contenido HTML de la plantilla 'registro.html' en caso de una solicitud GET o
             redirecciona a la página de inicio de sesión en caso de un registro exitoso.
    """
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contraseña')
        email = request.form.get('email')


        if len(nombre) > 30 or len(usuario) > 20 or len(contrasena) > 50 or len(email) > 50:
            error = "Alguno de los campos excede el límite permitido."
            return render_template('registro.html', error=error)

        error = register_user(nombre, usuario, contrasena, email)
        if error:
            return render_template('registro.html', error=error)
        return redirect(url_for('login'))
    return render_template('registro.html')

def login_user():
    """
    Maneja las solicitudes GET y POST para el inicio de sesión de usuarios.

    Returns:
        str: Contenido HTML de la plantilla 'inicio_sesion.html' en caso de una solicitud GET o
             redirecciona al panel de usuario en caso de un inicio de sesión exitoso.
    """
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contraseña')


        if len(usuario) > 20 or len(contrasena) > 50:
            error = "Usuario o contraseña exceden el límite permitido."
            return render_template('inicio_sesion.html', error=error)

        user = get_user_by_username(usuario)
        if user and check_password_hash(user[3], contrasena):
            session['usuario'] = usuario
            return redirect(url_for('user_panel', usuario=usuario))
        else:
            error = "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo."
            return render_template('inicio_sesion.html', error=error)
    return render_template('inicio_sesion.html')

def logout():
    """
    Cierra la sesión de usuario y redirecciona a la página de inicio de sesión.

    Returns:
        werkzeug.wrappers.response.Response: Redirección a la página de inicio de sesión.
    """
    session.pop('usuario', None)
    return redirect(url_for('login'))

def user_panel(usuario):
    """
    Muestra el panel de usuario si el usuario está autenticado.

    Args:
        usuario (str): El nombre de usuario del usuario.

    Returns:
        str: Contenido HTML de la plantilla 'panel_usuario.html' si el usuario está autenticado,
             mensaje de error si el usuario no está autenticado o no se encuentra.
    """
    if 'usuario' not in session or session['usuario'] != usuario:
        return redirect(url_for('login'))

    user = get_user_by_username(usuario)
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contraseña_actual = request.form.get('contraseña_actual')
        contraseña_nueva = request.form.get('contraseña_nueva')
        email = request.form.get('email')

        if len(nombre) > 30 or len(contraseña_actual) > 50 or len(contraseña_nueva) > 50 or len(email) > 50:
            error = "Alguno de los campos excede el límite permitido."


        if not check_password_hash(user[3], contraseña_actual):
            error = 'La contraseña actual no es correcta'
        if email != user[4]:
            existing_user = get_user_by_email(email)
            if existing_user:
                error = 'El correo electrónico ya está en uso'
        if not error:
            contraseña = generate_password_hash(contraseña_nueva) if contraseña_nueva else user[3]
            update_user(usuario, nombre, contraseña, email)
            return redirect(url_for('user_panel', usuario=usuario))

    if user:
        user_dict = {
            "nombre": user[1],
            "usuario": user[2],
            "contraseña": user[3],
            "email": user[4]
        }
        return render_template('panel_usuario.html', usuario=user_dict, error=error)

    return "Usuario no encontrado", 404

def favicon():
    """
    Devuelve el icono favicon.ico.

    Returns:
        werkzeug.wrappers.response.Response: Icono favicon.ico.
    """
    return send_from_directory(current_app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
