from api.register_user import RegisterUser
class TestRegistration:

    def test_register_new_user(self):
        new_user = RegisterUser()
        response = new_user.register_new_user()
        assert response.status_code == 200


