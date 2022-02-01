#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select100FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_100 import FNO100Page
from validation_and_description_check.validation_and_description_100 import FNO100MaxSymbolAnd0ValueCheck

browser = webdriver.Chrome


@allure.tag('Автотест ФНО100')
class TestFNO100:
    # 1. Автотест сценариев варианта использования «Создание формы налоговой отчетности»
    # 2. pytest -v -s testFNO400 --alluredir reports
    # 3. Отчёты по тестам создадутся в reports

    def test_scenario_one(self, browser_setup_and_teardown):
        self.login = LoginPage(browser_setup_and_teardown)
        self.main_page = MainPageAttribute(browser_setup_and_teardown)
        self.main_100 = Select100FNO(browser_setup_and_teardown)
        self.fno100page = FNO100Page(browser_setup_and_teardown)
        self.validation = FNO100MaxSymbolAnd0ValueCheck(browser_setup_and_teardown)
        self.login.make_login()
        self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.second_page()
        self.fno100page.third_page()
        self.fno100page.fourth_page()
        self.fno100page.five_page()
        self.fno100page.six_page()
        self.fno100page.app_one()
        self.fno100page.app_two()
        self.fno100page.app_three()
        self.fno100page.app_four()
        self.fno100page.app_five()
        self.fno100page.app_six()
        self.fno100page.app_seven()
        self.fno100page.app_eight()
        self.fno100page.app_nine()
        self.fno100page.app_ten()
        self.fno100page.app_eleven()
        self.fno100page.app_twelve()

    def test_validation_and_description_check(self, browser_setup_and_teardown):
        self.login = LoginPage(browser_setup_and_teardown)
        self.main_page = MainPageAttribute(browser_setup_and_teardown)
        self.main_100 = Select100FNO(browser_setup_and_teardown)
        self.fno100page = FNO100Page(browser_setup_and_teardown)
        self.validation = FNO100MaxSymbolAnd0ValueCheck(browser_setup_and_teardown)
        self.login.make_login()
        self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.validation.second_page_validation()
        self.validation.third_page_validation()
        self.validation.fourth_page_validation()
        self.fno100page.five_page()
        self.validation.sixth_page_validation()
        self.validation.validation_app_1()
        self.validation.validation_app_2()
        self.validation.validation_app_3()
        self.validation.validation_app_4()
        self.validation.validation_app_5()
        self.validation.validation_app_6()
        self.validation.validation_app_7()
        self.validation.validation_app_8()
        self.validation.validation_app_9()
        self.validation.validation_app_10()
        self.validation.validation_app_11()
        self.validation.validation_app_12()

    def test_validation_and_description_apps(self):
        self.login.make_login_entity()
        self.browser.get("https://knp.sapasoft.kz/document-submit/100.00")
        # self.login.make_login_entity()
        # self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.go_to_app_1()
        self.validation.validation_app_1()
        self.validation.validation_app_2()
        self.validation.validation_app_3()
        self.validation.validation_app_4()
        self.validation.validation_app_5()
        self.validation.validation_app_6()
        self.validation.validation_app_7()
        self.validation.validation_app_8()
        self.validation.validation_app_9()
        self.validation.validation_app_10()
        self.validation.validation_app_11()
        self.validation.validation_app_12()

    def test_validation_and_description_app_9(self):
        self.login.make_login_entity()
        self.browser.get("https://knp.sapasoft.kz/document-submit/100.00")
        # self.login.make_login_entity()
        # self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.go_to_app_9()
        self.validation.validation_app_9()

    def test_validation_and_description_app_10(self):
        self.login.make_login_entity()
        self.browser.get("https://knp.sapasoft.kz/document-submit/100.00")
        # self.login.make_login_entity()
        # self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.go_to_app_10()
        self.validation.validation_app_10()

    def test_validation_and_description_app_11(self):
        # self.login.make_login_entity()
        self.browser.get("https://knp.sapasoft.kz/document-submit/100.00")
        # self.login.make_login_entity()
        # self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.go_to_app_11()
        self.validation.validation_app_11()

    def test_validation_and_description_app_12(self):
        # self.login.make_login_entity()
        self.browser.get("https://knp.sapasoft.kz/document-submit/100.00")
        # self.login.make_login_entity()
        # self.main_100.open_100_fno()
        self.fno100page.first_page_1()
        self.fno100page.go_to_app_12()
        self.validation.validation_app_12()
