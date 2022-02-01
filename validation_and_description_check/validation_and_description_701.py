from browser_interaction import BasePage
from time import sleep
from locators.fno_701_locators import FNO701Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_701_locators import FNO701LocatorsName as N
import allure


class FNO701MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO701Locators

        '''Ниже первая страница'''

    def first_page_validation(self):
        assert 'Вид Расчёта' in self.browser.page_source
        assert 'Налоговый период, за который представляется налоговая отчетность: год' in self.browser.page_source
        assert 'Номер уведомления' in self.browser.page_source
        assert 'Дата уведомления' in self.browser.page_source
        assert 'Код валюты' in self.browser.page_source
        assert 'Количество листов Приложения к Расчету 701.00' in self.browser.page_source
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.max_symbol_20_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_zero_value_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_special_symbol_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_letter_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.scroll('600')
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_SELECT).click()
        self.find_element(*self.locator.AFTER).click()

    def app_1_validation(self):
        self.max_symbol_12_input(*self.locator.FIELD, name=N.FIELD)
        self.check_zero_value_input(*self.locator.FIELD, name=N.FIELD)
        self.check_special_symbol_input(*self.locator.FIELD, name=N.FIELD)
        self.check_letter_input(*self.locator.FIELD, name=N.FIELD)
        self.scroll('600')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0101).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        self.find_element(*self.locator.CONFIRM).click()
        self.max_symbol_12_input(*self.locator.APP_C, name=N.APP_C)
        self.check_zero_value_input(*self.locator.APP_C, name=N.APP_C)
        self.check_special_symbol_input(*self.locator.APP_C, name=N.APP_C)
        self.check_letter_input(*self.locator.APP_C, name=N.APP_C)
        self.find_element(*self.locator.APP_C).send_keys('123zxc')
        self.find_element(*self.locator.ADD).click()
        self.scroll('600')
        self.find_element(*self.locator.AFTER).click()
        self.find_element(*self.locator.AFTER).click()
