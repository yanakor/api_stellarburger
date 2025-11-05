import allure
from api.get_character import GetCharacter

@allure.feature('Character')
@allure.suite('')
class TestCharacter:

    @allure.title
    @allure.description
    def test_get_character(self):
        character = GetCharacter()
        resp =  character.get_character()
        print(resp.json())
        assert resp.status_code == 200
        # assert len(resp.json()) == 20

        assert (resp.json()['results'][-1]['id']) == 20

    def test_get_multiple_character(self):
        character = GetCharacter()
        resp =  character.get_multiple_character(1,183)
        print(resp.json())
        # assert resp.status_code == 200

