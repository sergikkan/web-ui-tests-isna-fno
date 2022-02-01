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
from filling_fields_with_correct_data.page_fno_500 import FNO500Page
from validation_and_description_check.validation_and_description_500 import FNO500MaxSymbolAnd0ValueCheck

browser = webdriver.Chrome


@allure.tag('Автотест ФНО500')
class TestFNO500:
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
            # chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
                chrome_type=ChromeType.GOOGLE).install())
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.login = LoginPage(self.browser)
        # self.main_page = MainPageAttribute(self.browser)
        # self.main_400 = Select400FNO(self.browser)
        self.fno500page = FNO500Page(self.browser)
        self.validation = FNO500MaxSymbolAnd0ValueCheck(self.browser)
        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО500 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО500 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one_before_2004(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/500.00')
        # self.login.make_login()
        # self.main_page.select_profile_individual()
        # self.main_400.open_400_fno()
        # self.fno500page.select_date_tax_pay()
        self.fno500page.first_page_before_2004()
        self.fno500page.app_1()
        self.fno500page.app_2()
        self.fno500page.app_3_before_2004()
        self.fno500page.app_4()
        self.fno500page.app_5()
        self.fno500page.app_6_before_2004()
        self.fno500page.app_7()
        self.fno500page.second_page()
        self.fno500page.end_page()

    def test_scenario_one_after_2005(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/500.00')
        # self.main_page.select_profile_individual()
        # self.main_400.open_400_fno()
        # self.fno500page.select_date_tax_pay()
        self.fno500page.first_page_after_2005()
        self.fno500page.app_1()
        self.fno500page.app_2()
        self.fno500page.app_3_after_2005()
        self.fno500page.app_4()
        self.fno500page.app_5()
        self.fno500page.app_6_after_2005()
        self.fno500page.app_7()
        self.fno500page.second_page()
        self.fno500page.end_page()

    def test_scenario_validation_before_2004(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/500.00')
        self.fno500page.first_page_before_2004()
        self.validation.validation_app_1()
        self.validation.validation_app_2()
        self.validation.validation_app_3_before_2004()
        self.validation.validation_app_4()
        self.validation.validation_app_5()
        self.validation.validation_app_6_before_2004()
        self.validation.validation_app_7()

    def test_scenario_validation_after_2005(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/500.00')
        self.fno500page.first_page_after_2005()
        self.validation.validation_app_1()
        self.validation.validation_app_2()
        self.validation.validation_app_3_after_2005()
        self.validation.validation_app_4()
        self.validation.validation_app_5()
        self.validation.validation_app_6_after_2005()
        self.validation.validation_app_7()
