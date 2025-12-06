from ui.base.base_page import BasePage
from playwright.sync_api import Page
import allure

from ui.locators.register_page_locators import RegisterPageLocators

class RegisterPage(BasePage):

    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)


    @allure.step('')
    def fill_register_field(self):
        self.fill_field(locator=RegisterPageLocators.NAME_FIELD, text='')
        self.fill_field(locator=RegisterPageLocators.EMAIL_FIELD, text='')
        self.fill_field(locator=RegisterPageLocators.PASSWORD_FIELD, text='')