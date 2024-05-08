"""
Definición de la clase Usuario.

Este módulo contiene la definición de la clase Usuario utilizada para representar a los usuarios en el sistema.
"""

class Usuario:
    """
    Clase para representar a un usuario.

    Atributos:
        nombre (str): Nombre del usuario.
        usuario (str): Nombre de usuario.
        contraseña (str): Contraseña del usuario.
        email (str): Correo electrónico del usuario.
    """
    def __init__(self, nombre, usuario, contraseña, email):
        """
        Constructor de la clase Usuario.

        :param nombre: Nombre del usuario.
        :type nombre: str
        :param usuario: Nombre de usuario.
        :type usuario: str
        :param contraseña: Contraseña del usuario.
        :type contraseña: str
        :param email: Correo electrónico del usuario.
        :type email: str
        """
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        self.email = email

# Lista de usuarios de ejemplo
usuarios = [
    Usuario("Ejemplo Usuario", "ejemplo", "123456", "ejemplo@example.com")
]
