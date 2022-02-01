#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select10102FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_10102 import FNO_10102_page
from promt_check.fno_10102_promt_check import PromtFNO1002
from field_validation_check.field_validation_check_10102 import FNO10102FieldCheck
from validation_and_description_check.validation_and_description_10102 import FNO10102ValidationAndDescription


@allure.tag('Автотест ФНО 101.02')
class TestFNO10102:
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
        self.main_10102 = Select10102FNO(self.browser)
        self.FNO10102 = FNO_10102_page(self.browser)
        self.promt = PromtFNO1002(self.browser)
        self.field_check = FNO10102FieldCheck(self.browser)
        self.desc = FNO10102ValidationAndDescription(self.browser)

        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('ФНО 101.02 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.02, с заполнением всех полей, выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.02')
    @allure.severity(severity_level="CRITICAL")
    def test_scenario_one_with_select_subparagraph(self):

        #self.main_page.select_profile_individual()
        #self.main_10102.open_10102_fno()
        self.browser.get('https://knp.isna.kz/document-submit/101.02')
        #self.FNO10102.tax_period_select()
        self.FNO10102.first_page_first_option()
        self.FNO10102.second_page_with_input_first_two_input()
        self.FNO10102.second_page_select_first_subparapgraph()
        self.FNO10102.third_page()

    @allure.title('ФНО 101.02 cо вторым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.02, с заполнением всех полей, выбор с подпунктом 2) пункта 5 статьи 305')
    @allure.tag('ФНО 101.02')
    @allure.severity(severity_level="CRITICAL")
    def test_scenario_two(self):
        self.login.make_login()
        #self.main_page.select_profile_individual()
        #self.main_10102.open_10102_fno()
        #self.FNO10102.tax_period_select()
        self.browser.get('https://knp.isna.kz/document-submit/101.02')
        self.FNO10102.first_page_second_option()
        self.FNO10102.second_page_with_input_first_two_input()
        self.FNO10102.second_page_select_second_subparagraph()
        self.FNO10102.third_page()

    @allure.title('Проверка подсказок ФНО 101.02 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.02, проверка подсказок, выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.02')
    @allure.severity(severity_level="CRITICAL")
    def test_promt_10102_first_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10102.open_10102_fno()
        self.FNO10102.tax_period_select()
        self.promt.activate_promt()
        self.promt.first_page_promt_check()
        self.FNO10102.select_first_subparagraph()
        self.promt.second_page_with_first_option_promt_check()

    @allure.title('Проверка по ФЛК, "Описание" ФНО 101.02 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, проверка описания ФЛК и максимальное кол-во символов,'
                        ' выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    def test_10102_with_description_first_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10102.open_10102_fno()
        self.FNO10102.tax_period_select()
        self.desc.section_general_information()
        self.desc.section_information_about_taxpayer()
        self.desc.select_first_subparagraph()
        self.desc.after_button_first_page()
        self.desc.second_page_with_input_first_two_input()
        self.desc.second_page_select_first_subparapgraph()
        self.desc.to_form()

    @allure.title('Проверка по ФЛК, "Описание" ФНО 101.02 c вторым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.02, проверка описания ФЛК и максимальное кол-во символов,'
                        ' выбор с подпунктом 2) пункта 5 статьи 305')
    @allure.tag('ФНО 101.02')
    @allure.severity(severity_level="CRITICAL")
    def test_10102_with_description_second_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10102.open_10102_fno()
        self.FNO10102.tax_period_select()
        self.desc.section_general_information()
        self.desc.section_information_about_taxpayer()
        self.desc.select_second_subparagraph()
        self.desc.after_button_first_page()
        self.desc.second_page_with_input_first_two_input()
        self.desc.second_page_select_second_subparapgraph()
        self.desc.to_form()

    @allure.title('Проверка правильности названия полей, по ФЛК')
    @allure.tag('ФНО 101.02')
    @allure.severity(severity_level="MEDIUM")
    def test_field_name_check(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10102.open_10102_fno()
        self.FNO10102.tax_period_select()
        self.field_check.all_field_name_check()
