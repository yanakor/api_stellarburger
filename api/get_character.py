import allure
import requests
from endpoins.endpoints import Url, Endpoints

class GetCharacter:

    @allure.step('Get character info')
    def get_character(self):
        response = requests.get(url=f'{Url.BASE_URL}{Endpoints.CHARACTER}')
        return response

    def get_multiple_character(self, *args):
        response = requests.get(url=f'{Url.BASE_URL}{Endpoints.CHARACTER}/{args}')
        return response
