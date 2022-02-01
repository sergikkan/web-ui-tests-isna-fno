from browser_interaction import BasePage
from time import sleep
from locators.fno_500_locators import FNO_500_Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_500_locators import FNO_500_Locators_Name as N
import allure


class FNO500MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO_500_Locators

        '''Ниже вторая страница'''

    def validation_app_1(self):
        sleep(1)
        #self.find_element(*self.locator.CHAPTER_1).click()
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.OIL_1, name=N.OIL_1)
        self.check_zero_value_input(*self.locator.OIL_1, name=N.OIL_1)
        self.check_special_symbol_input(*self.locator.OIL_1, name=N.OIL_1)
        self.check_letter_input(*self.locator.OIL_1, name=N.OIL_1)

        self.max_symbol_15_input(*self.locator.OIL_2, name=N.OIL_2)
        self.check_zero_value_input(*self.locator.OIL_2, name=N.OIL_2)
        self.check_special_symbol_input(*self.locator.OIL_2, name=N.OIL_2)
        self.check_letter_input(*self.locator.OIL_2, name=N.OIL_2)

        self.max_symbol_15_input(*self.locator.OIL_3, name=N.OIL_3)
        self.check_zero_value_input(*self.locator.OIL_3, name=N.OIL_3)
        self.check_special_symbol_input(*self.locator.OIL_3, name=N.OIL_3)
        self.check_letter_input(*self.locator.OIL_3, name=N.OIL_3)

        self.max_symbol_15_input(*self.locator.OIL_4, name=N.OIL_4)
        self.check_zero_value_input(*self.locator.OIL_4, name=N.OIL_4)
        self.check_special_symbol_input(*self.locator.OIL_4, name=N.OIL_4)
        self.check_letter_input(*self.locator.OIL_4, name=N.OIL_4)

        self.max_symbol_15_input(*self.locator.OIL_5, name=N.OIL_5)
        self.check_zero_value_input(*self.locator.OIL_5, name=N.OIL_5)
        self.check_special_symbol_input(*self.locator.OIL_5, name=N.OIL_5)
        self.check_letter_input(*self.locator.OIL_5, name=N.OIL_5)

        self.max_symbol_15_input(*self.locator.OIL_6, name=N.OIL_6)
        self.check_zero_value_input(*self.locator.OIL_6, name=N.OIL_6)
        self.check_special_symbol_input(*self.locator.OIL_6, name=N.OIL_6)
        self.check_letter_input(*self.locator.OIL_6, name=N.OIL_6)
        sleep(1)

        self.find_element(*self.locator.OIL_8).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.scroll('400')

        self.max_symbol_15_input(*self.locator.OIL_9, name=N.OIL_9)
        self.check_zero_value_input(*self.locator.OIL_9, name=N.OIL_9)
        self.check_special_symbol_input(*self.locator.OIL_9, name=N.OIL_9)
        self.check_letter_input(*self.locator.OIL_9, name=N.OIL_9)

        self.max_symbol_15_input(*self.locator.OIL_10, name=N.OIL_10)
        self.check_zero_value_input(*self.locator.OIL_10, name=N.OIL_10)
        self.check_special_symbol_input(*self.locator.OIL_10, name=N.OIL_10)
        self.check_letter_input(*self.locator.OIL_10, name=N.OIL_10)

        self.max_symbol_15_input(*self.locator.OIL_11, name=N.OIL_11)
        self.check_zero_value_input(*self.locator.OIL_11, name=N.OIL_11)
        self.check_special_symbol_input(*self.locator.OIL_11, name=N.OIL_11)
        self.check_letter_input(*self.locator.OIL_11, name=N.OIL_11)

        #self.find_element(*self.locator.CHAPTER_2).click()
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.GAS_1, name=N.GAS_1)
        self.check_zero_value_input(*self.locator.GAS_1, name=N.GAS_1)
        self.check_special_symbol_input(*self.locator.GAS_1, name=N.GAS_1)
        self.check_letter_input(*self.locator.GAS_1, name=N.GAS_1)

        self.max_symbol_15_input(*self.locator.GAS_2, name=N.GAS_2)
        self.check_zero_value_input(*self.locator.GAS_2, name=N.GAS_2)
        self.check_special_symbol_input(*self.locator.GAS_2, name=N.GAS_2)
        self.check_letter_input(*self.locator.GAS_2, name=N.GAS_2)

        self.max_symbol_15_input(*self.locator.GAS_3, name=N.GAS_3)
        self.check_zero_value_input(*self.locator.GAS_3, name=N.GAS_3)
        self.check_special_symbol_input(*self.locator.GAS_3, name=N.GAS_3)
        self.check_letter_input(*self.locator.GAS_3, name=N.GAS_3)

        self.max_symbol_15_input(*self.locator.GAS_4, name=N.GAS_4)
        self.check_zero_value_input(*self.locator.GAS_4, name=N.GAS_4)
        self.check_special_symbol_input(*self.locator.GAS_4, name=N.GAS_4)
        self.check_letter_input(*self.locator.GAS_4, name=N.GAS_4)

        self.max_symbol_15_input(*self.locator.GAS_5, name=N.GAS_5)
        self.check_zero_value_input(*self.locator.GAS_5, name=N.GAS_5)
        self.check_special_symbol_input(*self.locator.GAS_5, name=N.GAS_5)
        self.check_letter_input(*self.locator.GAS_5, name=N.GAS_5)

        self.max_symbol_15_input(*self.locator.GAS_6, name=N.GAS_6)
        self.check_zero_value_input(*self.locator.GAS_6, name=N.GAS_6)
        self.check_special_symbol_input(*self.locator.GAS_6, name=N.GAS_6)
        self.check_letter_input(*self.locator.GAS_6, name=N.GAS_6)
        self.scroll('600')

        self.find_element(*self.locator.GAS_8).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.GAS_9, name=N.GAS_9)
        self.check_zero_value_input(*self.locator.GAS_9, name=N.GAS_9)
        self.check_special_symbol_input(*self.locator.GAS_9, name=N.GAS_9)
        self.check_letter_input(*self.locator.GAS_9, name=N.GAS_9)

        self.max_symbol_15_input(*self.locator.GAS_10, name=N.GAS_10)
        self.check_zero_value_input(*self.locator.GAS_10, name=N.GAS_10)
        self.check_special_symbol_input(*self.locator.GAS_10, name=N.GAS_10)
        self.check_letter_input(*self.locator.GAS_10, name=N.GAS_10)

        self.max_symbol_15_input(*self.locator.GAS_11, name=N.GAS_11)
        self.check_zero_value_input(*self.locator.GAS_11, name=N.GAS_11)
        self.check_special_symbol_input(*self.locator.GAS_11, name=N.GAS_11)
        self.check_letter_input(*self.locator.GAS_11, name=N.GAS_11)

        #self.find_element(*self.locator.CHAPTER_3).click()
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.NATURE_GAS_1, name=N.NATURE_GAS_1)
        self.check_zero_value_input(*self.locator.NATURE_GAS_1, name=N.NATURE_GAS_1)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_1, name=N.NATURE_GAS_1)
        self.check_letter_input(*self.locator.NATURE_GAS_1, name=N.NATURE_GAS_1)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_2, name=N.NATURE_GAS_2)
        self.check_zero_value_input(*self.locator.NATURE_GAS_2, name=N.NATURE_GAS_2)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_2, name=N.NATURE_GAS_2)
        self.check_letter_input(*self.locator.NATURE_GAS_2, name=N.NATURE_GAS_2)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_3, name=N.NATURE_GAS_3)
        self.check_zero_value_input(*self.locator.NATURE_GAS_3, name=N.NATURE_GAS_3)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_3, name=N.NATURE_GAS_3)
        self.check_letter_input(*self.locator.NATURE_GAS_3, name=N.NATURE_GAS_3)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_4, name=N.NATURE_GAS_4)
        self.check_zero_value_input(*self.locator.NATURE_GAS_4, name=N.NATURE_GAS_4)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_4, name=N.NATURE_GAS_4)
        self.check_letter_input(*self.locator.NATURE_GAS_4, name=N.NATURE_GAS_4)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_5, name=N.NATURE_GAS_5)
        self.check_zero_value_input(*self.locator.NATURE_GAS_5, name=N.NATURE_GAS_5)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_5, name=N.NATURE_GAS_5)
        self.check_letter_input(*self.locator.NATURE_GAS_5, name=N.NATURE_GAS_5)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_6, name=N.NATURE_GAS_6)
        self.check_zero_value_input(*self.locator.NATURE_GAS_6, name=N.NATURE_GAS_6)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_6, name=N.NATURE_GAS_6)
        self.check_letter_input(*self.locator.NATURE_GAS_6, name=N.NATURE_GAS_6)
        self.scroll('600')

        self.find_element(*self.locator.NATURE_GAS_8).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.NATURE_GAS_9, name=N.NATURE_GAS_9)
        self.check_zero_value_input(*self.locator.NATURE_GAS_9, name=N.NATURE_GAS_9)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_9, name=N.NATURE_GAS_9)
        self.check_letter_input(*self.locator.NATURE_GAS_9, name=N.NATURE_GAS_9)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_10, name=N.NATURE_GAS_10)
        self.check_zero_value_input(*self.locator.NATURE_GAS_10, name=N.NATURE_GAS_10)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_10, name=N.NATURE_GAS_10)
        self.check_letter_input(*self.locator.NATURE_GAS_10, name=N.NATURE_GAS_10)

        self.max_symbol_15_input(*self.locator.NATURE_GAS_11, name=N.NATURE_GAS_11)
        self.check_zero_value_input(*self.locator.NATURE_GAS_11, name=N.NATURE_GAS_11)
        self.check_special_symbol_input(*self.locator.NATURE_GAS_11, name=N.NATURE_GAS_11)
        self.check_letter_input(*self.locator.NATURE_GAS_11, name=N.NATURE_GAS_11)

        #self.find_element(*self.locator.CHAPTER_4).click()
        self.scroll('400')

        self.max_symbol_15_input(*self.locator.WATER_1, name=N.WATER_1)
        self.check_zero_value_input(*self.locator.WATER_1, name=N.WATER_1)
        self.check_special_symbol_input(*self.locator.WATER_1, name=N.WATER_1)
        self.check_letter_input(*self.locator.WATER_1, name=N.WATER_1)

        self.max_symbol_15_input(*self.locator.WATER_2, name=N.WATER_2)
        self.check_zero_value_input(*self.locator.WATER_2, name=N.WATER_2)
        self.check_special_symbol_input(*self.locator.WATER_2, name=N.WATER_2)
        self.check_letter_input(*self.locator.WATER_2, name=N.WATER_2)

        self.find_element(*self.locator.WATER_3).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.WATER_4, name=N.WATER_4)
        self.check_zero_value_input(*self.locator.WATER_4, name=N.WATER_4)
        self.check_special_symbol_input(*self.locator.WATER_4, name=N.WATER_4)
        self.check_letter_input(*self.locator.WATER_4, name=N.WATER_4)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_2(self):
        sleep(1)
        self.find_element(*self.locator.PART_1).click()
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.SECOND_APP_1, name=N.SECOND_APP_1)
        self.check_zero_value_input(*self.locator.SECOND_APP_1, name=N.SECOND_APP_1)
        self.check_special_symbol_input(*self.locator.SECOND_APP_1, name=N.SECOND_APP_1)
        self.check_letter_input(*self.locator.SECOND_APP_1, name=N.SECOND_APP_1)

        self.max_symbol_15_input(*self.locator.SECOND_APP_2, name=N.SECOND_APP_2)
        self.check_zero_value_input(*self.locator.SECOND_APP_2, name=N.SECOND_APP_2)
        self.check_special_symbol_input(*self.locator.SECOND_APP_2, name=N.SECOND_APP_2)
        self.check_letter_input(*self.locator.SECOND_APP_2, name=N.SECOND_APP_2)

        self.max_symbol_15_input(*self.locator.SECOND_APP_3, name=N.SECOND_APP_3)
        self.check_zero_value_input(*self.locator.SECOND_APP_3, name=N.SECOND_APP_3)
        self.check_special_symbol_input(*self.locator.SECOND_APP_3, name=N.SECOND_APP_3)
        self.check_letter_input(*self.locator.SECOND_APP_3, name=N.SECOND_APP_3)
        self.find_element(*self.locator.PART_2).click()
        self.max_symbol_15_input(*self.locator.SECOND_APP_4, name=N.SECOND_APP_4)
        self.check_zero_value_input(*self.locator.SECOND_APP_4, name=N.SECOND_APP_4)
        self.check_special_symbol_input(*self.locator.SECOND_APP_4, name=N.SECOND_APP_4)
        self.check_letter_input(*self.locator.SECOND_APP_4, name=N.SECOND_APP_4)
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def validation_app_3_before_2004(self):
        sleep(1)
        self.find_element(*self.locator.THIRD_APP_FIRST_PART).click()
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.THIRD_APP_1, name=N.THIRD_APP_1)
        self.check_zero_value_input(*self.locator.THIRD_APP_1, name=N.THIRD_APP_1)
        self.check_special_symbol_input(*self.locator.THIRD_APP_1, name=N.THIRD_APP_1)
        self.check_letter_input(*self.locator.THIRD_APP_1, name=N.THIRD_APP_1)

        self.max_symbol_15_input(*self.locator.THIRD_APP_2, name=N.THIRD_APP_2)
        self.check_zero_value_input(*self.locator.THIRD_APP_1, name=N.THIRD_APP_2)
        self.check_special_symbol_input(*self.locator.THIRD_APP_2, name=N.THIRD_APP_2)
        self.check_letter_input(*self.locator.THIRD_APP_2, name=N.THIRD_APP_2)

        self.max_symbol_15_input(*self.locator.THIRD_APP_3, name=N.THIRD_APP_3)
        self.check_zero_value_input(*self.locator.THIRD_APP_3, name=N.THIRD_APP_3)
        self.check_special_symbol_input(*self.locator.THIRD_APP_3, name=N.THIRD_APP_3)
        self.check_letter_input(*self.locator.THIRD_APP_3, name=N.THIRD_APP_3)

        self.max_symbol_15_input(*self.locator.THIRD_APP_6, name=N.THIRD_APP_6)
        self.check_zero_value_input(*self.locator.THIRD_APP_6, name=N.THIRD_APP_6)
        self.check_special_symbol_input(*self.locator.THIRD_APP_6, name=N.THIRD_APP_6)
        self.check_letter_input(*self.locator.THIRD_APP_6, name=N.THIRD_APP_6)

        self.max_symbol_15_input(*self.locator.THIRD_APP_8, name=N.THIRD_APP_8)
        self.check_zero_value_input(*self.locator.THIRD_APP_8, name=N.THIRD_APP_8)
        self.check_special_symbol_input(*self.locator.THIRD_APP_8, name=N.THIRD_APP_8)
        self.check_letter_input(*self.locator.THIRD_APP_8, name=N.THIRD_APP_8)
        self.scroll('700')

        self.find_element(*self.locator.THIRD_APP_12).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.THIRD_APP_14, name=N.THIRD_APP_14)
        self.check_zero_value_input(*self.locator.THIRD_APP_14, name=N.THIRD_APP_14)
        self.check_special_symbol_input(*self.locator.THIRD_APP_14, name=N.THIRD_APP_14)
        self.check_letter_input(*self.locator.THIRD_APP_14, name=N.THIRD_APP_14)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_3_after_2005(self):
        sleep(1)
        self.find_element(*self.locator.THIRD_APP_SECOND_PART).click()
        self.scroll('600')
        self.max_symbol_15_input(*self.locator.THIRD_APP_15, name=N.THIRD_APP_15)
        self.check_zero_value_input(*self.locator.THIRD_APP_15, name=N.THIRD_APP_15)
        self.check_special_symbol_input(*self.locator.THIRD_APP_15, name=N.THIRD_APP_15)
        self.check_letter_input(*self.locator.THIRD_APP_15, name=N.THIRD_APP_15)

        self.max_symbol_15_input(*self.locator.THIRD_APP_17, name=N.THIRD_APP_17)
        self.check_zero_value_input(*self.locator.THIRD_APP_17, name=N.THIRD_APP_17)
        self.check_special_symbol_input(*self.locator.THIRD_APP_17, name=N.THIRD_APP_17)
        self.check_letter_input(*self.locator.THIRD_APP_17, name=N.THIRD_APP_17)

        self.max_symbol_15_input(*self.locator.THIRD_APP_19, name=N.THIRD_APP_19)
        self.check_zero_value_input(*self.locator.THIRD_APP_19, name=N.THIRD_APP_19)
        self.check_special_symbol_input(*self.locator.THIRD_APP_19, name=N.THIRD_APP_19)
        self.check_letter_input(*self.locator.THIRD_APP_19, name=N.THIRD_APP_19)

        self.max_symbol_3_input(*self.locator.THIRD_APP_22, name=N.THIRD_APP_22)
        self.check_zero_value_input(*self.locator.THIRD_APP_22, name=N.THIRD_APP_22)
        self.check_special_symbol_input(*self.locator.THIRD_APP_22, name=N.THIRD_APP_22)
        self.check_letter_input(*self.locator.THIRD_APP_22, name=N.THIRD_APP_22)

        self.max_symbol_15_input(*self.locator.THIRD_APP_23, name=N.THIRD_APP_23)
        self.check_zero_value_input(*self.locator.THIRD_APP_23, name=N.THIRD_APP_23)
        self.check_special_symbol_input(*self.locator.THIRD_APP_23, name=N.THIRD_APP_23)
        self.check_letter_input(*self.locator.THIRD_APP_23, name=N.THIRD_APP_23)

        self.max_symbol_3_input(*self.locator.THIRD_APP_26, name=N.THIRD_APP_26)
        self.check_zero_value_input(*self.locator.THIRD_APP_26, name=N.THIRD_APP_26)
        self.check_special_symbol_input(*self.locator.THIRD_APP_26, name=N.THIRD_APP_26)
        self.check_letter_input(*self.locator.THIRD_APP_26, name=N.THIRD_APP_26)

        self.find_element(*self.locator.THIRD_APP_27).send_keys('1/[]k23')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.THIRD_APP_28, name=N.THIRD_APP_28)
        self.check_zero_value_input(*self.locator.THIRD_APP_28, name=N.THIRD_APP_28)
        self.check_special_symbol_input(*self.locator.THIRD_APP_28, name=N.THIRD_APP_28)
        self.check_letter_input(*self.locator.THIRD_APP_28, name=N.THIRD_APP_28)

        self.find_element(*self.locator.THIRD_APP_29).send_keys('1/[]k23')
        assert '12' in self.browser.page_source
        self.check_zero_value_input(*self.locator.THIRD_APP_29, name=N.THIRD_APP_29)
        self.check_special_symbol_input(*self.locator.THIRD_APP_29, name=N.THIRD_APP_29)
        self.check_letter_input(*self.locator.THIRD_APP_29, name=N.THIRD_APP_29)

        self.max_symbol_15_input(*self.locator.THIRD_APP_30, name=N.THIRD_APP_30)
        self.check_zero_value_input(*self.locator.THIRD_APP_30, name=N.THIRD_APP_30)
        self.check_special_symbol_input(*self.locator.THIRD_APP_30, name=N.THIRD_APP_30)
        self.check_letter_input(*self.locator.THIRD_APP_30, name=N.THIRD_APP_30)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_4(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_12_input(*self.locator.B_APP_4, name=N.B_APP_4)

        self.max_symbol_15_input(*self.locator.C_APP_4, name=N.C_APP_4)
        self.check_zero_value_input(*self.locator.C_APP_4, name=N.C_APP_4)
        self.check_special_symbol_input(*self.locator.C_APP_4, name=N.C_APP_4)
        self.check_letter_input(*self.locator.C_APP_4, name=N.C_APP_4)

        self.max_symbol_15_input(*self.locator.D_APP_4, name=N.D_APP_4)
        self.check_zero_value_input(*self.locator.D_APP_4, name=N.D_APP_4)
        self.check_special_symbol_input(*self.locator.D_APP_4, name=N.D_APP_4)
        self.check_letter_input(*self.locator.D_APP_4, name=N.D_APP_4)

        self.max_symbol_15_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_zero_value_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_special_symbol_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_letter_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_5(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.B_APP_5).send_keys('BhjG][=034')
        sleep(0.5)
        assert 'BhjG][=034' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.C_APP_5, name=N.C_APP_5)
        self.check_zero_value_input(*self.locator.C_APP_5, name=N.C_APP_5)
        self.check_special_symbol_input(*self.locator.C_APP_5, name=N.C_APP_5)
        self.check_letter_input(*self.locator.C_APP_5, name=N.C_APP_5)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_6_before_2004(self):
        sleep(1)
        self.find_element(*self.locator.SIXTH_APP_FIRST_CHAPTER).click()
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.SIXTH_APP_2, name=N.SIXTH_APP_2)
        self.check_zero_value_input(*self.locator.SIXTH_APP_2, name=N.SIXTH_APP_2)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_2, name=N.SIXTH_APP_2)
        self.check_letter_input(*self.locator.SIXTH_APP_2, name=N.SIXTH_APP_2)

        self.max_symbol_15_input(*self.locator.SIXTH_APP_4, name=N.SIXTH_APP_4)
        self.check_zero_value_input(*self.locator.SIXTH_APP_4, name=N.SIXTH_APP_4)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_4, name=N.SIXTH_APP_4)
        self.check_letter_input(*self.locator.SIXTH_APP_4, name=N.SIXTH_APP_4)

        self.max_symbol_15_input(*self.locator.SIXTH_APP_5, name=N.SIXTH_APP_5)
        self.check_zero_value_input(*self.locator.SIXTH_APP_5, name=N.SIXTH_APP_5)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_5, name=N.SIXTH_APP_5)
        self.check_letter_input(*self.locator.SIXTH_APP_5, name=N.SIXTH_APP_5)
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def validation_app_6_after_2005(self):
        sleep(1)
        self.scroll('400')
        self.find_element(*self.locator.SIXTH_APP_SECOND_CHAPTER).click()
        self.max_symbol_15_input(*self.locator.SIXTH_APP_7, name=N.SIXTH_APP_7)
        self.check_zero_value_input(*self.locator.SIXTH_APP_7, name=N.SIXTH_APP_7)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_7, name=N.SIXTH_APP_7)
        self.check_letter_input(*self.locator.SIXTH_APP_7, name=N.SIXTH_APP_7)

        self.max_symbol_15_input(*self.locator.SIXTH_APP_8, name=N.SIXTH_APP_8)
        self.check_zero_value_input(*self.locator.SIXTH_APP_8, name=N.SIXTH_APP_8)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_8, name=N.SIXTH_APP_8)
        self.check_letter_input(*self.locator.SIXTH_APP_8, name=N.SIXTH_APP_8)
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.SIXTH_APP_9, name=N.SIXTH_APP_9)
        self.check_zero_value_input(*self.locator.SIXTH_APP_9, name=N.SIXTH_APP_9)
        self.check_special_symbol_input(*self.locator.SIXTH_APP_9, name=N.SIXTH_APP_9)
        self.check_letter_input(*self.locator.SIXTH_APP_9, name=N.SIXTH_APP_9)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_7(self):
        sleep(2)
        self.scroll('400')
        self.max_symbol_12_input(*self.locator.SEVEN_APP_1, name=N.SEVEN_APP_1)
        self.check_zero_value_input(*self.locator.SEVEN_APP_1, name=N.SEVEN_APP_1)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_1, name=N.SEVEN_APP_1)
        self.check_letter_input(*self.locator.SEVEN_APP_1, name=N.SEVEN_APP_1)

        self.max_symbol_9_input(*self.locator.SEVEN_APP_2, name=N.SEVEN_APP_2)
        self.check_zero_value_input(*self.locator.SEVEN_APP_2, name=N.SEVEN_APP_2)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_2, name=N.SEVEN_APP_2)
        self.check_letter_input(*self.locator.SEVEN_APP_2, name=N.SEVEN_APP_2)

        self.max_symbol_15_input(*self.locator.SEVEN_APP_4, name=N.SEVEN_APP_4)
        self.check_zero_value_input(*self.locator.SEVEN_APP_4, name=N.SEVEN_APP_4)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_4, name=N.SEVEN_APP_4)
        self.check_letter_input(*self.locator.SEVEN_APP_4, name=N.SEVEN_APP_4)

        self.max_symbol_12_input(*self.locator.SEVEN_APP_5, name=N.SEVEN_APP_5)
        self.check_zero_value_input(*self.locator.SEVEN_APP_5, name=N.SEVEN_APP_5)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_5, name=N.SEVEN_APP_5)
        self.check_letter_input(*self.locator.SEVEN_APP_5, name=N.SEVEN_APP_5)

        self.max_symbol_9_input(*self.locator.SEVEN_APP_6, name=N.SEVEN_APP_6)
        self.check_zero_value_input(*self.locator.SEVEN_APP_6, name=N.SEVEN_APP_6)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_6, name=N.SEVEN_APP_6)
        self.check_letter_input(*self.locator.SEVEN_APP_6, name=N.SEVEN_APP_6)
        self.scroll('800')
        self.max_symbol_15_input(*self.locator.SEVEN_APP_8, name=N.SEVEN_APP_8)
        self.check_zero_value_input(*self.locator.SEVEN_APP_8, name=N.SEVEN_APP_8)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_8, name=N.SEVEN_APP_8)
        self.check_letter_input(*self.locator.SEVEN_APP_8, name=N.SEVEN_APP_8)

        self.max_symbol_12_input(*self.locator.SEVEN_APP_9, name=N.SEVEN_APP_9)
        self.check_zero_value_input(*self.locator.SEVEN_APP_9, name=N.SEVEN_APP_9)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_9, name=N.SEVEN_APP_9)
        self.check_letter_input(*self.locator.SEVEN_APP_9, name=N.SEVEN_APP_9)

        self.max_symbol_9_input(*self.locator.SEVEN_APP_10, name=N.SEVEN_APP_10)
        self.check_zero_value_input(*self.locator.SEVEN_APP_10, name=N.SEVEN_APP_10)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_10, name=N.SEVEN_APP_10)
        self.check_letter_input(*self.locator.SEVEN_APP_10, name=N.SEVEN_APP_10)

        self.max_symbol_15_input(*self.locator.SEVEN_APP_12, name=N.SEVEN_APP_12)
        self.check_zero_value_input(*self.locator.SEVEN_APP_12, name=N.SEVEN_APP_12)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_12, name=N.SEVEN_APP_12)
        self.check_letter_input(*self.locator.SEVEN_APP_12, name=N.SEVEN_APP_12)

        self.find_element(*self.locator.SEVEN_APP_13).send_keys('1234')
        sleep(0.3)
        assert '1234' not in self.browser.page_source
        self.check_zero_value_input(*self.locator.SEVEN_APP_13, name=N.SEVEN_APP_13)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_13, name=N.SEVEN_APP_13)
        self.check_letter_input(*self.locator.SEVEN_APP_13, name=N.SEVEN_APP_13)

        self.max_symbol_15_input(*self.locator.SEVEN_APP_15, name=N.SEVEN_APP_15)
        self.check_zero_value_input(*self.locator.SEVEN_APP_15, name=N.SEVEN_APP_15)
        self.check_special_symbol_input(*self.locator.SEVEN_APP_15, name=N.SEVEN_APP_15)
        self.check_letter_input(*self.locator.SEVEN_APP_15, name=N.SEVEN_APP_15)
        self.scroll('800')
        self.find_element(*self.locator.AFTER).click()