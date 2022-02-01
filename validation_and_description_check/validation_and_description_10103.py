import allure

from locators.fno_10103_locators import FNO10103Locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
from locators.fno_10103_locators import FNO10103LocatorsName as N


class FNO10103ValidationAndDesc(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO10103Locators
        self.locator_main = MainPageLocators

    def first_page_check_desc(self):
        sleep(1)
        assert 'Налоговый период' in self.browser.page_source
        assert 'Код валюты' in self.browser.page_source
        assert 'Сведения о налогоплательщике' in self.browser.page_source
        assert 'Признак резидентства' in self.browser.page_source
        self.scroll('200')
        self.declaration_type_additional_with_notification()
        self.scroll('700')

        self.scroll('900')

        assert '101.03.001' in self.browser.page_source
        assert 'Сумма выплачиваемого дохода за квартал' in self.browser.page_source
        assert '1 месяц' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.FIRST_MONTH_I, name=N.FIRST_MONTH_I)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_I, name=N.FIRST_MONTH_I)
        self.check_letter_input(*self.locator.FIRST_MONTH_I, name=N.FIRST_MONTH_I)
        self.check_special_symbol_input(*self.locator.FIRST_MONTH_I, name=N.FIRST_MONTH_I)

        assert '2 месяц' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.SECOND_MONTH_I, name=N.SECOND_MONTH_I)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_I, name=N.SECOND_MONTH_I)
        self.check_letter_input(*self.locator.SECOND_MONTH_I, name=N.SECOND_MONTH_I)
        self.check_special_symbol_input(*self.locator.SECOND_MONTH_I, name=N.SECOND_MONTH_I)

        assert '3 месяц' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.THIRD_MONTH_I, name=N.THIRD_MONTH_I)
        self.check_zero_value_input(*self.locator.THIRD_MONTH_I, name=N.THIRD_MONTH_I)
        self.check_letter_input(*self.locator.THIRD_MONTH_I, name=N.THIRD_MONTH_I)
        self.check_special_symbol_input(*self.locator.THIRD_MONTH_I, name=N.THIRD_MONTH_I)

        assert '101.03.002' in self.browser.page_source
        assert 'Сумма налога, удержанного у источника выплаты за квартал' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.FIRST_MONTH_II, name=N.FIRST_MONTH_II)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_II, name=N.FIRST_MONTH_II)
        self.check_letter_input(*self.locator.FIRST_MONTH_II, name=N.FIRST_MONTH_II)
        self.check_special_symbol_input(*self.locator.FIRST_MONTH_II, name=N.FIRST_MONTH_II)

        self.max_symbol_15_input(*self.locator.SECOND_MONTH_II, name=N.SECOND_MONTH_II)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_II, name=N.SECOND_MONTH_II)
        self.check_letter_input(*self.locator.SECOND_MONTH_II, name=N.SECOND_MONTH_II)
        self.check_special_symbol_input(*self.locator.SECOND_MONTH_II, name=N.SECOND_MONTH_II)

        self.max_symbol_15_input(*self.locator.THIRD_MONTH_II, name=N.THIRD_MONTH_II)
        self.check_zero_value_input(*self.locator.THIRD_MONTH_II, name=N.THIRD_MONTH_II)
        self.check_letter_input(*self.locator.THIRD_MONTH_II, name=N.THIRD_MONTH_II)
        self.check_special_symbol_input(*self.locator.THIRD_MONTH_II, name=N.THIRD_MONTH_II)

        self.scroll('900')
        self.after_button_click()
        assert 'Раздел. Ответственность налогового агента' in self.browser.page_source
        assert 'Код ОГД' in self.browser.page_source
        self.side_stepper_false()
        self.check_without_filling_ogd_code()



