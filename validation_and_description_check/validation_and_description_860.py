from browser_interaction import BasePage
from time import sleep
from locators.fno_860_locators import FNO860Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_860_locators import FNO860LocatorsName as N
import allure


class FNO860MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO860Locators

        '''Ниже первая страница'''

    def first_page(self):
        self.declaration_type_additional_with_notification_second()
        self.scroll_500_px()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        self.find_element(*self.locator.TRUSTEE_SELECT).click()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        self.find_element(*self.locator.SUBMITTED_ANNEXES_TO_TAX_REPORTING).click()
        sleep(0.5)
        try:
            self.find_element(*self.locator.PAYMENT_FOR_USING_WATER_RESOURCES).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Сведения о налогоплательщике выборка',
                          attachment_type=allure.attachment_type.PNG)
        self.after_button_click()

    def second_page(self):
        sleep(2)
        assert 'Наличие разрешительного документа на специальное водопользование' in self.browser.page_source
        #self.find_element(*self.locator.CHECKBOX_AVALIABLE_RESOLUTION).click()
        #assert 'Дата выдачи' in self.browser.page_source
        #assert '№ разрешительного документа' in self.browser.page_source
        self.scroll_200_px()
        assert 'Вид специального водопользования' in self.browser.page_source
        assert 'Единицы измерения водопользования' in self.browser.page_source
        #self.find_element(*self.locator.SELECT_DATE).click()
        sleep(0.5)
        #self.find_element(*self.locator.SELECT_FIRST_DATE).click()
        #self.find_element(*self.locator.SELECT_DATE).click()
        #self.find_element(*self.locator.INPUT_ALLOW_DOC).send_keys('150160')
        #self.find_element(*self.locator.SPECIAL_WATER_USING_TYPE).click()
        #self.find_element(*self.locator.INDUSTRY).click()
        #self.find_element(*self.locator.WATER_UNITS).click()
        #self.find_element(*self.locator.CUB).click()
        #assert 'Промышленность, включая теплоэнергетику' in self.browser.page_source
        #self.find_element(*self.locator.BUTTON_ADD_NEW_FORM).click()
        #self.find_element(*self.locator.BUTTON_001).click()
        self.scroll('700')
        assert '860.01.001' in self.browser.page_source
        assert 'Установленный лимит (из расчета за отчетный налоговый период)' in self.browser.page_source
        assert '1 месяц' in self.browser.page_source
        assert '2 месяц' in self.browser.page_source
        assert '3 месяц' in self.browser.page_source

        assert '860.01.003' in self.browser.page_source
        assert 'Объем водопользования сверх установленного лимита (860.01.002-860.01.001)' in self.browser.page_source
        self.max_symbol_12_input(*self.locator.FIRST_MONTH_LIMIT, name=N.FIRST_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_LIMIT, name=N.FIRST_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.FIRST_MONTH_LIMIT, name=N.FIRST_MONTH_LIMIT)
        self.check_letter_input(*self.locator.FIRST_MONTH_LIMIT, name=N.FIRST_MONTH_LIMIT)

        assert '860.01.002' in self.browser.page_source
        assert 'Фактический объем водопользования за отчетный налоговый год' in self.browser.page_source
        self.max_symbol_12_input(*self.locator.SECOND_MONTH_LIMIT, name=N.SECOND_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_LIMIT, name=N.SECOND_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.SECOND_MONTH_LIMIT, name=N.SECOND_MONTH_LIMIT)
        self.check_letter_input(*self.locator.SECOND_MONTH_LIMIT, name=N.SECOND_MONTH_LIMIT)

        assert '860.01.003' in self.browser.page_source
        assert 'Объем водопользования сверх установленного лимита (860.01.002-860.01.001)' in self.browser.page_source
        self.max_symbol_12_input(*self.locator.THIRD_MONTH_LIMIT, name=N.THIRD_MONTH_LIMIT)
        self.check_zero_value_input(*self.locator.THIRD_MONTH_LIMIT, name=N.THIRD_MONTH_LIMIT)
        self.check_special_symbol_input(*self.locator.THIRD_MONTH_LIMIT, name=N.THIRD_MONTH_LIMIT)
        self.check_letter_input(*self.locator.THIRD_MONTH_LIMIT, name=N.THIRD_MONTH_LIMIT)

        self.max_symbol_12_input(*self.locator.FIRST_MONTH_FACT, name=N.FIRST_MONTH_FACT)
        self.check_zero_value_input(*self.locator.FIRST_MONTH_FACT, name=N.FIRST_MONTH_FACT)
        self.check_letter_input(*self.locator.FIRST_MONTH_FACT, name=N.FIRST_MONTH_FACT)

        self.max_symbol_12_input(*self.locator.SECOND_MONTH_FACT, name=N.SECOND_MONTH_FACT)
        self.check_zero_value_input(*self.locator.SECOND_MONTH_FACT, name=N.SECOND_MONTH_FACT)
        self.check_letter_input(*self.locator.SECOND_MONTH_FACT, name=N.SECOND_MONTH_FACT)

        self.max_symbol_12_input(*self.locator.THIRD_MOTH_FACT, name=N.THIRD_MOTH_FACT)
        self.check_zero_value_input(*self.locator.THIRD_MOTH_FACT, name=N.THIRD_MOTH_FACT)
        self.check_letter_input(*self.locator.THIRD_MOTH_FACT, name=N.THIRD_MOTH_FACT)

        self.scroll('900')
        self.max_symbol_12_input(*self.locator.RATE_WITHIN_THE_LIMIT, name=N.RATE_WITHIN_THE_LIMIT)
        self.check_zero_value_input(*self.locator.RATE_WITHIN_THE_LIMIT, name=N.RATE_WITHIN_THE_LIMIT)
        #self.check_data_type_fractional_numbers(*self.locator.RATE_WITHIN_THE_LIMIT, name=N.RATE_WITHIN_THE_LIMIT)
        self.check_letter_input(*self.locator.RATE_WITHIN_THE_LIMIT, name=N.RATE_WITHIN_THE_LIMIT)

        self.scroll('1500')
        self.max_symbol_12_input(*self.locator.CALCULATED_WITH_LIMIT, name=N.CALCULATED_WITH_LIMIT)
        self.check_zero_value_input(*self.locator.CALCULATED_WITH_LIMIT, name=N.CALCULATED_WITH_LIMIT)
        #self.check_data_type_fractional_numbers(*self.locator.CALCULATED_WITH_LIMIT, name=N.CALCULATED_WITH_LIMIT)
        self.check_letter_input(*self.locator.CALCULATED_WITH_LIMIT, name=N.CALCULATED_WITH_LIMIT)
        self.after_button_click()

        self.side_stepper_false()
        self.check_without_filling_ogd_code()



