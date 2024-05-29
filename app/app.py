from flask import Flask
from controllers.user_controller import login, register, login_user, logout, user_panel, favicon
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

#reglas de URL para las diferentes vistas
app.add_url_rule('/', 'login', login)
app.add_url_rule('/registro', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/inicio_sesion', 'login_user', login_user, methods=['GET', 'POST'])
app.add_url_rule('/cerrar_sesion', 'logout', logout)
app.add_url_rule('/panel_usuario/<usuario>', 'user_panel', user_panel, methods=['GET', 'POST'])
app.add_url_rule('/favicon.ico', 'favicon', favicon)

if __name__ == "__main__":
    app.run(debug=True)
