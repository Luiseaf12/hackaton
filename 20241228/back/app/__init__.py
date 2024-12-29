from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
import sys
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()
migrate = Migrate()

def crear_usuario_admin():
    """Crea el usuario administrador si no existe ningún usuario"""
    from app.modelos.usuario import Usuario

    try:
        if Usuario.query.first() is None:
            admin = Usuario(
                nombre="Administrador",
                apellido="Sistema",
                email="admin@sistema.com",
                nombre_usuario="admin",
            )
            admin.establecer_contraseña("xs1")
            admin.rol = "administrador"
            db.session.add(admin)
            db.session.commit()
            print("Usuario administrador creado exitosamente")
    except Exception as e:
        print(f"Error al crear usuario administrador: {str(e)}")
        db.session.rollback()

def crear_app(config_class=Config):
    """
    Función factory para crear la aplicación Flask
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registro de blueprints
    from app.rutas import bp as rutas_bp
    app.register_blueprint(rutas_bp)

    with app.app_context():
        try:
            # Intentar conectar a la base de datos
            db.engine.connect()
            print("Conexión exitosa a la base de datos")
            
            # Crear tablas si no existen
            db.create_all()
            # Crear usuario administrador si no existe ningún usuario
            crear_usuario_admin()
            
        except OperationalError as e:
            print("Error de conexión a la base de datos:")
            print(f"Host: {app.config['DB_HOST']}")
            print(f"Puerto: {app.config['DB_PORT']}")
            print(f"Base de datos: {app.config['DB_NAME']}")
            print(f"Usuario: {app.config['DB_USER']}")
            print("Error específico:", str(e))
            print("\nPor favor, verifica:")
            print("1. Que la base de datos esté activa")
            print("2. Que las credenciales sean correctas")
            print("3. Que el grupo de seguridad permita conexiones desde tu IP")
            sys.exit(1)

    return app
