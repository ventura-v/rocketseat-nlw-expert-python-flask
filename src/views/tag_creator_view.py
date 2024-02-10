from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsabilidade para interagir com HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # métodos em classe precisa ter o "self"
        # body = http_request.body
        # product_code = body["product_code"]

        # lógica de regra de negócio
        print('estou na minha view')
        print(http_request)
        # retorno HTTP
        return HttpResponse(status_code=200, body={"hello": "world"})
