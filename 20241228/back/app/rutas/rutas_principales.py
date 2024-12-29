from flask import jsonify
from app.rutas import bp

@bp.route('/api/estado', methods=['GET'])
def obtener_estado():
    """Ruta de prueba para verificar el estado de la API"""
    return jsonify({'estado': 'activo', 'mensaje': 'API funcionando correctamente'})
