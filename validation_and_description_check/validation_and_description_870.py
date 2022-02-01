from browser_interaction import BasePage
from time import sleep
from locators.fno_870_locators import FNO870Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_870_locators import FNO870LocatorsName as N
import allure


class FNO860MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO870Locators

        '''Ниже первая страница'''

    def first_page(self):
        self.declaration_type_additional_with_notification()
        self.scroll_500_px()
        self.scroll_500_px()
        self.find_element(*self.locator.BIN).send_keys('020140007102 ')
        self.find_element(*self.locator.TAXPAYER_CATEGORIES).click()
        self.find_element(*self.locator.TAXPAYER_CATEGORIES_SELECT).click()
        self.find_element(*self.locator.SUBMITTED_ANNEXES_TO_TAX_REPORTING).click()
        sleep(0.5)
        self.find_element(*self.locator.SELECT_APPLICATIONS_TO_TAX_REPORTING).click()
        self.after_button_click()

    def second_page(self):
        self.side_stepper_go_to_first_page()
        sleep(0.5)
        self.find_element(*self.locator.ENVIRONMENTAL_PERMIT).click()
        self.scroll_200_px()
        assert 'Дата выдачи' in self.browser.page_source
        assert '№ разрешительного документа' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.PEMISSION_NO, name=N.PEMISSION_NO)
        self.check_data_type_string(*self.locator.PEMISSION_NO, name=N.PEMISSION_NO)
        self.check_data_type_special_symbol(*self.locator.PEMISSION_NO, name=N.PEMISSION_NO)

        self.max_symbol_3_input(*self.locator.TYPE_OF_POLLUTANT_PARAGRAPH, N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_letter_input(*self.locator.TYPE_OF_POLLUTANT_PARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_data_type_special_symbol(*self.locator.TYPE_OF_POLLUTANT_PARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_zero_value_input(*self.locator.TYPE_OF_POLLUTANT_PARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)

        self.max_symbol_3_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_letter_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_data_type_special_symbol(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)
        self.check_zero_value_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_PARAGRAPH)

        self.max_symbol_9_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_SUBPARAGRAPH)
        self.check_letter_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_SUBPARAGRAPH)
        self.max_symbol_9_input_fractional_number(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_SUBPARAGRAPH)
        self.check_zero_value_input(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH, name=N.TYPE_OF_POLLUTANT_SUBPARAGRAPH)
        self.scroll('700')
        self.max_symbol_12_input(*self.locator.FIRST_MONTH_LIMIT, name=N.FIRST_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.FIRST_MONTH_LIMIT)
        self.check_letter_input(*self.locator.FIRST_MONTH_LIMIT)

        self.max_symbol_12_input(*self.locator.SECOND_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.SECOND_MONTH_LIMIT)
        self.check_letter_input(*self.locator.SECOND_MONTH_LIMIT)

        self.max_symbol_12_input(*self.locator.THIRD_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.THIRD_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.THIRD_MONTH_LIMIT)
        self.check_letter_input(*self.locator.THIRD_MONTH_LIMIT)

        self.max_symbol_12_input(*self.locator.FIRST_MONTH_FACT)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_FACT)
        self.check_data_type_fractional_numbers(*self.locator.FIRST_MONTH_FACT)
        self.check_letter_input(*self.locator.FIRST_MONTH_FACT)

        self.max_symbol_12_input(*self.locator.SECOND_MONTH_FACT)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_FACT)
        self.check_data_type_fractional_numbers(*self.locator.SECOND_MONTH_FACT)
        self.check_letter_input(*self.locator.SECOND_MONTH_FACT)

        self.max_symbol_12_input(*self.locator.SECOND_MONTH_FACT)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_FACT)
        self.check_data_type_fractional_numbers(*self.locator.SECOND_MONTH_FACT)
        self.check_letter_input(*self.locator.SECOND_MONTH_FACT)

        self.scroll_900_px()
        self.max_symbol_12_input(*self.locator.RATE_WITHIN_THE_LIMIT)
        self.check_zero_value_input(*self.locator.RATE_WITHIN_THE_LIMIT)
        self.check_data_type_fractional_numbers(*self.locator.RATE_WITHIN_THE_LIMIT)
        self.check_letter_input(*self.locator.RATE_WITHIN_THE_LIMIT)

        self.scroll_1500_px()
        self.max_symbol_12_input(*self.locator.CALCULATED_WITH_LIMIT)
        self.check_zero_value_input(*self.locator.CALCULATED_WITH_LIMIT)
        self.check_data_type_fractional_numbers(*self.locator.CALCULATED_WITH_LIMIT)
        self.check_letter_input(*self.locator.CALCULATED_WITH_LIMIT)
        self.after_button_click()

        self.side_stepper_false()
        self.check_without_filling_ogd_code()
