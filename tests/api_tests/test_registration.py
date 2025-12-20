import allure
import pytest
import requests
from api.endpoins.endpoints import Url, Endpoints


@allure.suite('Регистрация пользователя')
class TestRegistration:

    @pytest.mark.smoke
    def test_register_new_user_success(self, register_new_user_and_return_response):
        response = register_new_user_and_return_response[0]

        email = response.json()['user']['email']
        name = response.json()['user']['name']
        access_token = response.json()['accessToken']
        refresh_token = response.json()['refreshToken']

        assert (response.status_code == 200 and
                response.json() == f"{{'success': True, 'user': {'email': {email}, 'name': {name}},'accessToken':"
                                   f" {access_token}, 'refreshToken':{refresh_token}}}")

    @pytest.mark.smoke
    def test_register_new_user_with_same_email(self, register_new_user_and_return_response):

        data = register_new_user_and_return_response[1]

        payload = {
            'email' : data[0],
            "password": data[1],
            "name": data[2]
        }

        response = requests.post(url=f'{Url.BASE_URL}{Endpoints.REGISTER_USER}', json=payload)

        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @pytest.mark.smoke
    def test_register_new_user_without_email(self, register_new_user_and_return_response):

        data = register_new_user_and_return_response[1]

        payload = {
            "password": data[1],
            "name": data[2]
        }

        response = requests.post(url=f'{Url.BASE_URL}{Endpoints.REGISTER_USER}', json=payload)

        assert response.status_code == 403 and response.text == '{"success":false,"message":"Email, password and name are required fields"}'

