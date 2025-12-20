import pytest

@pytest.mark.smoke
def test_register_ui(register_page):
    register_page.open()