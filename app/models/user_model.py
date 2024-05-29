from werkzeug.security import generate_password_hash
from .db import get_db_connection  
import psycopg2

def register_user(nombre, usuario, contrasena, email):
    """
    Registra un nuevo usuario en la base de datos.

    Args:
        nombre (str): El nombre completo del usuario.
        usuario (str): El nombre de usuario del usuario.
        contrasena (str): La contraseña del usuario.
        email (str): El correo electrónico del usuario.

    Returns:
        str or None: Mensaje de error si ocurre un error durante el registro, None si el registro es exitoso.
    """
    hashed_password = generate_password_hash(contrasena)
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO Usuario (nombre, usuario, contrasena, email) VALUES (%s, %s, %s, %s)",
                    (nombre, usuario, hashed_password, email)
                )
                conn.commit()
    except psycopg2.IntegrityError as e:
        error_msg = str(e)
        error = "El nombre de usuario o el correo electrónico ya están en uso." if 'usuario' in error_msg or 'email' in error_msg else "Error en el registro. Por favor, inténtelo de nuevo más tarde."
        return error
    return None

def get_user_by_username(usuario):
    """
    Obtiene un usuario de la base de datos por su nombre de usuario.

    Args:
        usuario (str): El nombre de usuario del usuario.

    Returns:
        tuple or None: La información del usuario si se encuentra, None si no se encuentra ningún usuario con ese nombre de usuario.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Usuario WHERE usuario = %s", (usuario,))
            return cur.fetchone()

def get_user_by_email(email):
    """
    Obtiene un usuario de la base de datos por su correo electrónico.

    Args:
        email (str): El correo electrónico del usuario.

    Returns:
        tuple or None: La información del usuario si se encuentra, None si no se encuentra ningún usuario con ese correo electrónico.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Usuario WHERE email = %s", (email,))
            return cur.fetchone()

def update_user(usuario, nombre, contrasena, email):
    """
    Actualiza la información de un usuario en la base de datos.

    Args:
        usuario (str): El nombre de usuario del usuario.
        nombre (str): El nuevo nombre completo del usuario.
        contrasena (str): La nueva contraseña del usuario.
        email (str): El nuevo correo electrónico del usuario.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE Usuario SET nombre = %s, contrasena = %s, email = %s WHERE usuario = %s",
                (nombre, contrasena, email, usuario)
            )
            conn.commit()
