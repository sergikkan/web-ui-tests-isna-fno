#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select10103FNO, MainPageAttribute, TaxPeriodSelect
from filling_fields_with_correct_data.page_fno_10103 import FNO10103Page
from validation_and_description_check.validation_and_description_10103 import FNO10103ValidationAndDesc
from promt_check.fno_10103_promt_check import FNO10103Promt


@allure.tag('Автотест ФНО101.03')
class TestFNO10103():
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
        self.knp = 'http://knp.sapasoft.kz/document-submit/101.03'
        self.login = LoginPage(self.browser)
        #self.browser.get(self.knp)
        self.main_page = MainPageAttribute(self.browser)
        self.main_10103 = Select10103FNO(self.browser)
        self.fno10103page = FNO10103Page(self.browser)
        #self.field_mame = FNO10103FieldCheck(self.browser)
        self.desc = FNO10103ValidationAndDesc(self.browser)
        self.promt = FNO10103Promt(self.browser)
        self.tax_period = TaxPeriodSelect(self.browser)

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

        #self.main_page.select_profile_individual()
        #self.main_10103.open_10103_fno()
        #self.tax_period.select_date_tax_pay()
        self.browser.get('https://knp.isna.kz/document-submit/101.03')
        self.login.make_login()
        self.fno10103page.first_page_with_correct_data()
        self.fno10103page.second_page_sending()

    def test_promt_10103(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/101.03')
        self.main_page.select_profile_individual()
        self.main_10103.open_10103_fno()
        self.tax_period.select_date_tax_pay()
        self.promt.activate_promt()
        self.promt.first_page_promt()

    def test_10103_with_description_and_validation(self):
        self.login.make_login()
        self.browser.get('https://knp.isna.kz/document-submit/101.03')
        #self.main_page.select_profile_individual()
        #self.main_10103.open_10103_fno()
        #self.tax_period.select_date_tax_pay()
        self.desc.first_page_check_desc()

