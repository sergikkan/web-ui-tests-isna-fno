#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select421FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_421 import FNO421Page
from validation_and_description_check.validation_and_description_421 import FNO421MaxSymbolAnd0ValueCheck
from time import sleep



@allure.tag('Автотест ФНО421')
class TestFNO421:
    # 1. Автотест сценариев варианта использования «Создание формы налоговой отчетности»
    # 2. pytest -v -s testFNO400 --alluredir reports
    # 3. Отчёты по тестам создадутся в reports

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.use_selenoid = False  # set to True to run tests with Selenoid

        if self.use_selenoid:
            self.browser = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities={
                    "browserName": "chrome",
                    "browserSize": "1920x1080"
                }
            )
        else:
            chrome_options = Options()
            #chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
                chrome_type=ChromeType.GOOGLE).install())
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.login = LoginPage(self.browser)
        self.main_421 = Select421FNO(self.browser)
        self.main_page = MainPageAttribute(self.browser)
        self.fno421page = FNO421Page(self.browser)
        self.vad_check = FNO421MaxSymbolAnd0ValueCheck(self.browser)
        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО421 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО421 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one(self):
        self.login.make_login()
        #self.main_421.open_421_fno()
        #self.fno421page.select_date_tax_pay()
        self.browser.get('https://knp.isna.kz/document-submit/421.00')
        self.fno421page.first_page()
        self.fno421page.app_1()
        self.fno421page.app_2()
        self.fno421page.app_3()
        self.fno421page.app_4()
        self.fno421page.third_page()
        self.fno421page.fourth_page()

    def test_front_validation_fno421(self):
        self.login.make_login()
        #self.main_421.open_421_fno()
        #self.fno421page.select_date_tax_pay()
        self.browser.get('https://knp.isna.kz/document-submit/421.00')
        self.fno421page.first_page()
        self.vad_check.second_page()
        self.vad_check.third_page()


    def test_front_validation_fno421_app2(self):
        self.login.make_login()
        #self.main_421.open_421_fno()
        #self.fno421page.select_date_tax_pay()
        self.browser.get('https://knp.isna.kz/document-submit/421.00')
        self.fno421page.first_page2()
        self.vad_check.second_page_2()

    def test_front_validation_fno421_app3(self):
        self.login.make_login()
        self.main_421.open_421_fno()
        self.fno421page.select_date_tax_pay()
        self.fno421page.first_page3()
        self.vad_check.second_page_3()

    def test_front_validation_fno421_app4(self):
        self.login.make_login()
        self.main_421.open_421_fno()
        self.fno421page.select_date_tax_pay()
        self.fno421page.first_page4()
        self.vad_check.second_page_4()

