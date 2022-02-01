#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import allure
import pytest
from filling_fields_with_correct_data.login_page import LoginPage
from filling_fields_with_correct_data.main_page import Select10101FNO, MainPageAttribute
from filling_fields_with_correct_data.page_fno_10101 import FNO10101Page
from validation_and_description_check.validation_and_description_10101 import FNO10101WithDescription
from promt_check.fno_10101_promt_check import FNO_10101_promt
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@allure.tag('Автотест ФНО 101.01')
class TestFNO10101():
    # 1. Автотест сценариев варианта использования «Создание формы налоговой отчетности»
    # 2. pytest -v -s testFNO910 --alluredir reports
    # 3. Отчёты по тестам создадутся в report

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
            chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
                chrome_type=ChromeType.GOOGLE).install())
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(10)
        self.login = LoginPage(self.browser)
        self.main_page = MainPageAttribute(self.browser)
        self.main_10101 = Select10101FNO(self.browser)
        self.FNO10101 = FNO10101Page(self.browser)
        self.desc = FNO10101WithDescription(self.browser)
        self.promt = FNO_10101_promt(self.browser)

        yield

        try:
            self.browser.get_screenshot_as_png()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Результат теста',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.close()
        self.browser.quit()

    @allure.title('ФНО 101.01 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, с заполнением всех полей, выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    def test_scenario_one(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.FNO10101.first_page_first_option()
        self.FNO10101.second_page_first_option()
        self.FNO10101.third_page()

    @allure.title('ФНО 101.01 cо вторым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, с заполнением всех полей, выбор с подпунктом 2) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    def test_scenario_two(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.FNO10101.first_page_second_option()
        self.FNO10101.second_page_second_option()
        self.FNO10101.third_page()

    @allure.title('Проверка подсказок ФНО 101.01 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, проверка подсказок, выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.skip(reason="Нужно переделать")
    def test_promt_10101_first_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.promt.activate_promt()
        self.promt.first_page_promt_check()
        self.FNO10101.select_first_subparagraph()
        self.FNO10101.after_button_first_page()
        self.promt.second_page_with_first_option()

    @allure.title('Проверка подсказок ФНО 101.01 cо вторым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, проверка подсказок, выбор с подпунктом 2) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    @pytest.mark.skip(reason="Нужно переделать")
    def test_promt_10101_second_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.promt.activate_promt()
        self.promt.first_page_promt_check()
        self.FNO10101.select_second_subparagraph()
        self.FNO10101.after_button_first_page()
        self.promt.second_page_with_second_option()

    @allure.title('Проверка по ФЛК "Описание", названия полей, ФНО 101.01 c первым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, проверка описания ФЛК и максимальное кол-во символов,'
                        ' выбор с подпунктом 1) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    def test_10101_with_description_first_option(self):
        self.login.make_login()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.desc.section_general_information()
        self.desc.section_information_about_taxpayer()
        self.FNO10101.select_first_subparagraph()
        self.FNO10101.after_button_first_page()
        self.desc.second_page_with_first_option()
        self.desc.sending_page()

    @allure.title('Проверка по ФЛК "Описание", названия полей, ФНО 101.01 c вторым подпунтком 5 статьи.')
    @allure.description('Автотест ФНО 101.01, проверка описания ФЛК и максимальное кол-во символов,'
                        ' выбор с подпунктом 2) пункта 5 статьи 305')
    @allure.tag('ФНО 101.01')
    @allure.severity(severity_level="CRITICAL")
    def test_10101_with_description_second_option(self):
        self.login.make_login()
        self.main_page.select_profile_individual()
        self.main_10101.open_10101_fno()
        self.FNO10101.tax_period_select()
        self.desc.section_general_information()
        self.desc.section_information_about_taxpayer()
        self.FNO10101.select_second_subparagraph()
        self.FNO10101.after_button_first_page()
        self.desc.second_page_with_second_option()
        self.desc.sending_page()
