''' 
    a classe Blueprint será utilizada para nomear todas as rotas que forem de tag
    com um nome especial, para saber as responsabilidades de cada rota
'''
from flask import Blueprint, request, jsonify
# "request" é importado para acessar os dados da requisição HTTP que chega
# "jsonify" é usado para enviar respostas em formato JSON
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

from src.errors.error_handler import handle_errors
from src.validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint('tag_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
# Decorador que define a rota /create_tage especifica que ela aceita requisições POST

def create_tags():
    # a função que é chamada quando a rota /create_tag é acessada

    # definição de protocolo HTTP, troca de dados
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code
