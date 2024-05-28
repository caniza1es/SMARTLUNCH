import psycopg2

class Usuarios:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

    def agregar_usuario(self, nombre, usuario, contrasena, email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Usuario (nombre, usuario, contraseña, email) VALUES (%s, %s, %s, %s)",
                           (nombre, usuario, contrasena, email))
            self.connection.commit()
        finally:
            cursor.close()

    def borrar_usuario(self, usuario, contrasena):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Usuario WHERE usuario = %s AND contraseña = %s", (usuario, contrasena))
            self.connection.commit()
        finally:
            cursor.close()

    def actualizar_usuario(self, usuario, nombre, nuevo_usuario, nueva_contrasena, nuevo_email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Usuario SET nombre = %s, usuario = %s, contraseña = %s, email = %s WHERE usuario = %s",
                           (nombre, nuevo_usuario, nueva_contrasena, nuevo_email, usuario))
            self.connection.commit()
        finally:
            cursor.close()

    def consultar_usuario(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE usuario = %s", (usuario,))
            user_data = cursor.fetchone()
            return user_data
        finally:
            cursor.close()

    def __del__(self):
        self.connection.close()