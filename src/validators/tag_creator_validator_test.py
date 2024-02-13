from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

# testando a função "tag_creator_validator" do arquivo "tag_creator_validator.py"
def test_tag_creator_validator():
    # as funções de teste precisam começar com "_test"

    req = MockRequest(json={ 'product_code': '12345' })
    tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    # as funções de teste precisam começar com "_test"

    # função para testar o erro, logo, a requisição não pode estar correta
    req = MockRequest(json={ 'product_code': 12345 })

    try:
        tag_creator_validator(req)
        assert False
        # Como o teste é para cair na exceção, se a requisição estiver correto, é lançado um erro
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
