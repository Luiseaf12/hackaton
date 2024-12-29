from flask import jsonify, request, abort
from app.rutas import bp
from app.modelos.usuario import Usuario
from app import db
from sqlalchemy.exc import IntegrityError

@bp.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    """Crea un nuevo usuario"""
    datos = request.get_json()
    
    campos_requeridos = ['nombre', 'apellido', 'email', 'nombre_usuario', 'contraseña']
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    try:
        usuario = Usuario(
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            email=datos['email'],
            nombre_usuario=datos['nombre_usuario']
        )
        usuario.establecer_contraseña(datos['contraseña'])
        
        db.session.add(usuario)
        db.session.commit()
        
        return jsonify(usuario.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'El email o nombre de usuario ya existe'}), 400

@bp.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    """Obtiene la lista de usuarios"""
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@bp.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    """Obtiene un usuario específico por ID"""
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@bp.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    """Actualiza un usuario existente"""
    usuario = Usuario.query.get_or_404(id)
    datos = request.get_json()

    campos_actualizables = ['nombre', 'apellido', 'email', 'esta_activo']
    for campo in campos_actualizables:
        if campo in datos:
            setattr(usuario, campo, datos[campo])

    if 'contraseña' in datos:
        usuario.establecer_contraseña(datos['contraseña'])

    try:
        db.session.commit()
        return jsonify(usuario.to_dict())
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Error al actualizar el usuario'}), 400

@bp.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    """Elimina un usuario"""
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return '', 204
