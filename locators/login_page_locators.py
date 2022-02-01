from selenium.webdriver.common.by import By

'''Локаторы в странице в которой происходит, вход в систему'''

class LoginPageLocatorsName(object):
    INPUT_USERNAME = 'Электронная почта/ БИН'
    INPUT_PASSWORD = 'Пароль'
    LOGIN_BUTTON = 'Войти'


class LoginPageLocators(object):
    RELOAD = (By.XPATH, '')
    # Ввод логина
    INPUT_USERNAME = (By.XPATH, '//*[@id="iin"]')
    # Ввод пароля
    INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]')
    # Кнопка залогиниться
    LOGIN_BUTTON = (By.XPATH, '//*[@id="kc-login"]')

    # Выбор юридическое лицо
    PROFILE_TYPE = (By.XPATH, '//*[text()="Перейти"]')
    SELECT_PROFILE_ENTITY = (By.XPATH, '//*[text()='']')
