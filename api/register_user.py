from faker import Faker
import requests
from endpoins.endpoints import Url, Endpoints
from helpers.helper import generate_password

class RegisterUser:

    fake = Faker()

    def register_new_user(self):

        payload = {
            "email": self.fake.email(),
            "password": generate_password(10),
            "name": self.fake.name()
        }

        response = requests.post(url=f'{Url.BASE_URL}{Endpoints.REGISTER_USER}', json=payload)
        return response

