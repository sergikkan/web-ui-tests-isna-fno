#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select860FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_860 import FNO860Page
from validation_and_description_check.validation_and_description_860 import FNO860MaxSymbolAnd0ValueCheck
from promt_check.fno_860_promt_check import FNO860Promt

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


@allure.tag('Автотест ФНО860')
class TestFNO860:
    # 1. Автотест сценариев варианта использования «Создание формы налоговой отчетности»
    # 2. pytest -v -s testFNO910 --alluredir reports
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
        self.main_page = MainPageAttribute(self.browser)
        self.main_860 = Select860FNO(self.browser)
        self.fno860page = FNO860Page(self.browser)
        self.validation = FNO860MaxSymbolAnd0ValueCheck(self.browser)
        self.promt = FNO860Promt(self.browser)
        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО860 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО860 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/860.00')
        # self.main_page.select_profile_individual()
        # self.main_860.open_860_fno()
        # self.fno860page.tax_period_select()
        self.fno860page.first_page()
        self.fno860page.second_page()
        self.fno860page.third_page()

    @allure.title('Проверка валидации, описания по постановке, и названия полей')
    @allure.description('Проверка ограничения максимальных символов по ФНО 860')
    @allure.severity(severity_level='CRITICAL')
    def test_front_validation_fno860(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/860.00')
        # self.main_page.select_profile_individual()
        # self.main_860.open_860_fno()
        # self.fno860page.tax_period_select()
        self.validation.first_page()
        self.validation.second_page()

    @allure.title('Проверк подсказок ФНО 860')
    @allure.description('Проверка подскзаок по ФНО 86')
    @allure.severity(severity_level='CRITICAL')
    def test_promt_check_860(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_860.open_860_fno()
        self.fno860page.tax_period_select()
        self.fno860page.first_page()
        self.promt.promt_check()

