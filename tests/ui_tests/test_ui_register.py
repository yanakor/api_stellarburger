import pytest

@pytest.mark.smoke
def test_register_ui(register_page):
    register_page.open("")

def test_login(register_page):
    register_page.open('/login')
    register_page.fill_login_form('test@teta.com', '3333333')
    register_page.click_on_login_btn()
