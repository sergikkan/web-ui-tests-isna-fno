from selenium.webdriver.common.by import By
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
from selenium import webdriver
import pyautogui



'''Страница в которой происходит, вход в систему'''


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators
        self.login_page_locator = LoginPageLocators

    def enter_login(self):
        self.open()
        self.find_element(*self.login_page_locator.INPUT_USERNAME).send_keys('010815501417')

    def enter_password(self):
        self.find_element(*self.login_page_locator.INPUT_PASSWORD).send_keys('!@#QWEasdzxc123')

    def login_button_click(self):
        self.find_element(*self.login_page_locator.LOGIN_BUTTON).click()

    def make_login(self):
        self.enter_login()
        self.enter_password()
        self.login_button_click()

    def make_login_entity(self):
        self.enter_login()
        self.enter_password()
        self.login_button_click()
        sleep(1)
        self.find_element(*self.login_page_locator.PROFILE_TYPE).click()
        self.scroll('1300')

        self.find_element(*self.login_page_locator.SELECT_PROFILE_ENTITY).click()
