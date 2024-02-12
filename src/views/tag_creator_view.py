from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
        responsabilidade para interagir com HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # métodos em classe precisa ter o "self"
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        # lógica de regra de negócio
        formatted_response = tag_creator_controller.create(product_code)

        # retorno HTTP
        return HttpResponse(status_code=200, body=formatted_response)
