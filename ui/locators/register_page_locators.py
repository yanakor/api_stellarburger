class RegisterPageLocators:
    NAME_FIELD = "//label[text()='Имя']/following-sibling::input"
    EMAIL_FIELD = "//label[text()='Email']/following-sibling::input"
    PASSWORD_FIELD = "//label[text()='Пароль']/following-sibling::input"


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = ".//form//input[@name='name']"  # Поле ввода email на странице входа
    LOGIN_PASSWORD_FIELD =  ".//form//input[@type='password']"  # Поле ввода пароля на странице входа
    LOGIN_BUTTON = "//button[contains(text(), 'Войти')]" # Кнопка "Войти" в форме
    LOGOUT_BUTTON = ".//button[text()='Выход']" # Кнопка "Выход" в личном кабинете
    ORDERS_HISTORY = ".//a[text()='История заказов']" # Копка "История заказов в личном кабинете "
