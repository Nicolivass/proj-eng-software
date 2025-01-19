from controllers.usuario_controller import usuario_bp
from controllers.restaurante_controller import restaurante_bp
from controllers.menu_controller import menu_bp
from controllers.tipo_usuario_controller import tipo_usuario_bp

def register_controllers(app):
    app.register_blueprint(usuario_bp)
    app.register_blueprint(restaurante_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(tipo_usuario_bp)
