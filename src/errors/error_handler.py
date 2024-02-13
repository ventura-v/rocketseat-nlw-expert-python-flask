from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        '''
            exemplos de processos no tratamento dos erros
                enviar para um log
                enviar um e-mail de notificação
        '''
        return HttpResponse(
            status_code=error.status_code,
            body=[{
                "title": error.name,
                "detail": error.message
            }]
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
