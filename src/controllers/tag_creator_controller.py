from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
        responsabilidade para implementar as regras de negócio
    '''

    def create(
            self,
            product_code: str
    ) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    def __create_tag( # os 2 underlines (__) indicam que é um método privado
            self,
            product_code: str
    ):
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

    def __format_response( # os 2 underlines (__) indicam que é um método privado
            self,
            path_from_tag: str
    ) -> Dict:
        return {
            'data': {
                'type': 'Tag Image',
                'count': 1,
                'path': f'{path_from_tag}.png'
            }
        }
