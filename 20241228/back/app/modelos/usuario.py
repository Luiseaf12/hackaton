from werkzeug.security import generate_password_hash, check_password_hash
from app.modelos import ModeloBase
from app import db
from datetime import datetime

class Usuario(ModeloBase):
    """Modelo para la gestión de usuarios en el sistema"""
    __tablename__ = 'usuarios'

    nombre = db.Column(db.String(64), nullable=False)
    apellido = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    nombre_usuario = db.Column(db.String(64), unique=True, nullable=False, index=True)
    hash_contraseña = db.Column(db.String(256))
    esta_activo = db.Column(db.Boolean, default=True)
    ultimo_acceso = db.Column(db.DateTime, default=None)
    rol = db.Column(db.String(20), default='usuario')

    def __init__(self, nombre, apellido, email, nombre_usuario, contraseña=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nombre_usuario = nombre_usuario
        if contraseña:
            self.establecer_contraseña(contraseña)

    def establecer_contraseña(self, contraseña):
        """Establece la contraseña del usuario de forma segura"""
        self.hash_contraseña = generate_password_hash(contraseña)

    def verificar_contraseña(self, contraseña):
        """Verifica si la contraseña proporcionada es correcta"""
        return check_password_hash(self.hash_contraseña, contraseña)

    def actualizar_ultimo_acceso(self):
        """Actualiza la marca de tiempo del último acceso"""
        self.ultimo_acceso = datetime.utcnow()
        db.session.commit()

    def to_dict(self):
        """Convierte el usuario a un diccionario para la API"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'nombre_usuario': self.nombre_usuario,
            'esta_activo': self.esta_activo,
            'ultimo_acceso': self.ultimo_acceso.isoformat() if self.ultimo_acceso else None,
            'rol': self.rol,
            'creado_en': self.creado_en.isoformat(),
            'actualizado_en': self.actualizado_en.isoformat()
        }

    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'
