import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    """Clase de configuración base"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave-secreta-por-defecto"

    # Configuración de la base de datos
    DB_USER = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_NAME = os.environ.get("DB_NAME", "mi_base_datos")

    # Construcción de la URL de la base de datos
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración adicional de SQLAlchemy para timeout y reconexión
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_timeout': 30,  # timeout de 30 segundos
        'pool_recycle': 3600,  # reciclar conexiones cada hora
        'connect_args': {
            'connect_timeout': 10  # timeout de conexión de 10 segundos
        }
    }
