from browser_interaction import BasePage
from time import sleep
from locators.fno_70101_locators import FNO70101Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_70101_locators import FNO70101LocatorsName as N
import allure


class FNO70101MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO70101Locators

        '''Ниже первая страница'''

    def first_page_validation(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT_1).click()
        self.max_symbol_20_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_zero_value_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_special_symbol_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_letter_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.scroll('600')
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def second_page_validation(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_PAGE_A).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_PAGE_A_SELECT).click()
        assert 'Земельный налог на земли населенных пунктов' in self.browser.page_source
        self.max_symbol_12_input(*self.locator.SECOND_PAGE_C, name=N.SECOND_PAGE_C)
        self.check_zero_value_input(*self.locator.SECOND_PAGE_C, name=N.SECOND_PAGE_C)
        self.check_special_symbol_input(*self.locator.SECOND_PAGE_C, name=N.SECOND_PAGE_C)
        self.check_letter_input(*self.locator.SECOND_PAGE_C, name=N.SECOND_PAGE_C)

        self.max_symbol_12_input(*self.locator.SECOND_PAGE_D, name=N.SECOND_PAGE_D)
        self.check_zero_value_input(*self.locator.SECOND_PAGE_D, name=N.SECOND_PAGE_D)
        self.check_special_symbol_input(*self.locator.SECOND_PAGE_D, name=N.SECOND_PAGE_D)
        self.check_letter_input(*self.locator.SECOND_PAGE_D, name=N.SECOND_PAGE_D)

        self.max_symbol_12_input(*self.locator.SECOND_PAGE_E, name=N.SECOND_PAGE_E)
        self.check_zero_value_input(*self.locator.SECOND_PAGE_E, name=N.SECOND_PAGE_E)
        self.check_special_symbol_input(*self.locator.SECOND_PAGE_E, name=N.SECOND_PAGE_E)
        self.check_letter_input(*self.locator.SECOND_PAGE_E, name=N.SECOND_PAGE_E)

        self.max_symbol_12_input(*self.locator.SECOND_PAGE_F, name=N.SECOND_PAGE_F)
        self.check_zero_value_input(*self.locator.SECOND_PAGE_F, name=N.SECOND_PAGE_F)
        self.check_special_symbol_input(*self.locator.SECOND_PAGE_F, name=N.SECOND_PAGE_F)
        self.check_letter_input(*self.locator.SECOND_PAGE_F, name=N.SECOND_PAGE_F)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_1_validation(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.max_symbol_12_input(*self.locator.APP_C, name=N.APP_C)
        self.check_zero_value_input(*self.locator.APP_C, name=N.APP_C)
        self.check_special_symbol_input(*self.locator.APP_C, name=N.APP_C)
        self.check_letter_input(*self.locator.APP_C, name=N.APP_C)

        self.max_symbol_12_input(*self.locator.APP_D, name=N.APP_D)
        self.check_zero_value_input(*self.locator.APP_D, name=N.APP_D)
        self.check_special_symbol_input(*self.locator.APP_D, name=N.APP_D)
        self.check_letter_input(*self.locator.APP_D, name=N.APP_D)

        self.max_symbol_12_input(*self.locator.APP_E, name=N.APP_E)
        self.check_zero_value_input(*self.locator.APP_E, name=N.APP_E)
        self.check_special_symbol_input(*self.locator.APP_E, name=N.APP_E)
        self.check_letter_input(*self.locator.APP_E, name=N.APP_E)

        self.max_symbol_12_input(*self.locator.APP_F, name=N.APP_F)
        self.check_zero_value_input(*self.locator.APP_F, name=N.APP_F)
        self.check_special_symbol_input(*self.locator.APP_F, name=N.APP_F)
        self.check_letter_input(*self.locator.APP_F, name=N.APP_F)