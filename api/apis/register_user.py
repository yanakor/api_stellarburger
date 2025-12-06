from faker import Faker
import requests
from api.endpoins.endpoints import Url, Endpoints
from api.helpers.helper import generate_password

class RegisterUser:

    fake = Faker()

    def register_new_user(self):
        user_creds = []

        email = self.fake.email()
        password = generate_password(10)
        name = self.fake.name()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(url=f'{Url.BASE_URL}{Endpoints.REGISTER_USER}', json=payload)

        if response.status_code == 200:
            user_creds.append(email)
            user_creds.append(password)
            user_creds.append(name)


        return response, user_creds


