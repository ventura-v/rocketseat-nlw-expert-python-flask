from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

''' criando um mock para simular a criação de um barcode genérico, 
    para não depender da utilização da biblioteca "BarcodeHandler" do "TagCreatorController"
    caso contrário, sempre que rodar o teste, será gerado um barcode
'''
@patch.object(BarcodeHandler, 'create_barcode') # gera uma espécie de espelho do BarcodeHandler

# testando a função "tag_creator_validator" do arquivo "tag_creator_validator.py"
def test_create(mock_create_barcode):
    # as funções de teste precisam começar com "_test"

    mock_value = 'image_path'
    mock_create_barcode.return_value = mock_value # mockando o BarcodeHandler, para o mesmo não ser acessado
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    ''' 
        verificar se o retorno (result) está de acordo com o esperado, isto é, um Dict com as seguintes propriedades:
        {
            'data': {
                'type': 'Tag Image',
                'count': 1,
                'path': f'{path_from_tag}.png'
            }
        }
    '''
    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    # mais verificações
    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'
