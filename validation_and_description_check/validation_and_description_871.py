from browser_interaction import BasePage
from time import sleep
from locators.fno_871_locators import FNO871Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_871_locators import FNO871LocatorsName as N
import allure


class FNO871MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO871Locators

        '''Ниже первая страница'''

    def third_page_validation(self):
        self.max_symbol_7_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_zero_value_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_special_symbol_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_letter_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)

        self.max_symbol_7_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_zero_value_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_special_symbol_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)
        self.check_letter_input(*self.locator.GENERAL_SQUARE, name=N.GENERAL_SQUARE)

        self.max_symbol_9_input(*self.locator.NUMBER_OF_TRADE_PLACES, name=N.NUMBER_OF_TRADE_PLACES)
        self.check_zero_value_input(*self.locator.NUMBER_OF_TRADE_PLACES, name=N.NUMBER_OF_TRADE_PLACES)
        self.check_special_symbol_input(*self.locator.NUMBER_OF_TRADE_PLACES, name=N.NUMBER_OF_TRADE_PLACES)
        self.check_letter_input(*self.locator.NUMBER_OF_TRADE_PLACES, name=N.NUMBER_OF_TRADE_PLACES)

        self.max_symbol_9_input(*self.locator.APP_E, name=N.APP_E)
        self.check_zero_value_input(*self.locator.APP_E, name=N.APP_E)
        self.check_special_symbol_input(*self.locator.APP_E, name=N.APP_E)
        self.check_letter_input(*self.locator.APP_E, name=N.APP_E)

        self.max_symbol_12_input(*self.locator.APP_G, name=N.APP_G)
        self.check_zero_value_input(*self.locator.APP_G, name=N.APP_G)
        self.check_special_symbol_input(*self.locator.APP_G, name=N.APP_G)
        self.check_letter_input(*self.locator.APP_G, name=N.APP_G)

        self.max_symbol_20_input(*self.locator.APP_I, name=N.APP_I)
        self.check_zero_value_input(*self.locator.APP_I, name=N.APP_I)
        self.check_special_symbol_input(*self.locator.APP_I, name=N.APP_I)
        self.check_letter_input(*self.locator.APP_I, name=N.APP_I)

        self.max_symbol_20_input(*self.locator.APP_J, name=N.APP_J)
        self.check_zero_value_input(*self.locator.APP_J, name=N.APP_J)
        self.check_special_symbol_input(*self.locator.APP_J, name=N.APP_J)
        self.check_letter_input(*self.locator.APP_J, name=N.APP_J)

        self.max_symbol_12_input(*self.locator.APP_L, name=N.APP_L)
        self.check_zero_value_input(*self.locator.APP_L, name=N.APP_L)
        self.check_special_symbol_input(*self.locator.APP_L, name=N.APP_L)
        self.check_letter_input(*self.locator.APP_L, name=N.APP_L)

        self.max_symbol_12_input(*self.locator.APP_M, name=N.APP_M)
        self.check_zero_value_input(*self.locator.APP_M, name=N.APP_M)
        self.check_special_symbol_input(*self.locator.APP_M, name=N.APP_M)
        self.check_letter_input(*self.locator.APP_M, name=N.APP_M)

        self.max_symbol_12_input(*self.locator.APP_N, name=N.APP_N)
        self.check_zero_value_input(*self.locator.APP_N, name=N.APP_N)
        self.check_special_symbol_input(*self.locator.APP_N, name=N.APP_N)
        self.check_letter_input(*self.locator.APP_N, name=N.APP_N)

        self.max_symbol_12_input(*self.locator.APP_O, name=N.APP_O)
        self.check_zero_value_input(*self.locator.APP_O, name=N.APP_O)
        self.check_special_symbol_input(*self.locator.APP_O, name=N.APP_O)
        self.check_letter_input(*self.locator.APP_O, name=N.APP_O)