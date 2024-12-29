from flask import Blueprint

bp = Blueprint('rutas', __name__)

from app.rutas import rutas_principales, usuarios
