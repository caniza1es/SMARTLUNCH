import psycopg2

class Usuarios:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='123456789',
                database='Proyecto_ADDS'
            )
            print("Conexión a la base de datos establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def agregar_usuario(self, nombre, usuario, contrasena, email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Usuario (nombre, usuario, contrasena, email) VALUES (%s, %s, %s, %s)",
                           (nombre, usuario, contrasena, email))
            self.connection.commit()
            print("Usuario agregado correctamente en la base de datos.")
        finally:
            cursor.close()

    def consultar_usuario(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE usuario = %s", (usuario,))
            user_data = cursor.fetchone()
            print(f"Datos del usuario consultado: {user_data}")
            return user_data
        finally:
            cursor.close()

    def __del__(self):
        self.connection.close()

