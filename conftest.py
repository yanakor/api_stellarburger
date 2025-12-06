from trace import Trace

import requests
import allure
import pytest
from api.apis.register_user import RegisterUser
from api.endpoins.endpoints import Url, Endpoints


@pytest.fixture
def register_new_user_and_return_response():
    with allure.step('Получение данных о зарегистрированном пользователе'):
        new_user = RegisterUser()
        data = new_user.register_new_user()

        yield data

        with allure.step('Получение токена'):
            token = data[0].json()['accessToken']
        with allure.step('Удаление пользователя'):
            requests.delete(url=f"{Url.BASE_URL}{Endpoints.USER}", headers={'Authorization':f'Bearer: {token}'})


@pytest.fixture(autouse=True)
def browser_context(browser_context_args):
    viewport = {'width': 1680, 'height': 1080}
    args = {
            **browser_context_args,
            'ignore_https_errors': True,
            'viewport': viewport,
        }
    return args