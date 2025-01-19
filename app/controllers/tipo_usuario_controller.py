from flask import Blueprint, request, jsonify

tipo_usuario_bp = Blueprint('tipo_usuario', __name__, url_prefix='/usuarios')