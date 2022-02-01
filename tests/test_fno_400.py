#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select400FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_400 import FNO400Page
from validation_and_description_check.validation_and_description_400 import FNO400MaxSymbolAnd0ValueCheck
from promt_check.fno_400_promt_check import FNO400Promt

@allure.tag('Автотест ФНО400')
class TestFNO400:
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
        self.main_page = MainPageAttribute(self.browser)
        self.main_400 = Select400FNO(self.browser)
        self.fno400page = FNO400Page(self.browser)
        self.promt = FNO400Promt(self.browser)
        self.validation = FNO400MaxSymbolAnd0ValueCheck(self.browser)
        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('Тестовый сценарий 1 ФНО400 (стандартный с корректными данными)')
    @allure.description('Тестовый сценарий 1 ФНО400 (стандартный с корректными данными)')
    @allure.severity(severity_level='CRITICAL')
    def test_scenario_one(self):
        self.login.make_login_entity()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page()
        self.fno400page.second_page()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_two(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_002()
        self.fno400page.second_page_002()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_three(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_003()
        self.fno400page.second_page_003()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_four(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_004()
        self.fno400page.second_page_004()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_five(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_005()
        self.fno400page.second_page_005()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_six(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_006()
        self.fno400page.second_page_006()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_seven(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_007()
        self.fno400page.second_page_007()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    def test_scenario_eight(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_008()
        self.fno400page.second_page_008()
        self.fno400page.third_page()
        self.fno400page.fourth_page()

    @allure.title('Проверка валидации, описания по постановке, и названия полей')
    @allure.description('Проверка ограничения максимальных символов по ФНО 400')
    @allure.severity(severity_level='CRITICAL')
    def test_front_validation_fno400_01(self):
        self.login.make_login_entity()
        self.main_400.open_400_fno()
        self.fno400page.select_date_tax_pay()
        self.validation.first_validation_page_1()
        self.validation.second_validation_page_1()
        self.validation.validation_page_3()

    def test_front_validation_fno400_02(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_002()
        self.validation.second_validation_page_2()

    def test_front_validation_fno400_03(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_003()
        self.validation.second_validation_page_3()

    def test_front_validation_fno400_04(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_004()
        self.validation.second_validation_page_4()

    def test_front_validation_fno400_05(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_005()
        self.validation.second_validation_page_5()

    def test_front_validation_fno400_06(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_006()
        self.validation.second_validation_page_6()

    def test_front_validation_fno400_07(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_007()
        self.validation.second_validation_page_7()

    def test_front_validation_fno400_08(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.fno400page.first_page_008()
        self.validation.second_validation_page_8()

    # ПОДСКАЗКИ
    def test_scenario_promt_check(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/400.00')
        # self.main_400.open_400_fno()
        # self.fno400page.select_date_tax_pay()
        self.promt.promt_check()
