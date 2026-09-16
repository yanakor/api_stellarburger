from ui.base.base_page import BasePage
from playwright.sync_api import Page

from ui.locators.register_page_locators import LoginPageLocators


class RegisterPage(BasePage):

    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)

    def open_main_page(self):
        self.open(self.base_url)

    def click_on_login_btn(self):
        self.click_on_el(LoginPageLocators.LOGIN_BUTTON)

    def fill_login_form(self, login, password):
        self.fill_field(LoginPageLocators.LOGIN_EMAIL_FIELD, text=login)
        self.fill_field(LoginPageLocators.LOGIN_PASSWORD_FIELD, text=password)
