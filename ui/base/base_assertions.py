import allure
from playwright.sync_api import Page, expect

from ui.base.base_page import BasePage


class Assertions(BasePage):

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)

    @allure.step('')
    def check_current_url(self, url):
        expect(self.page).to_have_url(url)

