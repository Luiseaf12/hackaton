from app import db

class ModeloBase(db.Model):
    """Clase base abstracta para todos los modelos"""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    creado_en = db.Column(db.DateTime, default=db.func.current_timestamp())
    actualizado_en = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
