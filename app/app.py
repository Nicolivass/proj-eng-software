from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Instâncias globais
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Configurações da aplicação
    app.config.from_object('settings.Config')
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar controladores automaticamente
    with app.app_context():
        from controllers import register_controllers
        register_controllers(app)
    
    return app

if __name__ == '__main__':
    # Import the config for the proper environment using the
    # shell var APP_ENV
    app = create_app()

    app.run()