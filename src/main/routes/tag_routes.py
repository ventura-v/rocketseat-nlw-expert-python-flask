''' 
    a classe Blueprint será utilizada para nomear todas as rotas que forem de tag
    com um nome especial, para saber as responsabilidades de cada rota
'''
from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tag_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])

def create_tags():
    # definição de protocolo HTTP, troca de dados
    print(request.json)
    return jsonify({ 'resp': 'ok' }), 200
