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
from filling_fields_with_correct_data.main_page import Select250FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_250 import FNO250Page
from validation_and_description_check.validation_and_description_250 import FNO250MaxSymbolAnd0ValueCheck


@allure.tag('Автотест ФНО250')
class TestFNO250:
    # 1. Автотест сценариев варианта использования «Создание формы налоговой отчетности»
    # 2. pytest -v -s testFNO220 --alluredir reports
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
            # chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
                chrome_type=ChromeType.GOOGLE).install())
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.login = LoginPage(self.browser)
        # self.main_page = MainPageAttribute(self.browser)
        # self.main_400 = Select400FNO(self.browser)
        self.fno250page = FNO250Page(self.browser)
        self.validation = FNO250MaxSymbolAnd0ValueCheck(self.browser)
        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО220 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО220 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/250.00')
        self.fno250page.first_page()
        self.fno250page.app_1()
        self.fno250page.app_2()
        self.fno250page.app_3()
        self.fno250page.app_4()
        self.fno250page.app_5()
        self.fno250page.app_6()