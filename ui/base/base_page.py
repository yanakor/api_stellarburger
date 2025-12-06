from playwright.sync_api import Page
import allure


class BasePage:

    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url


    @allure.suite('Открытие страницы')
    def open(self, url):
        self.page.goto(url)

    @allure.step('')
    def click_on_el(self, locator):
        self.page.click(selector=locator)

    @allure.step('')
    def fill_field(self, locator, text):
        self.page.fill(selector=locator, value=text)