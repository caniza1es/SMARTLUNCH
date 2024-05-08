"""
Funciones de las vistas de la aplicación.

Este módulo contiene las funciones que manejan las vistas de la aplicación, utilizando Flask para renderizar plantillas HTML.
"""

from flask import render_template

def inicio_sesion():
    """
    Renderiza la plantilla HTML para la página de inicio de sesión.

    :return: Página de inicio de sesión renderizada.
    """
    return render_template('inicio_sesion.html')

def registro():
    """
    Renderiza la plantilla HTML para la página de registro.

    :return: Página de registro renderizada.
    """
    return render_template('registro.html')

def panel_usuario(usuario):
    """
    Renderiza la plantilla HTML para el panel de usuario.

    :param usuario: Objeto Usuario con la información del usuario.
    :type usuario: Usuario
    :return: Panel de usuario renderizado con la información del usuario.
    """
    return render_template('panel_usuario.html', usuario=usuario)
