#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select910FNO, MainPageAttribute
from promt_check.fno_910_promt_check import FNO_910_promt
from filling_fields_with_correct_data.page_fno_910 import FNO910Page
from validation_and_description_check.validation_and_description_910 import FNO910MaxSymbolAnd0ValueCheck, \
    FNO910WithDescription

browser = webdriver.Chrome
@allure.tag('Автотест ФНО910')
class TestFNO910:
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
            #chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
                chrome_type=ChromeType.GOOGLE).install())
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.login = LoginPage(self.browser)
        self.main_page = MainPageAttribute(self.browser)
        self.main_910 = Select910FNO(self.browser)
        self.fno910page = FNO910Page(self.browser)
        self.promt = FNO_910_promt(self.browser)
        self.validation = FNO910MaxSymbolAnd0ValueCheck(self.browser)
        self.description = FNO910WithDescription(self.browser)

        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО910 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО910 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one(self):
        self.login.make_login()
        self.main_910.open_910_fno()
        self.fno910page.tax_period_select()
        self.fno910page.first_page_without_annexes_to_tax_reporting()
        self.fno910page.second_page()
        self.fno910page.third_page()
        self.fno910page.fourth_page()
        self.fno910page.sending_page()

    @allure.title('Проверка подсказок ФНО 910')
    @allure.description('Проверка всех подсказок ФНО 910')
    @allure.severity(severity_level='MEDIUM')
    def test_prompt_fno910(self):
        self.login.make_login_entity()
        self.main_910.open_910_fno()
        self.fno910page.tax_period_select()
        self.promt.activate_promt()
        self.promt.first_page_promt()
        self.promt.second_page_promt()
        self.promt.third_page_promt()
        self.promt.sending_page_promt()

    @allure.title('Проверка максимальных символов по ФНО 910')
    @allure.description('Проверка ограничения максимальных символов по ФНО 910')
    @allure.severity(severity_level='CRITICAL')
    def test_front_validation_fno910(self):
        self.login.make_login()
        self.main_910.open_910_fno()
        self.fno910page.tax_period_select()
        self.validation.first_page()
        self.validation.second_page_validation_test()
        self.validation.third_page_validation_test()

    @allure.title('Проверка ошибок по ФЛК ФНО910')
    @allure.description('Проверка ошибок по ФНО910 ФЛК (описание) ')
    @allure.severity(severity_level='CRITICAL')
    def test_description_fno910(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_910.open_910_fno()
        self.fno910page.tax_period_select()
        self.description.currency_decsription_test_with_no_tenge()
        self.description.return_to_first_page()
        self.description.assert_required_field()
        self.description.tis_description_test()
        self.description.continue_two_page()
        self.description.check_description_second_page()
