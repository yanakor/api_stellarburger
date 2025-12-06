import pytest
from playwright.sync_api import Page
from api.endpoins.endpoints import Url

from ui.pages import RegisterPage, BasePage

@pytest.fixture
def register_page(page:Page):
    return RegisterPage(page, base_url=Url.BASE_URL)