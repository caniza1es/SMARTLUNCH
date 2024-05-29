from usuario import Usuarios

usuariox = Usuarios()

def agregar_usuario(nombre, usuario, contrasena, email):
    try:
        usuariox.agregar_usuario(nombre, usuario, contrasena, email)
        print("Usuario agregado correctamente")
    except Exception as e:
        print(f"Error al agregar usuario: {e}")

def consultar_usuario(usuario):
    try:
        user_data = usuariox.consultar_usuario(usuario)
        return user_data
    except Exception as e:
        print(f"Error al consultar usuario: {e}")

def actualizar_usuario(usuario, nombre, nuevo_usuario, nueva_contrasena, nuevo_email):
    try:
        usuariox.actualizar_usuario(usuario, nombre, nuevo_usuario, nueva_contrasena, nuevo_email)
        print("Usuario actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")


