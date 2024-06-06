# Guía de Instalación y Ejecución de SmartLunch

## Descripción
SmartLunch es una aplicación Flask para gestionar pedidos de comida. Esta guía proporciona instrucciones para configurar el entorno de desarrollo y ejecutar la aplicación.

## Requisitos Previos
- Python 3.x instalado en tu sistema.

## Pasos de Instalación

1. **Crear un Entorno Virtual:**
  ```
  python -m venv SmartLunch
  ```


2. **Activar el Entorno Virtual:**
- En Windows:
  ```
  SmartLunch\Scripts\activate
  ```
- En sistemas Unix/MacOS:
  ```
  source SmartLunch/bin/activate
  ```

3. **Actualizar pip (administrador de paquetes de Python):**
  ```
  python -m pip install --upgrade pip
  ```

4. **Instalar Dependencias:**
  ```
  python -m pip install -r requirements.txt
  ```

## Ejecución de la Aplicación

1. **Iniciar el Servidor Flask:**

  ```
  python -m flask --app .\app\app.py run 
  ```

2. **Acceder a la Aplicación:**
Una vez que el servidor esté en funcionamiento, abre un navegador web y navega a la dirección `http://localhost:5000`.

