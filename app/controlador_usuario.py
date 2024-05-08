"""
Módulo controlador_usuario.py

Este módulo contiene funciones para el manejo de usuarios.
"""

from usuario import Usuario, usuarios

def registrar_usuario(nombre, usuario, contraseña, email):
    """
    Registra un nuevo usuario.

    :param nombre: Nombre del usuario.
    :type nombre: str
    :param usuario: Nombre de usuario.
    :type usuario: str
    :param contraseña: Contraseña del usuario.
    :type contraseña: str
    :param email: Correo electrónico del usuario.
    :type email: str
    """
    usuarios.append(Usuario(nombre, usuario, contraseña, email))

def autenticar_usuario(usuario, contraseña):
    """
    Autentica a un usuario.

    :param usuario: Nombre de usuario.
    :type usuario: str
    :param contraseña: Contraseña del usuario.
    :type contraseña: str
    :return: El objeto Usuario si la autenticación es exitosa, None en caso contrario.
    :rtype: Usuario or None
    """
    for user in usuarios:
        if user.usuario == usuario and user.contraseña == contraseña:
            return user
    return None

def obtener_usuario_por_usuario(usuario):
    """
    Obtiene un usuario por su nombre de usuario.

    :param usuario: Nombre de usuario.
    :type usuario: str
    :return: El objeto Usuario si se encuentra, None en caso contrario.
    :rtype: Usuario or None
    """
    for u in usuarios:
        if u.usuario == usuario:
            return u
    return None

def actualizar_usuario(usuario, nombre, contraseña, email):
    """
    Actualiza la información de un usuario.

    :param usuario: Nombre de usuario.
    :type usuario: str
    :param nombre: Nuevo nombre del usuario.
    :type nombre: str
    :param contraseña: Nueva contraseña del usuario.
    :type contraseña: str
    :param email: Nuevo correo electrónico del usuario.
    :type email: str
    """
    user = obtener_usuario_por_usuario(usuario)
    if user:
        user.nombre = nombre
        user.contraseña = contraseña
        user.email = email
