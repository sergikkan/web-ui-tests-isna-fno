from browser_interaction import BasePage
from time import sleep
from locators.fno_100_locators import FNO100Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_100_locators import FNO100LocatorsName as N


class FNO100MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO100Locators

        # НАЧАТО СО ВТОРОЙ СТРАНИЦЫ

    def second_page_validation(self):
        self.max_symbol_15_input(*self.locator.REAL_INCOME_1, name=N.REAL_INCOME_1)
        self.check_zero_value_input(*self.locator.REAL_INCOME_1, name=N.REAL_INCOME_1)
        self.check_special_symbol_input(*self.locator.REAL_INCOME_1, name=N.REAL_INCOME_1)
        self.check_letter_input(*self.locator.REAL_INCOME_1, name=N.REAL_INCOME_1)
        self.max_symbol_15_input(*self.locator.REAL_INCOME_2, name=N.REAL_INCOME_2)
        self.check_zero_value_input(*self.locator.REAL_INCOME_2, name=N.REAL_INCOME_2)
        self.check_special_symbol_input(*self.locator.REAL_INCOME_2, name=N.REAL_INCOME_2)
        self.check_letter_input(*self.locator.REAL_INCOME_2, name=N.REAL_INCOME_2)
        self.max_symbol_15_input(*self.locator.REAL_INCOME_3, name=N.REAL_INCOME_3)
        self.check_zero_value_input(*self.locator.REAL_INCOME_3, name=N.REAL_INCOME_3)
        self.check_special_symbol_input(*self.locator.REAL_INCOME_3, name=N.REAL_INCOME_3)
        self.check_letter_input(*self.locator.REAL_INCOME_3, name=N.REAL_INCOME_3)
        self.max_symbol_15_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_zero_value_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_special_symbol_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_letter_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.scroll('200')
        self.max_symbol_15_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_zero_value_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_special_symbol_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)
        self.check_letter_input(*self.locator.REAL_INCOME_4, name=N.REAL_INCOME_4)

        self.max_symbol_15_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_zero_value_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_special_symbol_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_letter_input(*self.locator.INCOME_2, name=N.INCOME_2)

        self.max_symbol_15_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_zero_value_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_special_symbol_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_letter_input(*self.locator.INCOME_3, name=N.INCOME_3)

        self.max_symbol_15_input(*self.locator.INCOME_4, name=N.INCOME_4)
        self.check_zero_value_input(*self.locator.INCOME_4, name=N.INCOME_4)
        self.check_special_symbol_input(*self.locator.INCOME_4, name=N.INCOME_4)
        self.check_letter_input(*self.locator.INCOME_4, name=N.INCOME_4)

        self.max_symbol_15_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_zero_value_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_special_symbol_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_letter_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.scroll('600')
        self.max_symbol_15_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_zero_value_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_special_symbol_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_letter_input(*self.locator.INCOME_6, name=N.INCOME_6)

        self.max_symbol_15_input(*self.locator.INCOME_6_I, name=N.INCOME_6_I)
        self.check_zero_value_input(*self.locator.INCOME_6_I, name=N.INCOME_6_I)
        self.check_special_symbol_input(*self.locator.INCOME_6_I, name=N.INCOME_6_I)
        self.check_letter_input(*self.locator.INCOME_6_I, name=N.INCOME_6_I)

        self.max_symbol_15_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_zero_value_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_special_symbol_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_letter_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)

        self.max_symbol_15_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_zero_value_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_special_symbol_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_letter_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)

        self.max_symbol_15_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_zero_value_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_special_symbol_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_letter_input(*self.locator.INCOME_8, name=N.INCOME_8)

        self.max_symbol_15_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_zero_value_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_special_symbol_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_letter_input(*self.locator.INCOME_9, name=N.INCOME_9)

        self.max_symbol_15_input(*self.locator.INCOME_10, name=N.INCOME_10)
        self.check_zero_value_input(*self.locator.INCOME_10, name=N.INCOME_10)
        self.check_special_symbol_input(*self.locator.INCOME_10, name=N.INCOME_10)
        self.check_letter_input(*self.locator.INCOME_10, name=N.INCOME_10)

        self.max_symbol_15_input(*self.locator.INCOME_11, name=N.INCOME_11)
        self.check_zero_value_input(*self.locator.INCOME_11, name=N.INCOME_11)
        self.check_special_symbol_input(*self.locator.INCOME_11, name=N.INCOME_11)
        self.check_letter_input(*self.locator.INCOME_11, name=N.INCOME_11)

        self.max_symbol_15_input(*self.locator.INCOME_12, name=N.INCOME_12)
        self.check_zero_value_input(*self.locator.INCOME_12, name=N.INCOME_12)
        self.check_special_symbol_input(*self.locator.INCOME_12, name=N.INCOME_12)
        self.check_letter_input(*self.locator.INCOME_12, name=N.INCOME_12)
        self.scroll('5000')
        self.max_symbol_15_input(*self.locator.INCOME_13, name=N.INCOME_13)
        self.check_zero_value_input(*self.locator.INCOME_13, name=N.INCOME_13)
        self.check_special_symbol_input(*self.locator.INCOME_13, name=N.INCOME_13)
        self.check_letter_input(*self.locator.INCOME_13, name=N.INCOME_13)
        self.find_element(*self.locator.AFTER).click()

    def third_page_validation(self):
        sleep(1)
        self.scroll('200')

        self.max_symbol_15_input(*self.locator.CORR_INCOME_1, name=N.CORR_INCOME_1)
        self.check_zero_value_input(*self.locator.CORR_INCOME_1, name=N.CORR_INCOME_1)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_1, name=N.CORR_INCOME_1)
        self.check_letter_input(*self.locator.CORR_INCOME_1, name=N.CORR_INCOME_1)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_2, name=N.CORR_INCOME_2)
        self.check_zero_value_input(*self.locator.CORR_INCOME_2, name=N.CORR_INCOME_2)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_2, name=N.CORR_INCOME_2)
        self.check_letter_input(*self.locator.CORR_INCOME_2, name=N.CORR_INCOME_2)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_3, name=N.CORR_INCOME_3)
        self.check_zero_value_input(*self.locator.CORR_INCOME_3, name=N.CORR_INCOME_3)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_3, name=N.CORR_INCOME_3)
        self.check_letter_input(*self.locator.CORR_INCOME_3, name=N.CORR_INCOME_3)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_4, name=N.CORR_INCOME_4)
        self.check_zero_value_input(*self.locator.CORR_INCOME_4, name=N.CORR_INCOME_4)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_4, name=N.CORR_INCOME_4)
        self.check_letter_input(*self.locator.CORR_INCOME_4, name=N.CORR_INCOME_4)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_5, name=N.CORR_INCOME_5)
        self.check_zero_value_input(*self.locator.CORR_INCOME_5, name=N.CORR_INCOME_5)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_5, name=N.CORR_INCOME_5)
        self.check_letter_input(*self.locator.CORR_INCOME_5, name=N.CORR_INCOME_5)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_6, name=N.CORR_INCOME_6)
        self.check_zero_value_input(*self.locator.CORR_INCOME_6, name=N.CORR_INCOME_6)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_6, name=N.CORR_INCOME_6)
        self.check_letter_input(*self.locator.CORR_INCOME_6, name=N.CORR_INCOME_6)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_7, name=N.CORR_INCOME_7)
        self.check_zero_value_input(*self.locator.CORR_INCOME_7, name=N.CORR_INCOME_7)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_7, name=N.CORR_INCOME_7)
        self.check_letter_input(*self.locator.CORR_INCOME_7, name=N.CORR_INCOME_7)
        self.scroll('600')
        self.max_symbol_15_input(*self.locator.CORR_INCOME_8, name=N.CORR_INCOME_8)
        self.check_zero_value_input(*self.locator.CORR_INCOME_8, name=N.CORR_INCOME_1)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_8, name=N.CORR_INCOME_8)
        self.check_letter_input(*self.locator.CORR_INCOME_8, name=N.CORR_INCOME_8)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_9, name=N.CORR_INCOME_9)
        self.check_zero_value_input(*self.locator.CORR_INCOME_9, name=N.CORR_INCOME_9)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_9, name=N.CORR_INCOME_9)
        self.check_letter_input(*self.locator.CORR_INCOME_9, name=N.CORR_INCOME_9)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_10, name=N.CORR_INCOME_10)
        self.check_zero_value_input(*self.locator.CORR_INCOME_10, name=N.CORR_INCOME_10)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_10, name=N.CORR_INCOME_10)
        self.check_letter_input(*self.locator.CORR_INCOME_10, name=N.CORR_INCOME_10)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_11, name=N.CORR_INCOME_11)
        self.check_zero_value_input(*self.locator.CORR_INCOME_11, name=N.CORR_INCOME_11)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_11, name=N.CORR_INCOME_11)
        self.check_letter_input(*self.locator.CORR_INCOME_11, name=N.CORR_INCOME_11)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_12, name=N.CORR_INCOME_12)
        self.check_zero_value_input(*self.locator.CORR_INCOME_12, name=N.CORR_INCOME_12)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_12, name=N.CORR_INCOME_12)
        self.check_letter_input(*self.locator.CORR_INCOME_12, name=N.CORR_INCOME_12)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_13, name=N.CORR_INCOME_13)
        self.check_zero_value_input(*self.locator.CORR_INCOME_13, name=N.CORR_INCOME_13)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_13, name=N.CORR_INCOME_13)
        self.check_letter_input(*self.locator.CORR_INCOME_13, name=N.CORR_INCOME_13)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_14, name=N.CORR_INCOME_14)
        self.check_zero_value_input(*self.locator.CORR_INCOME_14, name=N.CORR_INCOME_14)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_14, name=N.CORR_INCOME_14)
        self.check_letter_input(*self.locator.CORR_INCOME_14, name=N.CORR_INCOME_14)
        self.scroll('700')
        self.max_symbol_15_input(*self.locator.CORR_INCOME_15, name=N.CORR_INCOME_15)
        self.check_zero_value_input(*self.locator.CORR_INCOME_15, name=N.CORR_INCOME_15)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_15, name=N.CORR_INCOME_15)
        self.check_letter_input(*self.locator.CORR_INCOME_15, name=N.CORR_INCOME_15)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_16, name=N.CORR_INCOME_16)
        self.check_zero_value_input(*self.locator.CORR_INCOME_16, name=N.CORR_INCOME_16)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_16, name=N.CORR_INCOME_16)
        self.check_letter_input(*self.locator.CORR_INCOME_16, name=N.CORR_INCOME_16)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_17, name=N.CORR_INCOME_17)
        self.check_zero_value_input(*self.locator.CORR_INCOME_17, name=N.CORR_INCOME_17)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_17, name=N.CORR_INCOME_17)
        self.check_letter_input(*self.locator.CORR_INCOME_17, name=N.CORR_INCOME_17)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_18, name=N.CORR_INCOME_18)
        self.check_zero_value_input(*self.locator.CORR_INCOME_18, name=N.CORR_INCOME_18)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_18, name=N.CORR_INCOME_18)
        self.check_letter_input(*self.locator.CORR_INCOME_18, name=N.CORR_INCOME_18)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_19, name=N.CORR_INCOME_19)
        self.check_zero_value_input(*self.locator.CORR_INCOME_19, name=N.CORR_INCOME_19)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_19, name=N.CORR_INCOME_19)
        self.check_letter_input(*self.locator.CORR_INCOME_19, name=N.CORR_INCOME_19)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_20, name=N.CORR_INCOME_20)
        self.check_zero_value_input(*self.locator.CORR_INCOME_20, name=N.CORR_INCOME_20)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_20, name=N.CORR_INCOME_20)
        self.check_letter_input(*self.locator.CORR_INCOME_20, name=N.CORR_INCOME_20)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_21, name=N.CORR_INCOME_21)
        self.check_zero_value_input(*self.locator.CORR_INCOME_21, name=N.CORR_INCOME_21)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_21, name=N.CORR_INCOME_21)
        self.check_letter_input(*self.locator.CORR_INCOME_21, name=N.CORR_INCOME_21)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_22, name=N.CORR_INCOME_22)
        self.check_zero_value_input(*self.locator.CORR_INCOME_22, name=N.CORR_INCOME_22)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_22, name=N.CORR_INCOME_22)
        self.check_letter_input(*self.locator.CORR_INCOME_22, name=N.CORR_INCOME_22)
        self.scroll('700')
        self.max_symbol_15_input(*self.locator.CORR_INCOME_23, name=N.CORR_INCOME_23)
        self.check_zero_value_input(*self.locator.CORR_INCOME_23, name=N.CORR_INCOME_23)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_23, name=N.CORR_INCOME_23)
        self.check_letter_input(*self.locator.CORR_INCOME_23, name=N.CORR_INCOME_23)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_24, name=N.CORR_INCOME_24)
        self.check_zero_value_input(*self.locator.CORR_INCOME_24, name=N.CORR_INCOME_24)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_24, name=N.CORR_INCOME_24)
        self.check_letter_input(*self.locator.CORR_INCOME_24, name=N.CORR_INCOME_24)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_25, name=N.CORR_INCOME_25)
        self.check_zero_value_input(*self.locator.CORR_INCOME_25, name=N.CORR_INCOME_25)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_25, name=N.CORR_INCOME_25)
        self.check_letter_input(*self.locator.CORR_INCOME_25, name=N.CORR_INCOME_25)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_26, name=N.CORR_INCOME_26)
        self.check_zero_value_input(*self.locator.CORR_INCOME_26, name=N.CORR_INCOME_26)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_26, name=N.CORR_INCOME_26)
        self.check_letter_input(*self.locator.CORR_INCOME_26, name=N.CORR_INCOME_26)

        self.max_symbol_15_input(*self.locator.CORR_INCOME_27, name=N.CORR_INCOME_27)
        self.check_zero_value_input(*self.locator.CORR_INCOME_27, name=N.CORR_INCOME_27)
        self.check_special_symbol_input(*self.locator.CORR_INCOME_27, name=N.CORR_INCOME_27)
        self.check_letter_input(*self.locator.CORR_INCOME_27, name=N.CORR_INCOME_27)

        self.find_element(*self.locator.AFTER).click()

    def fourth_page_validation(self):
        self.scroll('300')
        self.max_symbol_15_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_zero_value_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_special_symbol_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_letter_input(*self.locator.STOCK_1, name=N.STOCK_1)

        self.max_symbol_15_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_zero_value_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_special_symbol_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_letter_input(*self.locator.STOCK_2, name=N.STOCK_2)

        #self.max_symbol_15_input(*self.locator.STOCK_3, name=N.STOCK_3)
        #self.check_zero_value_input(*self.locator.STOCK_3, name=N.STOCK_3)
        #self.check_special_symbol_input(*self.locator.STOCK_3, name=N.STOCK_3)
        #self.check_letter_input(*self.locator.STOCK_3, name=N.STOCK_3)

        self.max_symbol_15_input(*self.locator.SERVICE_1, name=N.SERVICE_1)
        self.check_zero_value_input(*self.locator.SERVICE_1, name=N.SERVICE_1)
        self.check_special_symbol_input(*self.locator.SERVICE_1, name=N.SERVICE_1)
        self.check_letter_input(*self.locator.SERVICE_1, name=N.SERVICE_1)

        self.max_symbol_15_input(*self.locator.SERVICE_2, name=N.SERVICE_2)
        self.check_zero_value_input(*self.locator.SERVICE_2, name=N.SERVICE_2)
        self.check_special_symbol_input(*self.locator.SERVICE_2, name=N.SERVICE_2)
        self.check_letter_input(*self.locator.SERVICE_2, name=N.SERVICE_2)

        self.max_symbol_15_input(*self.locator.SERVICE_3, name=N.SERVICE_3)
        self.check_zero_value_input(*self.locator.SERVICE_3, name=N.SERVICE_3)
        self.check_special_symbol_input(*self.locator.SERVICE_3, name=N.SERVICE_3)
        self.check_letter_input(*self.locator.SERVICE_3, name=N.SERVICE_3)

        self.max_symbol_15_input(*self.locator.SERVICE_4, name=N.SERVICE_4)
        self.check_zero_value_input(*self.locator.SERVICE_4, name=N.SERVICE_4)
        self.check_special_symbol_input(*self.locator.SERVICE_4, name=N.SERVICE_4)
        self.check_letter_input(*self.locator.SERVICE_4, name=N.SERVICE_4)

        self.max_symbol_15_input(*self.locator.SERVICE_5, name=N.SERVICE_5)
        self.check_zero_value_input(*self.locator.SERVICE_5, name=N.SERVICE_5)
        self.check_special_symbol_input(*self.locator.SERVICE_5, name=N.SERVICE_5)
        self.check_letter_input(*self.locator.SERVICE_5, name=N.SERVICE_5)

        self.max_symbol_15_input(*self.locator.SERVICE_6, name=N.SERVICE_6)
        self.check_zero_value_input(*self.locator.SERVICE_6, name=N.SERVICE_6)
        self.check_special_symbol_input(*self.locator.SERVICE_6, name=N.SERVICE_6)
        self.check_letter_input(*self.locator.SERVICE_6, name=N.SERVICE_6)

        self.max_symbol_15_input(*self.locator.SERVICE_7, name=N.SERVICE_7)
        self.check_zero_value_input(*self.locator.SERVICE_7, name=N.SERVICE_7)
        self.check_special_symbol_input(*self.locator.SERVICE_7, name=N.SERVICE_7)
        self.check_letter_input(*self.locator.SERVICE_7, name=N.SERVICE_7)

        self.max_symbol_15_input(*self.locator.SERVICE_8, name=N.SERVICE_8)
        self.check_zero_value_input(*self.locator.SERVICE_8, name=N.SERVICE_8)
        self.check_special_symbol_input(*self.locator.SERVICE_8, name=N.SERVICE_8)
        self.check_letter_input(*self.locator.SERVICE_8, name=N.SERVICE_8)
        self.scroll('600')
        self.max_symbol_15_input(*self.locator.STOCK_4, name=N.STOCK_4)
        self.check_zero_value_input(*self.locator.STOCK_4, name=N.STOCK_4)
        self.check_special_symbol_input(*self.locator.STOCK_4, name=N.STOCK_4)
        self.check_letter_input(*self.locator.STOCK_4, name=N.STOCK_4)

        self.max_symbol_15_input(*self.locator.STOCK_5, name=N.STOCK_5)
        self.check_zero_value_input(*self.locator.STOCK_5, name=N.STOCK_5)
        self.check_special_symbol_input(*self.locator.STOCK_5, name=N.STOCK_5)
        self.check_letter_input(*self.locator.STOCK_5, name=N.STOCK_5)

        self.max_symbol_15_input(*self.locator.STOCK_6, name=N.STOCK_6)
        self.check_zero_value_input(*self.locator.STOCK_6, name=N.STOCK_6)
        self.check_special_symbol_input(*self.locator.STOCK_6, name=N.STOCK_6)
        self.check_letter_input(*self.locator.STOCK_6, name=N.STOCK_6)

        self.max_symbol_15_input(*self.locator.STOCK_7, name=N.STOCK_7)
        self.check_zero_value_input(*self.locator.STOCK_7, name=N.STOCK_7)
        self.check_special_symbol_input(*self.locator.STOCK_7, name=N.STOCK_7)
        self.check_letter_input(*self.locator.STOCK_7, name=N.STOCK_7)

        self.max_symbol_15_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_zero_value_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_special_symbol_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_letter_input(*self.locator.STOCK_8, name=N.STOCK_8)

        self.max_symbol_15_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_zero_value_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_special_symbol_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_letter_input(*self.locator.STOCK_9, name=N.STOCK_9)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FIELD_1, name=N.FIELD_1)
        self.check_zero_value_input(*self.locator.FIELD_1, name=N.FIELD_1)
        self.check_special_symbol_input(*self.locator.FIELD_1, name=N.FIELD_1)
        self.check_letter_input(*self.locator.FIELD_1, name=N.FIELD_1)

        self.max_symbol_15_input(*self.locator.FIELD_2, name=N.FIELD_2)
        self.check_zero_value_input(*self.locator.FIELD_2, name=N.FIELD_2)
        self.check_special_symbol_input(*self.locator.FIELD_2, name=N.FIELD_2)
        self.check_letter_input(*self.locator.FIELD_2, name=N.FIELD_2)

        self.max_symbol_15_input(*self.locator.FIELD_3, name=N.FIELD_3)
        self.check_zero_value_input(*self.locator.FIELD_3, name=N.FIELD_3)
        self.check_special_symbol_input(*self.locator.FIELD_3, name=N.FIELD_3)
        self.check_letter_input(*self.locator.FIELD_3, name=N.FIELD_3)

        self.max_symbol_15_input(*self.locator.FIELD_4, name=N.FIELD_4)
        self.check_zero_value_input(*self.locator.FIELD_4, name=N.FIELD_4)
        self.check_special_symbol_input(*self.locator.FIELD_4, name=N.FIELD_4)
        self.check_letter_input(*self.locator.FIELD_4, name=N.FIELD_4)

        self.max_symbol_15_input(*self.locator.FIELD_5, name=N.FIELD_5)
        self.check_zero_value_input(*self.locator.FIELD_5, name=N.FIELD_5)
        self.check_special_symbol_input(*self.locator.FIELD_5, name=N.FIELD_5)
        self.check_letter_input(*self.locator.FIELD_5, name=N.FIELD_5)

        self.max_symbol_15_input(*self.locator.FIELD_6, name=N.FIELD_6)
        self.check_zero_value_input(*self.locator.FIELD_6, name=N.FIELD_6)
        self.check_special_symbol_input(*self.locator.FIELD_6, name=N.FIELD_6)
        self.check_letter_input(*self.locator.FIELD_6, name=N.FIELD_6)

        self.max_symbol_15_input(*self.locator.FIELD_7, name=N.FIELD_7)
        self.check_zero_value_input(*self.locator.FIELD_7, name=N.FIELD_7)
        self.check_special_symbol_input(*self.locator.FIELD_7, name=N.FIELD_7)
        self.check_letter_input(*self.locator.FIELD_7, name=N.FIELD_7)

        self.max_symbol_15_input(*self.locator.FIELD_8, name=N.FIELD_8)
        self.check_zero_value_input(*self.locator.FIELD_8, name=N.FIELD_8)
        self.check_special_symbol_input(*self.locator.FIELD_8, name=N.FIELD_8)
        self.check_letter_input(*self.locator.FIELD_8, name=N.FIELD_8)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.LOANS_1, name=N.LOANS_1)
        self.check_zero_value_input(*self.locator.LOANS_1, name=N.LOANS_1)
        self.check_special_symbol_input(*self.locator.LOANS_1, name=N.LOANS_1)
        self.check_letter_input(*self.locator.LOANS_1, name=N.LOANS_1)

        self.max_symbol_15_input(*self.locator.LOANS_2, name=N.LOANS_2)
        self.check_zero_value_input(*self.locator.LOANS_2, name=N.LOANS_2)
        self.check_special_symbol_input(*self.locator.LOANS_2, name=N.LOANS_2)
        self.check_letter_input(*self.locator.LOANS_2, name=N.LOANS_2)

        self.max_symbol_15_input(*self.locator.LOANS_3, name=N.LOANS_3)
        self.check_zero_value_input(*self.locator.LOANS_3, name=N.LOANS_3)
        self.check_special_symbol_input(*self.locator.LOANS_3, name=N.LOANS_3)
        self.check_letter_input(*self.locator.LOANS_3, name=N.LOANS_3)

        self.max_symbol_15_input(*self.locator.LOANS_4, name=N.LOANS_4)
        self.check_zero_value_input(*self.locator.LOANS_4, name=N.LOANS_4)
        self.check_special_symbol_input(*self.locator.LOANS_4, name=N.LOANS_4)
        self.check_letter_input(*self.locator.LOANS_4, name=N.LOANS_4)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.FIELD_9, name=N.FIELD_9)
        self.check_zero_value_input(*self.locator.FIELD_9, name=N.FIELD_9)
        self.check_special_symbol_input(*self.locator.FIELD_9, name=N.FIELD_9)
        self.check_letter_input(*self.locator.FIELD_9, name=N.FIELD_9)

        self.max_symbol_15_input(*self.locator.FIELD_10, name=N.FIELD_10)
        self.check_zero_value_input(*self.locator.FIELD_10, name=N.FIELD_10)
        self.check_special_symbol_input(*self.locator.FIELD_10, name=N.FIELD_10)
        self.check_letter_input(*self.locator.FIELD_10, name=N.FIELD_10)

        self.max_symbol_15_input(*self.locator.FIELD_11, name=N.FIELD_11)
        self.check_zero_value_input(*self.locator.FIELD_11, name=N.FIELD_11)
        self.check_special_symbol_input(*self.locator.FIELD_11, name=N.FIELD_11)
        self.check_letter_input(*self.locator.FIELD_11, name=N.FIELD_11)

        self.max_symbol_15_input(*self.locator.FIELD_12, name=N.FIELD_12)
        self.check_zero_value_input(*self.locator.FIELD_12, name=N.FIELD_12)
        self.check_special_symbol_input(*self.locator.FIELD_12, name=N.FIELD_12)
        self.check_letter_input(*self.locator.FIELD_12, name=N.FIELD_12)

        self.max_symbol_15_input(*self.locator.FIELD_13, name=N.FIELD_13)
        self.check_zero_value_input(*self.locator.FIELD_13, name=N.FIELD_13)
        self.check_special_symbol_input(*self.locator.FIELD_13, name=N.FIELD_13)
        self.check_letter_input(*self.locator.FIELD_13, name=N.FIELD_13)

        self.max_symbol_15_input(*self.locator.FIELD_14, name=N.FIELD_14)
        self.check_zero_value_input(*self.locator.FIELD_14, name=N.FIELD_14)
        self.check_special_symbol_input(*self.locator.FIELD_14, name=N.FIELD_14)
        self.check_letter_input(*self.locator.FIELD_14, name=N.FIELD_14)

        self.max_symbol_15_input(*self.locator.FIELD_15, name=N.FIELD_15)
        self.check_zero_value_input(*self.locator.FIELD_15, name=N.FIELD_15)
        self.check_special_symbol_input(*self.locator.FIELD_15, name=N.FIELD_15)
        self.check_letter_input(*self.locator.FIELD_15, name=N.FIELD_15)

        self.max_symbol_15_input(*self.locator.FIELD_16, name=N.FIELD_16)
        self.check_zero_value_input(*self.locator.FIELD_16, name=N.FIELD_16)
        self.check_special_symbol_input(*self.locator.FIELD_16, name=N.FIELD_16)
        self.check_letter_input(*self.locator.FIELD_16, name=N.FIELD_16)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.FIELD_17_I, name=N.FIELD_17_I)
        self.check_zero_value_input(*self.locator.FIELD_17_I, name=N.FIELD_17_I)
        self.check_special_symbol_input(*self.locator.FIELD_17_I, name=N.FIELD_17_I)
        self.check_letter_input(*self.locator.FIELD_17_I, name=N.FIELD_17_I)

        self.max_symbol_15_input(*self.locator.FIELD_17_II, name=N.FIELD_17_II)
        self.check_zero_value_input(*self.locator.FIELD_17_II, name=N.FIELD_17_II)
        self.check_special_symbol_input(*self.locator.FIELD_17_II, name=N.FIELD_17_II)
        self.check_letter_input(*self.locator.FIELD_17_II, name=N.FIELD_17_II)

        self.max_symbol_15_input(*self.locator.FIELD_18, name=N.FIELD_18)
        self.check_zero_value_input(*self.locator.FIELD_18, name=N.FIELD_18)
        self.check_special_symbol_input(*self.locator.FIELD_18, name=N.FIELD_18)
        self.check_letter_input(*self.locator.FIELD_18, name=N.FIELD_18)

        self.max_symbol_15_input(*self.locator.FIELD_19, name=N.FIELD_19)
        self.check_zero_value_input(*self.locator.FIELD_19, name=N.FIELD_19)
        self.check_special_symbol_input(*self.locator.FIELD_19, name=N.FIELD_19)
        self.check_letter_input(*self.locator.FIELD_19, name=N.FIELD_19)

        self.scroll('500')

        #self.find_element(*self.locator.FIELD_20_I).send_keys('123456789012345')
        #self.find_element(*self.locator.FIELD_20_II).send_keys('123456789012345')
        #self.find_element(*self.locator.FIELD_20_III).send_keys('123456789012345')
        self.find_element(*self.locator.FIELD_20_IV).send_keys('123456789012345')
        self.find_element(*self.locator.AFTER).click()

    def sixth_page_validation(self):
        self.scroll('1200')
        self.max_symbol_15_input(*self.locator.FIELD_21_I, name=N.FIELD_21_I)
        self.check_zero_value_input(*self.locator.FIELD_21_I, name=N.FIELD_21_I)
        self.check_special_symbol_input(*self.locator.FIELD_21_I, name=N.FIELD_21_I)
        self.check_letter_input(*self.locator.FIELD_21_I, name=N.FIELD_21_I)

        self.max_symbol_15_input(*self.locator.FIELD_21_I_A, name=N.FIELD_21_I_A)
        self.check_zero_value_input(*self.locator.FIELD_21_I_A, name=N.FIELD_21_I_A)
        self.check_special_symbol_input(*self.locator.FIELD_21_I_A, name=N.FIELD_21_I_A)
        self.check_letter_input(*self.locator.FIELD_21_I_A, name=N.FIELD_21_I_A)

        self.max_symbol_15_input(*self.locator.FIELD_21_I_B, name=N.FIELD_21_I_B)
        self.check_zero_value_input(*self.locator.FIELD_21_I_B, name=N.FIELD_21_I_B)
        self.check_special_symbol_input(*self.locator.FIELD_21_I_B, name=N.FIELD_21_I_B)
        self.check_letter_input(*self.locator.FIELD_21_I_B, name=N.FIELD_21_I_B)

        self.max_symbol_15_input(*self.locator.FIELD_21_II, name=N.FIELD_21_II)
        self.check_zero_value_input(*self.locator.FIELD_21_II, name=N.FIELD_21_II)
        self.check_special_symbol_input(*self.locator.FIELD_21_II, name=N.FIELD_21_II)
        self.check_letter_input(*self.locator.FIELD_21_II, name=N.FIELD_21_II)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FIELD_22, name=N.FIELD_22)
        self.check_zero_value_input(*self.locator.FIELD_22, name=N.FIELD_22)
        self.check_special_symbol_input(*self.locator.FIELD_22, name=N.FIELD_22)
        self.check_letter_input(*self.locator.FIELD_22, name=N.FIELD_22)

        self.max_symbol_15_input(*self.locator.FIELD_23_III, name=N.FIELD_23_III)
        self.check_zero_value_input(*self.locator.FIELD_23_III, name=N.FIELD_23_III)
        self.check_special_symbol_input(*self.locator.FIELD_23_III, name=N.FIELD_23_III)
        self.check_letter_input(*self.locator.FIELD_23_III, name=N.FIELD_23_III)

        self.max_symbol_15_input(*self.locator.FIELD_23_IV, name=N.FIELD_23_IV)
        self.check_zero_value_input(*self.locator.FIELD_23_IV, name=N.FIELD_23_IV)
        self.check_special_symbol_input(*self.locator.FIELD_23_IV, name=N.FIELD_23_IV)
        self.check_letter_input(*self.locator.FIELD_23_IV, name=N.FIELD_23_IV)

        self.max_symbol_15_input(*self.locator.FIELD_23_V, name=N.FIELD_23_V)
        self.check_zero_value_input(*self.locator.FIELD_23_V, name=N.FIELD_23_V)
        self.check_special_symbol_input(*self.locator.FIELD_23_V, name=N.FIELD_23_V)
        self.check_letter_input(*self.locator.FIELD_23_V, name=N.FIELD_23_V)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FIELD_23_VI, name=N.FIELD_23_VI)
        self.check_zero_value_input(*self.locator.FIELD_23_VI, name=N.FIELD_23_VI)
        self.check_special_symbol_input(*self.locator.FIELD_23_VI, name=N.FIELD_23_VI)
        self.check_letter_input(*self.locator.FIELD_23_VI, name=N.FIELD_23_VI)

        self.max_symbol_15_input(*self.locator.FIELD_24, name=N.FIELD_24)
        self.check_zero_value_input(*self.locator.FIELD_24, name=N.FIELD_24)
        self.check_special_symbol_input(*self.locator.FIELD_24, name=N.FIELD_24)
        self.check_letter_input(*self.locator.FIELD_24, name=N.FIELD_24)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FIELD_25_B, name=N.FIELD_25_B)
        self.check_zero_value_input(*self.locator.FIELD_25_B, name=N.FIELD_25_B)
        self.check_special_symbol_input(*self.locator.FIELD_25_B, name=N.FIELD_25_B)
        self.check_letter_input(*self.locator.FIELD_25_B, name=N.FIELD_25_B)

        self.max_symbol_15_input(*self.locator.FIELD_25_IV, name=N.FIELD_25_IV)
        self.check_zero_value_input(*self.locator.FIELD_25_IV, name=N.FIELD_25_IV)
        self.check_special_symbol_input(*self.locator.FIELD_25_IV, name=N.FIELD_25_IV)
        self.check_letter_input(*self.locator.FIELD_25_IV, name=N.FIELD_25_IV)

        self.find_element(*self.locator.AFTER).click()

    def validation_app_1(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()

        self.max_symbol_12_input(*self.locator.B_APP_1, name=N.B_APP_1)
        self.check_zero_value_input(*self.locator.B_APP_1, name=N.B_APP_1)
        self.check_special_symbol_input(*self.locator.B_APP_1, name=N.B_APP_1)
        self.check_letter_input(*self.locator.B_APP_1, name=N.B_APP_1)

        #self.max_symbol_15_input(*self.locator.F_APP_1, name=N.F_APP_1)
        #self.check_zero_value_input(*self.locator.F_APP_1, name=N.F_APP_1)
        #self.check_special_symbol_input(*self.locator.F_APP_1, name=N.F_APP_1)
        #self.check_letter_input(*self.locator.F_APP_1, name=N.F_APP_1)

        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_2(self):
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.GROUP_1, name=N.GROUP_1)
        self.check_zero_value_input(*self.locator.GROUP_1, name=N.GROUP_1)
        self.check_special_symbol_input(*self.locator.GROUP_1, name=N.GROUP_1)
        self.check_letter_input(*self.locator.GROUP_1, name=N.GROUP_1)

        self.max_symbol_15_input(*self.locator.GROUP_2, name=N.GROUP_2)
        self.check_zero_value_input(*self.locator.GROUP_2, name=N.GROUP_2)
        self.check_special_symbol_input(*self.locator.GROUP_2, name=N.GROUP_2)
        self.check_letter_input(*self.locator.GROUP_2, name=N.GROUP_2)

        self.max_symbol_15_input(*self.locator.GROUP_3, name=N.GROUP_3)
        self.check_zero_value_input(*self.locator.GROUP_3, name=N.GROUP_3)
        self.check_special_symbol_input(*self.locator.GROUP_3, name=N.GROUP_3)
        self.check_letter_input(*self.locator.GROUP_3, name=N.GROUP_3)

        self.max_symbol_15_input(*self.locator.GROUP_4, name=N.GROUP_4)
        self.check_zero_value_input(*self.locator.GROUP_4, name=N.GROUP_4)
        self.check_special_symbol_input(*self.locator.GROUP_4, name=N.GROUP_4)
        self.check_letter_input(*self.locator.GROUP_4, name=N.GROUP_4)

        self.max_symbol_15_input(*self.locator.GROUP_5, name=N.GROUP_5)
        self.check_zero_value_input(*self.locator.GROUP_5, name=N.GROUP_5)
        self.check_special_symbol_input(*self.locator.GROUP_5, name=N.GROUP_5)
        self.check_letter_input(*self.locator.GROUP_5, name=N.GROUP_5)

        self.max_symbol_15_input(*self.locator.GROUP_6, name=N.GROUP_6)
        self.check_zero_value_input(*self.locator.GROUP_6, name=N.GROUP_6)
        self.check_special_symbol_input(*self.locator.GROUP_6, name=N.GROUP_6)
        self.check_letter_input(*self.locator.GROUP_6, name=N.GROUP_6)

        self.max_symbol_15_input(*self.locator.GROUP_7, name=N.GROUP_7)
        self.check_zero_value_input(*self.locator.GROUP_7, name=N.GROUP_7)
        self.check_special_symbol_input(*self.locator.GROUP_7, name=N.GROUP_7)
        self.check_letter_input(*self.locator.GROUP_7, name=N.GROUP_7)

        self.max_symbol_15_input(*self.locator.GROUP_8, name=N.GROUP_8)
        self.check_zero_value_input(*self.locator.GROUP_8, name=N.GROUP_8)
        self.check_special_symbol_input(*self.locator.GROUP_8, name=N.GROUP_8)
        self.check_letter_input(*self.locator.GROUP_8, name=N.GROUP_8)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.GROUP_9, name=N.GROUP_9)
        self.check_zero_value_input(*self.locator.GROUP_9, name=N.GROUP_9)
        self.check_special_symbol_input(*self.locator.GROUP_9, name=N.GROUP_9)
        self.check_letter_input(*self.locator.GROUP_9, name=N.GROUP_9)

        self.max_symbol_15_input(*self.locator.GROUP_10, name=N.GROUP_10)
        self.check_zero_value_input(*self.locator.GROUP_10, name=N.GROUP_10)
        self.check_special_symbol_input(*self.locator.GROUP_10, name=N.GROUP_10)
        self.check_letter_input(*self.locator.GROUP_10, name=N.GROUP_10)

        self.max_symbol_15_input(*self.locator.GROUP_11, name=N.GROUP_11)
        self.check_zero_value_input(*self.locator.GROUP_11, name=N.GROUP_11)
        self.check_special_symbol_input(*self.locator.GROUP_11, name=N.GROUP_11)
        self.check_letter_input(*self.locator.GROUP_11, name=N.GROUP_11)

        self.max_symbol_15_input(*self.locator.GROUP_12, name=N.GROUP_12)
        self.check_zero_value_input(*self.locator.GROUP_12, name=N.GROUP_12)
        self.check_special_symbol_input(*self.locator.GROUP_12, name=N.GROUP_12)
        self.check_letter_input(*self.locator.GROUP_12, name=N.GROUP_12)

        self.max_symbol_15_input(*self.locator.GROUP_13, name=N.GROUP_13)
        self.check_zero_value_input(*self.locator.GROUP_13, name=N.GROUP_13)
        self.check_special_symbol_input(*self.locator.GROUP_13, name=N.GROUP_13)
        self.check_letter_input(*self.locator.GROUP_13, name=N.GROUP_13)

        self.max_symbol_15_input(*self.locator.GROUP_14, name=N.GROUP_14)
        self.check_zero_value_input(*self.locator.GROUP_14, name=N.GROUP_14)
        self.check_special_symbol_input(*self.locator.GROUP_14, name=N.GROUP_14)
        self.check_letter_input(*self.locator.GROUP_14, name=N.GROUP_14)

        self.max_symbol_15_input(*self.locator.GROUP_16, name=N.GROUP_16)
        self.check_zero_value_input(*self.locator.GROUP_16, name=N.GROUP_16)
        self.check_special_symbol_input(*self.locator.GROUP_16, name=N.GROUP_16)
        self.check_letter_input(*self.locator.GROUP_16, name=N.GROUP_16)
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.GROUP_17, name=N.GROUP_17)
        self.check_zero_value_input(*self.locator.GROUP_17, name=N.GROUP_17)
        self.check_special_symbol_input(*self.locator.GROUP_17, name=N.GROUP_17)
        self.check_letter_input(*self.locator.GROUP_17, name=N.GROUP_17)

        self.max_symbol_15_input(*self.locator.GROUP_18, name=N.GROUP_18)
        self.check_zero_value_input(*self.locator.GROUP_18, name=N.GROUP_18)
        self.check_special_symbol_input(*self.locator.GROUP_18, name=N.GROUP_18)
        self.check_letter_input(*self.locator.GROUP_18, name=N.GROUP_18)

        self.max_symbol_15_input(*self.locator.GROUP_19, name=N.GROUP_19)
        self.check_zero_value_input(*self.locator.GROUP_19, name=N.GROUP_19)
        self.check_special_symbol_input(*self.locator.GROUP_19, name=N.GROUP_19)
        self.check_letter_input(*self.locator.GROUP_19, name=N.GROUP_19)

        self.max_symbol_15_input(*self.locator.GROUP_20, name=N.GROUP_20)
        self.check_zero_value_input(*self.locator.GROUP_20, name=N.GROUP_20)
        self.check_special_symbol_input(*self.locator.GROUP_20, name=N.GROUP_20)
        self.check_letter_input(*self.locator.GROUP_20, name=N.GROUP_20)

        self.max_symbol_15_input(*self.locator.GROUP_21, name=N.GROUP_21)
        self.check_zero_value_input(*self.locator.GROUP_21, name=N.GROUP_21)
        self.check_special_symbol_input(*self.locator.GROUP_21, name=N.GROUP_21)
        self.check_letter_input(*self.locator.GROUP_21, name=N.GROUP_21)

        self.max_symbol_15_input(*self.locator.GROUP_22, name=N.GROUP_22)
        self.check_zero_value_input(*self.locator.GROUP_22, name=N.GROUP_22)
        self.check_special_symbol_input(*self.locator.GROUP_22, name=N.GROUP_22)
        self.check_letter_input(*self.locator.GROUP_22, name=N.GROUP_22)

        self.max_symbol_15_input(*self.locator.GROUP_23, name=N.GROUP_23)
        self.check_zero_value_input(*self.locator.GROUP_23, name=N.GROUP_23)
        self.check_special_symbol_input(*self.locator.GROUP_23, name=N.GROUP_23)
        self.check_letter_input(*self.locator.GROUP_23, name=N.GROUP_23)

        self.max_symbol_15_input(*self.locator.GROUP_24, name=N.GROUP_24)
        self.check_zero_value_input(*self.locator.GROUP_24, name=N.GROUP_24)
        self.check_special_symbol_input(*self.locator.GROUP_24, name=N.GROUP_24)
        self.check_letter_input(*self.locator.GROUP_24, name=N.GROUP_24)
        self.scroll('700')
        self.max_symbol_15_input(*self.locator.GROUP_25, name=N.GROUP_25)
        self.check_zero_value_input(*self.locator.GROUP_25, name=N.GROUP_25)
        self.check_special_symbol_input(*self.locator.GROUP_25, name=N.GROUP_25)
        self.check_letter_input(*self.locator.GROUP_25, name=N.GROUP_25)

        self.max_symbol_15_input(*self.locator.GROUP_26, name=N.GROUP_26)
        self.check_zero_value_input(*self.locator.GROUP_26, name=N.GROUP_26)
        self.check_special_symbol_input(*self.locator.GROUP_26, name=N.GROUP_26)
        self.check_letter_input(*self.locator.GROUP_26, name=N.GROUP_26)

        self.max_symbol_15_input(*self.locator.GROUP_27, name=N.GROUP_27)
        self.check_zero_value_input(*self.locator.GROUP_27, name=N.GROUP_27)
        self.check_special_symbol_input(*self.locator.GROUP_27, name=N.GROUP_27)
        self.check_letter_input(*self.locator.GROUP_27, name=N.GROUP_27)

        self.max_symbol_15_input(*self.locator.GROUP_28, name=N.GROUP_28)
        self.check_zero_value_input(*self.locator.GROUP_28, name=N.GROUP_28)
        self.check_special_symbol_input(*self.locator.GROUP_28, name=N.GROUP_28)
        self.check_letter_input(*self.locator.GROUP_28, name=N.GROUP_28)

        self.max_symbol_15_input(*self.locator.GROUP_29, name=N.GROUP_29)
        self.check_zero_value_input(*self.locator.GROUP_29, name=N.GROUP_29)
        self.check_special_symbol_input(*self.locator.GROUP_29, name=N.GROUP_29)
        self.check_letter_input(*self.locator.GROUP_29, name=N.GROUP_29)

        self.max_symbol_15_input(*self.locator.GROUP_30, name=N.GROUP_30)
        self.check_zero_value_input(*self.locator.GROUP_30, name=N.GROUP_30)
        self.check_special_symbol_input(*self.locator.GROUP_30, name=N.GROUP_30)
        self.check_letter_input(*self.locator.GROUP_30, name=N.GROUP_30)

        self.max_symbol_15_input(*self.locator.GROUP_31, name=N.GROUP_31)
        self.check_zero_value_input(*self.locator.GROUP_31, name=N.GROUP_31)
        self.check_special_symbol_input(*self.locator.GROUP_31, name=N.GROUP_31)
        self.check_letter_input(*self.locator.GROUP_31, name=N.GROUP_31)

        self.max_symbol_15_input(*self.locator.GROUP_32, name=N.GROUP_32)
        self.check_zero_value_input(*self.locator.GROUP_32, name=N.GROUP_32)
        self.check_special_symbol_input(*self.locator.GROUP_32, name=N.GROUP_32)
        self.check_letter_input(*self.locator.GROUP_32, name=N.GROUP_32)
        self.scroll('600')
        self.max_symbol_15_input(*self.locator.GROUP_33, name=N.GROUP_33)
        self.check_zero_value_input(*self.locator.GROUP_33, name=N.GROUP_33)
        self.check_special_symbol_input(*self.locator.GROUP_33, name=N.GROUP_33)
        self.check_letter_input(*self.locator.GROUP_33, name=N.GROUP_33)

        self.max_symbol_15_input(*self.locator.GROUP_34, name=N.GROUP_34)
        self.check_zero_value_input(*self.locator.GROUP_34, name=N.GROUP_34)
        self.check_special_symbol_input(*self.locator.GROUP_34, name=N.GROUP_34)
        self.check_letter_input(*self.locator.GROUP_34, name=N.GROUP_34)

        self.max_symbol_15_input(*self.locator.GROUP_35, name=N.GROUP_35)
        self.check_zero_value_input(*self.locator.GROUP_35, name=N.GROUP_35)
        self.check_special_symbol_input(*self.locator.GROUP_35, name=N.GROUP_35)
        self.check_letter_input(*self.locator.GROUP_35, name=N.GROUP_35)

        self.max_symbol_15_input(*self.locator.GROUP_36, name=N.GROUP_36)
        self.check_zero_value_input(*self.locator.GROUP_36, name=N.GROUP_36)
        self.check_special_symbol_input(*self.locator.GROUP_36, name=N.GROUP_36)
        self.check_letter_input(*self.locator.GROUP_36, name=N.GROUP_36)

        self.max_symbol_15_input(*self.locator.GROUP_37, name=N.GROUP_37)
        self.check_zero_value_input(*self.locator.GROUP_37, name=N.GROUP_37)
        self.check_special_symbol_input(*self.locator.GROUP_37, name=N.GROUP_37)
        self.check_letter_input(*self.locator.GROUP_37, name=N.GROUP_37)

        self.max_symbol_15_input(*self.locator.GROUP_38, name=N.GROUP_38)
        self.check_zero_value_input(*self.locator.GROUP_38, name=N.GROUP_38)
        self.check_special_symbol_input(*self.locator.GROUP_38, name=N.GROUP_38)
        self.check_letter_input(*self.locator.GROUP_38, name=N.GROUP_38)

        self.max_symbol_15_input(*self.locator.GROUP_39, name=N.GROUP_39)
        self.check_zero_value_input(*self.locator.GROUP_39, name=N.GROUP_39)
        self.check_special_symbol_input(*self.locator.GROUP_39, name=N.GROUP_39)
        self.check_letter_input(*self.locator.GROUP_39, name=N.GROUP_39)

        self.max_symbol_15_input(*self.locator.GROUP_40, name=N.GROUP_40)
        self.check_zero_value_input(*self.locator.GROUP_40, name=N.GROUP_40)
        self.check_special_symbol_input(*self.locator.GROUP_40, name=N.GROUP_40)
        self.check_letter_input(*self.locator.GROUP_40, name=N.GROUP_40)
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def validation_app_3(self):
        self.scroll('122500')
        self.find_element(*self.locator.AFTER).click()

    def validation_app_4(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()

        self.max_symbol_15_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_zero_value_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_special_symbol_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.check_letter_input(*self.locator.E_APP_4, name=N.E_APP_4)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_5(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()

        self.max_symbol_15_input(*self.locator.E_APP_5, name=N.E_APP_5)
        self.check_zero_value_input(*self.locator.E_APP_5, name=N.E_APP_5)
        self.check_special_symbol_input(*self.locator.E_APP_5, name=N.E_APP_5)
        self.check_letter_input(*self.locator.E_APP_5, name=N.E_APP_5)

        self.max_symbol_15_input(*self.locator.F_APP_5, name=N.F_APP_5)
        self.check_zero_value_input(*self.locator.F_APP_5, name=N.F_APP_5)
        self.check_special_symbol_input(*self.locator.F_APP_5, name=N.F_APP_5)
        self.check_letter_input(*self.locator.F_APP_5, name=N.F_APP_5)

        element = self.browser.find_element_by_xpath('//*[@name="K"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

        self.max_symbol_15_input(*self.locator.G_APP_5, name=N.G_APP_5)
        self.check_zero_value_input(*self.locator.G_APP_5, name=N.G_APP_5)
        self.check_special_symbol_input(*self.locator.G_APP_5, name=N.G_APP_5)
        self.check_letter_input(*self.locator.G_APP_5, name=N.G_APP_5)

        self.max_symbol_15_input(*self.locator.H_APP_5, name=N.H_APP_5)
        self.check_zero_value_input(*self.locator.H_APP_5, name=N.H_APP_5)
        self.check_special_symbol_input(*self.locator.H_APP_5, name=N.H_APP_5)
        self.check_letter_input(*self.locator.H_APP_5, name=N.H_APP_5)

        self.max_symbol_15_input(*self.locator.I_APP_5, name=N.I_APP_5)
        self.check_zero_value_input(*self.locator.I_APP_5, name=N.I_APP_5)
        self.check_special_symbol_input(*self.locator.I_APP_5, name=N.I_APP_5)
        self.check_letter_input(*self.locator.I_APP_5, name=N.I_APP_5)

        self.max_symbol_15_input(*self.locator.J_APP_5, name=N.J_APP_5)
        self.check_zero_value_input(*self.locator.J_APP_5, name=N.J_APP_5)
        self.check_special_symbol_input(*self.locator.J_APP_5, name=N.J_APP_5)
        self.check_letter_input(*self.locator.J_APP_5, name=N.J_APP_5)

        self.max_symbol_15_input(*self.locator.K_APP_5, name=N.K_APP_5)
        self.check_zero_value_input(*self.locator.K_APP_5, name=N.K_APP_5)
        self.check_special_symbol_input(*self.locator.K_APP_5, name=N.K_APP_5)
        self.check_letter_input(*self.locator.K_APP_5, name=N.K_APP_5)

        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_6(self):
        sleep(1)
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.YEAR_EXPENSE, name=N.YEAR_EXPENSE)
        self.check_zero_value_input(*self.locator.YEAR_EXPENSE, name=N.YEAR_EXPENSE)
        self.check_special_symbol_input(*self.locator.YEAR_EXPENSE, name=N.YEAR_EXPENSE)
        self.check_letter_input(*self.locator.YEAR_EXPENSE, name=N.YEAR_EXPENSE)

        self.max_symbol_15_input(*self.locator.STR_1, name=N.STR_1)
        self.check_zero_value_input(*self.locator.STR_1, name=N.STR_1)
        self.check_special_symbol_input(*self.locator.STR_1, name=N.STR_1)
        self.check_letter_input(*self.locator.STR_1, name=N.STR_1)

        self.max_symbol_15_input(*self.locator.STR_2, name=N.STR_2)
        self.check_zero_value_input(*self.locator.STR_2, name=N.STR_2)
        self.check_special_symbol_input(*self.locator.STR_2, name=N.STR_2)
        self.check_letter_input(*self.locator.STR_2, name=N.STR_2)

        self.max_symbol_15_input(*self.locator.STR_3_I, name=N.STR_3_I)
        self.check_zero_value_input(*self.locator.STR_3_I, name=N.STR_3_I)
        self.check_special_symbol_input(*self.locator.STR_3_I, name=N.STR_3_I)
        self.check_letter_input(*self.locator.STR_3_I, name=N.STR_3_I)

        self.max_symbol_15_input(*self.locator.STR_3_II, name=N.STR_3_II)
        self.check_zero_value_input(*self.locator.STR_3_II, name=N.STR_3_II)
        self.check_special_symbol_input(*self.locator.STR_3_II, name=N.STR_3_II)
        self.check_letter_input(*self.locator.STR_3_II, name=N.STR_3_II)

        sleep(0.2)
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.STR_4, name=N.STR_4)
        self.check_zero_value_input(*self.locator.STR_4, name=N.STR_4)
        self.check_special_symbol_input(*self.locator.STR_4, name=N.STR_4)
        self.check_letter_input(*self.locator.STR_4, name=N.STR_4)

        self.max_symbol_15_input(*self.locator.STR_5, name=N.STR_5)
        self.check_zero_value_input(*self.locator.STR_5, name=N.STR_5)
        self.check_special_symbol_input(*self.locator.STR_5, name=N.STR_5)
        self.check_letter_input(*self.locator.STR_5, name=N.STR_5)

        self.max_symbol_15_input(*self.locator.STR_6, name=N.STR_6)
        self.check_zero_value_input(*self.locator.STR_6, name=N.STR_6)
        self.check_special_symbol_input(*self.locator.STR_6, name=N.STR_6)
        self.check_letter_input(*self.locator.STR_6, name=N.STR_6)

        self.max_symbol_15_input(*self.locator.STR_7, name=N.STR_7)
        self.check_zero_value_input(*self.locator.STR_7, name=N.STR_7)
        self.check_special_symbol_input(*self.locator.STR_7, name=N.STR_7)
        self.check_letter_input(*self.locator.STR_7, name=N.STR_7)
        sleep(0.2)
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.STR_8, name=N.STR_8)
        self.check_zero_value_input(*self.locator.STR_8, name=N.STR_8)
        self.check_special_symbol_input(*self.locator.STR_8, name=N.STR_8)
        self.check_letter_input(*self.locator.STR_8, name=N.STR_8)

        self.max_symbol_15_input(*self.locator.STR_9_I, name=N.STR_9_I)
        self.check_zero_value_input(*self.locator.STR_9_I, name=N.STR_9_I)
        self.check_special_symbol_input(*self.locator.STR_9_I, name=N.STR_9_I)
        self.check_letter_input(*self.locator.STR_9_I, name=N.STR_9_I)

        self.max_symbol_15_input(*self.locator.STR_9_II, name=N.STR_9_II)
        self.check_zero_value_input(*self.locator.STR_9_II, name=N.STR_9_II)
        self.check_special_symbol_input(*self.locator.STR_9_II, name=N.STR_9_II)
        self.check_letter_input(*self.locator.STR_9_II, name=N.STR_9_II)

        self.max_symbol_15_input(*self.locator.STR_10, name=N.STR_10)
        self.check_zero_value_input(*self.locator.STR_10, name=N.STR_10)
        self.check_special_symbol_input(*self.locator.STR_10, name=N.STR_10)
        self.check_letter_input(*self.locator.STR_10, name=N.STR_10)

        self.max_symbol_15_input(*self.locator.STR_11, name=N.STR_11)
        self.check_zero_value_input(*self.locator.STR_11, name=N.STR_11)
        self.check_special_symbol_input(*self.locator.STR_11, name=N.STR_11)
        self.check_letter_input(*self.locator.STR_11, name=N.STR_11)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.STR_12, name=N.STR_12)
        self.check_zero_value_input(*self.locator.STR_12, name=N.STR_12)
        self.check_special_symbol_input(*self.locator.STR_12, name=N.STR_12)
        self.check_letter_input(*self.locator.STR_12, name=N.STR_12)

        self.max_symbol_15_input(*self.locator.STR_13, name=N.STR_13)
        self.check_zero_value_input(*self.locator.STR_13, name=N.STR_13)
        self.check_special_symbol_input(*self.locator.STR_13, name=N.STR_13)
        self.check_letter_input(*self.locator.STR_13, name=N.STR_13)

        self.max_symbol_15_input(*self.locator.STR_14, name=N.STR_14)
        self.check_zero_value_input(*self.locator.STR_14, name=N.STR_14)
        self.check_special_symbol_input(*self.locator.STR_14, name=N.STR_14)
        self.check_letter_input(*self.locator.STR_14, name=N.STR_14)

        self.find_element(*self.locator.STR_15).send_keys('123')
        assert '12' in self.browser.page_source

        sleep(0.3)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.STR_16_I, name=N.STR_16_I)
        self.check_zero_value_input(*self.locator.STR_16_I, name=N.STR_16_I)
        self.check_special_symbol_input(*self.locator.STR_16_I, name=N.STR_16_I)
        self.check_letter_input(*self.locator.STR_16_I, name=N.STR_16_I)

        self.max_symbol_15_input(*self.locator.STR_16_II, name=N.STR_16_II)
        self.check_zero_value_input(*self.locator.STR_16_II, name=N.STR_16_II)
        self.check_special_symbol_input(*self.locator.STR_16_II, name=N.STR_16_II)
        self.check_letter_input(*self.locator.STR_16_II, name=N.STR_16_II)

        self.max_symbol_15_input(*self.locator.STR_16_III, name=N.STR_16_III)
        self.check_zero_value_input(*self.locator.STR_16_III, name=N.STR_16_III)
        self.check_special_symbol_input(*self.locator.STR_16_III, name=N.STR_16_III)
        self.check_letter_input(*self.locator.STR_16_III, name=N.STR_16_III)

        self.max_symbol_15_input(*self.locator.STR_16_IV, name=N.STR_16_IV)
        self.check_zero_value_input(*self.locator.STR_16_IV, name=N.STR_16_IV)
        self.check_special_symbol_input(*self.locator.STR_16_IV, name=N.STR_16_IV)
        self.check_letter_input(*self.locator.STR_16_IV, name=N.STR_16_IV)

        self.max_symbol_15_input(*self.locator.STR_16_V, name=N.STR_16_V)
        self.check_zero_value_input(*self.locator.STR_16_V, name=N.STR_16_V)
        self.check_special_symbol_input(*self.locator.STR_16_V, name=N.STR_16_V)
        self.check_letter_input(*self.locator.STR_16_V, name=N.STR_16_V)

        self.max_symbol_15_input(*self.locator.STR_16_VI, name=N.STR_16_VI)
        self.check_zero_value_input(*self.locator.STR_16_VI, name=N.STR_16_VI)
        self.check_special_symbol_input(*self.locator.STR_16_VI, name=N.STR_16_VI)
        self.check_letter_input(*self.locator.STR_16_VI, name=N.STR_16_VI)

        self.max_symbol_15_input(*self.locator.STR_16_VII, name=N.STR_16_VII)
        self.check_zero_value_input(*self.locator.STR_16_VII, name=N.STR_16_VII)
        self.check_special_symbol_input(*self.locator.STR_16_VII, name=N.STR_16_VII)
        self.check_letter_input(*self.locator.STR_16_VII, name=N.STR_16_VII)

        sleep(0.3)
        self.scroll('500')
        self.find_element(*self.locator.PERCENT).send_keys('123')
        assert '12' in self.browser.page_source

        self.max_symbol_15_input(*self.locator.PERCENT_2, name=N.PERCENT_2)
        self.check_zero_value_input(*self.locator.PERCENT_2, name=N.PERCENT_2)
        self.check_special_symbol_input(*self.locator.PERCENT_2, name=N.PERCENT_2)
        self.check_letter_input(*self.locator.PERCENT_2, name=N.PERCENT_2)
        self.scroll('500')
        sleep(0.3)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_7(self):
        self.hover(*self.locator.CONTROL_TEXT)
        sleep(1)
        self.find_element(*self.locator.CHAPTER_1).click()
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.START_1, name=N.START_1)
        self.check_zero_value_input(*self.locator.START_1, name=N.START_1)
        self.check_special_symbol_input(*self.locator.START_1, name=N.START_1)
        self.check_letter_input(*self.locator.START_1, name=N.START_1)

        self.max_symbol_15_input(*self.locator.END_1, name=N.END_1)
        self.check_zero_value_input(*self.locator.END_1, name=N.END_1)
        self.check_special_symbol_input(*self.locator.END_1, name=N.END_1)
        self.check_letter_input(*self.locator.END_1, name=N.END_1)

        self.max_symbol_15_input(*self.locator.START_2, name=N.START_2)
        self.check_zero_value_input(*self.locator.START_2, name=N.START_2)
        self.check_special_symbol_input(*self.locator.START_2, name=N.START_2)
        self.check_letter_input(*self.locator.START_2, name=N.START_2)

        self.max_symbol_15_input(*self.locator.END_2, name=N.END_2)
        self.check_zero_value_input(*self.locator.END_2, name=N.END_2)
        self.check_special_symbol_input(*self.locator.END_2, name=N.END_2)
        self.check_letter_input(*self.locator.END_2, name=N.END_2)

        self.max_symbol_15_input(*self.locator.START_3, name=N.START_3)
        self.check_zero_value_input(*self.locator.START_3, name=N.START_3)
        self.check_special_symbol_input(*self.locator.START_3, name=N.START_3)
        self.check_letter_input(*self.locator.START_3, name=N.START_3)

        self.max_symbol_15_input(*self.locator.END_3, name=N.END_3)
        self.check_zero_value_input(*self.locator.END_3, name=N.END_3)
        self.check_special_symbol_input(*self.locator.END_3, name=N.END_3)
        self.check_letter_input(*self.locator.END_3, name=N.END_3)

        self.max_symbol_15_input(*self.locator.START_4, name=N.START_4)
        self.check_zero_value_input(*self.locator.START_4, name=N.START_4)
        self.check_special_symbol_input(*self.locator.START_4, name=N.START_4)
        self.check_letter_input(*self.locator.START_4, name=N.START_4)

        self.max_symbol_15_input(*self.locator.END_4, name=N.END_4)
        self.check_zero_value_input(*self.locator.END_4, name=N.END_4)
        self.check_special_symbol_input(*self.locator.END_4, name=N.END_4)
        self.check_letter_input(*self.locator.END_4, name=N.END_4)

        self.max_symbol_15_input(*self.locator.START_5, name=N.START_5)
        self.check_zero_value_input(*self.locator.START_5, name=N.START_5)
        self.check_special_symbol_input(*self.locator.START_5, name=N.START_5)
        self.check_letter_input(*self.locator.START_5, name=N.START_5)

        self.max_symbol_15_input(*self.locator.END_5, name=N.END_5)
        self.check_zero_value_input(*self.locator.END_5, name=N.END_5)
        self.check_special_symbol_input(*self.locator.END_5, name=N.END_5)
        self.check_letter_input(*self.locator.END_5, name=N.END_5)

        self.max_symbol_15_input(*self.locator.START_6, name=N.START_6)
        self.check_zero_value_input(*self.locator.START_6, name=N.START_6)
        self.check_special_symbol_input(*self.locator.START_6, name=N.START_6)
        self.check_letter_input(*self.locator.START_6, name=N.START_6)

        self.max_symbol_15_input(*self.locator.END_6, name=N.END_6)
        self.check_zero_value_input(*self.locator.END_6, name=N.END_6)
        self.check_special_symbol_input(*self.locator.END_6, name=N.END_6)
        self.check_letter_input(*self.locator.END_6, name=N.END_6)

        sleep(0.2)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.START_7, name=N.START_7)
        self.check_zero_value_input(*self.locator.START_7, name=N.START_7)
        self.check_special_symbol_input(*self.locator.START_7, name=N.START_7)
        self.check_letter_input(*self.locator.START_7, name=N.START_7)

        self.max_symbol_15_input(*self.locator.END_7, name=N.END_7)
        self.check_zero_value_input(*self.locator.END_7, name=N.END_7)
        self.check_special_symbol_input(*self.locator.END_7, name=N.END_7)
        self.check_letter_input(*self.locator.END_7, name=N.END_7)

        self.max_symbol_15_input(*self.locator.START_8, name=N.START_8)
        self.check_zero_value_input(*self.locator.START_8, name=N.START_8)
        self.check_special_symbol_input(*self.locator.START_8, name=N.START_8)
        self.check_letter_input(*self.locator.START_8, name=N.START_8)

        self.max_symbol_15_input(*self.locator.END_8, name=N.END_8)
        self.check_zero_value_input(*self.locator.END_8, name=N.END_8)
        self.check_special_symbol_input(*self.locator.END_8, name=N.END_8)
        self.check_letter_input(*self.locator.END_8, name=N.END_8)

        self.max_symbol_15_input(*self.locator.START_9, name=N.START_9)
        self.check_zero_value_input(*self.locator.START_9, name=N.START_9)
        self.check_special_symbol_input(*self.locator.START_3, name=N.START_9)
        self.check_letter_input(*self.locator.START_9, name=N.START_9)

        self.max_symbol_15_input(*self.locator.END_9, name=N.END_9)
        self.check_zero_value_input(*self.locator.END_9, name=N.END_9)
        self.check_special_symbol_input(*self.locator.END_9, name=N.END_9)
        self.check_letter_input(*self.locator.END_9, name=N.END_9)

        self.max_symbol_15_input(*self.locator.START_10, name=N.START_10)
        self.check_zero_value_input(*self.locator.START_10, name=N.START_10)
        self.check_special_symbol_input(*self.locator.START_10, name=N.START_10)
        self.check_letter_input(*self.locator.START_10, name=N.START_10)

        self.max_symbol_15_input(*self.locator.END_10, name=N.END_10)
        self.check_zero_value_input(*self.locator.END_10, name=N.END_10)
        self.check_special_symbol_input(*self.locator.END_10, name=N.END_10)
        self.check_letter_input(*self.locator.END_10, name=N.END_10)

        self.max_symbol_15_input(*self.locator.START_11, name=N.START_11)
        self.check_zero_value_input(*self.locator.START_11, name=N.START_11)
        self.check_special_symbol_input(*self.locator.START_11, name=N.START_11)
        self.check_letter_input(*self.locator.START_11, name=N.START_11)

        self.max_symbol_15_input(*self.locator.END_11, name=N.END_11)
        self.check_zero_value_input(*self.locator.END_11, name=N.END_11)
        self.check_special_symbol_input(*self.locator.END_11, name=N.END_11)
        self.check_letter_input(*self.locator.END_11, name=N.END_11)

        self.max_symbol_15_input(*self.locator.START_12, name=N.START_12)
        self.check_zero_value_input(*self.locator.START_12, name=N.START_12)
        self.check_special_symbol_input(*self.locator.START_12, name=N.START_12)
        self.check_letter_input(*self.locator.START_12, name=N.START_12)

        self.max_symbol_15_input(*self.locator.END_12, name=N.END_12)
        self.check_zero_value_input(*self.locator.END_12, name=N.END_12)
        self.check_special_symbol_input(*self.locator.END_12, name=N.END_12)
        self.check_letter_input(*self.locator.END_12, name=N.END_12)
        sleep(0.2)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.START_13, name=N.START_13)
        self.check_zero_value_input(*self.locator.START_13, name=N.START_13)
        self.check_special_symbol_input(*self.locator.START_13, name=N.START_13)
        self.check_letter_input(*self.locator.START_13, name=N.START_13)

        self.max_symbol_15_input(*self.locator.END_13, name=N.END_13)
        self.check_zero_value_input(*self.locator.END_13, name=N.END_13)
        self.check_special_symbol_input(*self.locator.END_13, name=N.END_13)
        self.check_letter_input(*self.locator.END_13, name=N.END_13)

        self.max_symbol_15_input(*self.locator.START_14, name=N.START_14)
        self.check_zero_value_input(*self.locator.START_14, name=N.START_14)
        self.check_special_symbol_input(*self.locator.START_14, name=N.START_14)
        self.check_letter_input(*self.locator.START_14, name=N.START_14)

        self.max_symbol_15_input(*self.locator.END_14, name=N.END_14)
        self.check_zero_value_input(*self.locator.END_14, name=N.END_14)
        self.check_special_symbol_input(*self.locator.END_14, name=N.END_14)
        self.check_letter_input(*self.locator.END_14, name=N.END_14)

        self.max_symbol_15_input(*self.locator.START_15, name=N.START_15)
        self.check_zero_value_input(*self.locator.START_15, name=N.START_15)
        self.check_special_symbol_input(*self.locator.START_15, name=N.START_15)
        self.check_letter_input(*self.locator.START_15, name=N.START_15)

        self.max_symbol_15_input(*self.locator.END_15, name=N.END_15)
        self.check_zero_value_input(*self.locator.END_15, name=N.END_15)
        self.check_special_symbol_input(*self.locator.END_15, name=N.END_15)
        self.check_letter_input(*self.locator.END_15, name=N.END_15)

        self.max_symbol_15_input(*self.locator.START_16, name=N.START_16)
        self.check_zero_value_input(*self.locator.START_16, name=N.START_16)
        self.check_special_symbol_input(*self.locator.START_16, name=N.START_16)
        self.check_letter_input(*self.locator.START_16, name=N.START_16)

        self.max_symbol_15_input(*self.locator.END_16, name=N.END_16)
        self.check_zero_value_input(*self.locator.END_16, name=N.END_16)
        self.check_special_symbol_input(*self.locator.END_16, name=N.END_16)
        self.check_letter_input(*self.locator.END_16, name=N.END_16)

        self.max_symbol_15_input(*self.locator.START_17, name=N.START_17)
        self.check_zero_value_input(*self.locator.START_17, name=N.START_17)
        self.check_special_symbol_input(*self.locator.START_17, name=N.START_17)
        self.check_letter_input(*self.locator.START_17, name=N.START_17)

        self.max_symbol_15_input(*self.locator.END_17, name=N.END_17)
        self.check_zero_value_input(*self.locator.END_17, name=N.END_17)
        self.check_special_symbol_input(*self.locator.END_17, name=N.END_17)
        self.check_letter_input(*self.locator.END_17, name=N.END_17)

        sleep(0.2)
        self.scroll('200')
        self.find_element(*self.locator.CHAPTER_2).click()
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.START_19, name=N.START_19)
        self.check_zero_value_input(*self.locator.START_19, name=N.START_19)
        self.check_special_symbol_input(*self.locator.START_19, name=N.START_19)
        self.check_letter_input(*self.locator.START_19, name=N.START_19)

        self.max_symbol_15_input(*self.locator.END_19, name=N.END_19)
        self.check_zero_value_input(*self.locator.END_19, name=N.END_19)
        self.check_special_symbol_input(*self.locator.END_19, name=N.END_19)
        self.check_letter_input(*self.locator.END_19, name=N.END_19)

        self.max_symbol_15_input(*self.locator.START_20, name=N.START_20)
        self.check_zero_value_input(*self.locator.START_20, name=N.START_20)
        self.check_special_symbol_input(*self.locator.START_20, name=N.START_20)
        self.check_letter_input(*self.locator.START_20, name=N.START_20)

        self.max_symbol_15_input(*self.locator.END_20, name=N.END_20)
        self.check_zero_value_input(*self.locator.END_20, name=N.END_20)
        self.check_special_symbol_input(*self.locator.END_20, name=N.END_20)
        self.check_letter_input(*self.locator.END_20, name=N.END_20)

        self.max_symbol_15_input(*self.locator.START_21, name=N.START_21)
        self.check_zero_value_input(*self.locator.START_21, name=N.START_21)
        self.check_special_symbol_input(*self.locator.START_21, name=N.START_21)
        self.check_letter_input(*self.locator.START_21, name=N.START_21)

        self.max_symbol_15_input(*self.locator.END_21, name=N.END_21)
        self.check_zero_value_input(*self.locator.END_21, name=N.END_21)
        self.check_special_symbol_input(*self.locator.END_21, name=N.END_21)
        self.check_letter_input(*self.locator.END_21, name=N.END_21)

        self.max_symbol_15_input(*self.locator.START_22, name=N.START_22)
        self.check_zero_value_input(*self.locator.START_22, name=N.START_22)
        self.check_special_symbol_input(*self.locator.START_22, name=N.START_22)
        self.check_letter_input(*self.locator.START_22, name=N.START_22)

        self.max_symbol_15_input(*self.locator.END_22, name=N.END_22)
        self.check_zero_value_input(*self.locator.END_22, name=N.END_22)
        self.check_special_symbol_input(*self.locator.END_22, name=N.END_22)
        self.check_letter_input(*self.locator.END_22, name=N.END_22)

        self.max_symbol_15_input(*self.locator.START_23, name=N.START_23)
        self.check_zero_value_input(*self.locator.START_23, name=N.START_23)
        self.check_special_symbol_input(*self.locator.START_23, name=N.START_23)
        self.check_letter_input(*self.locator.START_23, name=N.START_23)

        self.max_symbol_15_input(*self.locator.END_23, name=N.END_23)
        self.check_zero_value_input(*self.locator.END_23, name=N.END_23)
        self.check_special_symbol_input(*self.locator.END_23, name=N.END_23)
        self.check_letter_input(*self.locator.END_23, name=N.END_23)

        self.max_symbol_15_input(*self.locator.START_24, name=N.START_24)
        self.check_zero_value_input(*self.locator.START_24, name=N.START_24)
        self.check_special_symbol_input(*self.locator.START_24, name=N.START_24)
        self.check_letter_input(*self.locator.START_24, name=N.START_24)

        self.max_symbol_15_input(*self.locator.END_24, name=N.END_24)
        self.check_zero_value_input(*self.locator.END_24, name=N.END_24)
        self.check_special_symbol_input(*self.locator.END_24, name=N.END_24)
        self.check_letter_input(*self.locator.END_24, name=N.END_24)
        sleep(0.2)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.START_25, name=N.START_25)
        self.check_zero_value_input(*self.locator.START_25, name=N.START_25)
        self.check_special_symbol_input(*self.locator.START_25, name=N.START_25)
        self.check_letter_input(*self.locator.START_25, name=N.START_25)

        self.max_symbol_15_input(*self.locator.END_25, name=N.END_25)
        self.check_zero_value_input(*self.locator.END_25, name=N.END_25)
        self.check_special_symbol_input(*self.locator.END_25, name=N.END_25)
        self.check_letter_input(*self.locator.END_25, name=N.END_25)

        self.max_symbol_15_input(*self.locator.START_26, name=N.START_26)
        self.check_zero_value_input(*self.locator.START_26, name=N.START_26)
        self.check_special_symbol_input(*self.locator.START_26, name=N.START_26)
        self.check_letter_input(*self.locator.START_26, name=N.START_26)

        self.max_symbol_15_input(*self.locator.END_26, name=N.END_26)
        self.check_zero_value_input(*self.locator.END_26, name=N.END_26)
        self.check_special_symbol_input(*self.locator.END_26, name=N.END_26)
        self.check_letter_input(*self.locator.END_26, name=N.END_26)

        self.max_symbol_15_input(*self.locator.START_27, name=N.START_27)
        self.check_zero_value_input(*self.locator.START_27, name=N.START_27)
        self.check_special_symbol_input(*self.locator.START_27, name=N.START_27)
        self.check_letter_input(*self.locator.START_27, name=N.START_27)

        self.max_symbol_15_input(*self.locator.END_27, name=N.END_27)
        self.check_zero_value_input(*self.locator.END_27, name=N.END_27)
        self.check_special_symbol_input(*self.locator.END_27, name=N.END_27)
        self.check_letter_input(*self.locator.END_27, name=N.END_27)

        self.max_symbol_15_input(*self.locator.START_28, name=N.START_28)
        self.check_zero_value_input(*self.locator.START_28, name=N.START_28)
        self.check_special_symbol_input(*self.locator.START_28, name=N.START_28)
        self.check_letter_input(*self.locator.START_28, name=N.START_28)

        self.max_symbol_15_input(*self.locator.END_28, name=N.END_28)
        self.check_zero_value_input(*self.locator.END_28, name=N.END_28)
        self.check_special_symbol_input(*self.locator.END_28, name=N.END_28)
        self.check_letter_input(*self.locator.END_28, name=N.END_28)

        self.max_symbol_15_input(*self.locator.START_29, name=N.START_29)
        self.check_zero_value_input(*self.locator.START_29, name=N.START_29)
        self.check_special_symbol_input(*self.locator.START_29, name=N.START_29)
        self.check_letter_input(*self.locator.START_29, name=N.START_29)

        self.max_symbol_15_input(*self.locator.END_29, name=N.END_29)
        self.check_zero_value_input(*self.locator.END_29, name=N.END_29)
        self.check_special_symbol_input(*self.locator.END_29, name=N.END_29)
        self.check_letter_input(*self.locator.END_29, name=N.END_29)
        self.scroll('200')
        self.find_element(*self.locator.CHAPTER_3).click()
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.START_31, name=N.START_31)
        self.check_zero_value_input(*self.locator.START_31, name=N.START_31)
        self.check_special_symbol_input(*self.locator.START_31, name=N.START_31)
        self.check_letter_input(*self.locator.START_31, name=N.START_31)

        self.max_symbol_15_input(*self.locator.END_31, name=N.END_31)
        self.check_zero_value_input(*self.locator.END_31, name=N.END_31)
        self.check_special_symbol_input(*self.locator.END_31, name=N.END_31)
        self.check_letter_input(*self.locator.END_31, name=N.END_31)

        self.max_symbol_15_input(*self.locator.START_32, name=N.START_32)
        self.check_zero_value_input(*self.locator.START_32, name=N.START_32)
        self.check_special_symbol_input(*self.locator.START_32, name=N.START_32)
        self.check_letter_input(*self.locator.START_32, name=N.START_32)

        self.max_symbol_15_input(*self.locator.END_32, name=N.END_32)
        self.check_zero_value_input(*self.locator.END_32, name=N.END_32)
        self.check_special_symbol_input(*self.locator.END_32, name=N.END_32)
        self.check_letter_input(*self.locator.END_32, name=N.END_32)

        self.max_symbol_15_input(*self.locator.START_33, name=N.START_33)
        self.check_zero_value_input(*self.locator.START_33, name=N.START_33)
        self.check_special_symbol_input(*self.locator.START_33, name=N.START_33)
        self.check_letter_input(*self.locator.START_33, name=N.START_33)

        self.max_symbol_15_input(*self.locator.END_33, name=N.END_33)
        self.check_zero_value_input(*self.locator.END_33, name=N.END_33)
        self.check_special_symbol_input(*self.locator.END_33, name=N.END_33)
        self.check_letter_input(*self.locator.END_33, name=N.END_33)

        self.max_symbol_15_input(*self.locator.START_34, name=N.START_34)
        self.check_zero_value_input(*self.locator.START_34, name=N.START_34)
        self.check_special_symbol_input(*self.locator.START_34, name=N.START_34)
        self.check_letter_input(*self.locator.START_34, name=N.START_34)

        self.max_symbol_15_input(*self.locator.END_34, name=N.END_34)
        self.check_zero_value_input(*self.locator.END_34, name=N.END_34)
        self.check_special_symbol_input(*self.locator.END_34, name=N.END_34)
        self.check_letter_input(*self.locator.END_34, name=N.END_34)

        self.max_symbol_15_input(*self.locator.START_35, name=N.START_35)
        self.check_zero_value_input(*self.locator.START_35, name=N.START_35)
        self.check_special_symbol_input(*self.locator.START_35, name=N.START_35)
        self.check_letter_input(*self.locator.START_35, name=N.START_35)

        self.max_symbol_15_input(*self.locator.END_35, name=N.END_35)
        self.check_zero_value_input(*self.locator.END_35, name=N.END_35)
        self.check_special_symbol_input(*self.locator.END_35, name=N.END_35)
        self.check_letter_input(*self.locator.END_35, name=N.END_35)

        self.max_symbol_15_input(*self.locator.START_36, name=N.START_36)
        self.check_zero_value_input(*self.locator.START_36, name=N.START_36)
        self.check_special_symbol_input(*self.locator.START_36, name=N.START_36)
        self.check_letter_input(*self.locator.START_36, name=N.START_36)

        self.max_symbol_15_input(*self.locator.END_36, name=N.END_36)
        self.check_zero_value_input(*self.locator.END_36, name=N.END_36)
        self.check_special_symbol_input(*self.locator.END_36, name=N.END_36)
        self.check_letter_input(*self.locator.END_36, name=N.END_36)
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def validation_app_8(self):
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_1, name=N.EIGHT_PAGE_1)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_1, name=N.EIGHT_PAGE_1)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_1, name=N.EIGHT_PAGE_1)
        self.check_letter_input(*self.locator.EIGHT_PAGE_1, name=N.EIGHT_PAGE_1)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_2, name=N.EIGHT_PAGE_2)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_2, name=N.EIGHT_PAGE_2)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_2, name=N.EIGHT_PAGE_2)
        self.check_letter_input(*self.locator.EIGHT_PAGE_2, name=N.EIGHT_PAGE_2)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_3, name=N.EIGHT_PAGE_3)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_3, name=N.EIGHT_PAGE_3)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_3, name=N.EIGHT_PAGE_3)
        self.check_letter_input(*self.locator.EIGHT_PAGE_3, name=N.EIGHT_PAGE_3)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_4, name=N.EIGHT_PAGE_4)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_4, name=N.EIGHT_PAGE_4)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_4, name=N.EIGHT_PAGE_4)
        self.check_letter_input(*self.locator.EIGHT_PAGE_4, name=N.EIGHT_PAGE_4)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_5, name=N.EIGHT_PAGE_5)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_5, name=N.EIGHT_PAGE_5)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_5, name=N.EIGHT_PAGE_5)
        self.check_letter_input(*self.locator.EIGHT_PAGE_5, name=N.EIGHT_PAGE_5)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_6, name=N.EIGHT_PAGE_6)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_6, name=N.EIGHT_PAGE_6)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_6, name=N.EIGHT_PAGE_6)
        self.check_letter_input(*self.locator.EIGHT_PAGE_6, name=N.EIGHT_PAGE_6)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_7, name=N.EIGHT_PAGE_7)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_7, name=N.EIGHT_PAGE_7)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_7, name=N.EIGHT_PAGE_7)
        self.check_letter_input(*self.locator.EIGHT_PAGE_7, name=N.EIGHT_PAGE_7)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_8, name=N.EIGHT_PAGE_8)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_8, name=N.EIGHT_PAGE_8)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_8, name=N.EIGHT_PAGE_8)
        self.check_letter_input(*self.locator.EIGHT_PAGE_8, name=N.EIGHT_PAGE_8)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_9, name=N.EIGHT_PAGE_9)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_9, name=N.EIGHT_PAGE_9)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_9, name=N.EIGHT_PAGE_9)
        self.check_letter_input(*self.locator.EIGHT_PAGE_9, name=N.EIGHT_PAGE_9)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_10, name=N.EIGHT_PAGE_10)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_10, name=N.EIGHT_PAGE_10)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_10, name=N.EIGHT_PAGE_10)
        self.check_letter_input(*self.locator.EIGHT_PAGE_10, name=N.EIGHT_PAGE_10)

        self.max_symbol_15_input(*self.locator.EIGHT_PAGE_11, name=N.EIGHT_PAGE_11)
        self.check_zero_value_input(*self.locator.EIGHT_PAGE_11, name=N.EIGHT_PAGE_11)
        self.check_special_symbol_input(*self.locator.EIGHT_PAGE_11, name=N.EIGHT_PAGE_11)
        self.check_letter_input(*self.locator.EIGHT_PAGE_11, name=N.EIGHT_PAGE_11)

        sleep(0.2)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_9(self):
        self.scroll('10000')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.D_APP_9).send_keys('12345678901234567')
        sleep(0.2)
        assert '1234567890123456' in self.browser.page_source
        self.find_element(*self.locator.E_APP_9).send_keys('9,12345')
        sleep(0.2)
        element = self.browser.find_element_by_xpath('//*[@name="Q"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

        #self.max_symbol_12_input(*self.locator.G_APP_9, name=N.G_APP_9)
        self.check_zero_value_input(*self.locator.G_APP_9, name=N.G_APP_9)
        self.check_special_symbol_input(*self.locator.G_APP_9, name=N.G_APP_9)
        self.check_letter_input(*self.locator.G_APP_9, name=N.G_APP_9)

        #self.max_symbol_12_input(*self.locator.H_APP_9, name=N.H_APP_9)
        self.check_zero_value_input(*self.locator.H_APP_9, name=N.H_APP_9)
        self.check_special_symbol_input(*self.locator.H_APP_9, name=N.H_APP_9)
        self.check_letter_input(*self.locator.H_APP_9, name=N.H_APP_9)

        #self.max_symbol_12_input(*self.locator.J_APP_9, name=N.J_APP_9)
        self.check_zero_value_input(*self.locator.J_APP_9, name=N.J_APP_9)
        self.check_special_symbol_input(*self.locator.J_APP_9, name=N.J_APP_9)
        self.check_letter_input(*self.locator.J_APP_9, name=N.J_APP_9)

        #self.max_symbol_12_input(*self.locator.L_APP_9, name=N.L_APP_9)
        self.check_zero_value_input(*self.locator.L_APP_9, name=N.L_APP_9)
        self.check_special_symbol_input(*self.locator.L_APP_9, name=N.L_APP_9)
        self.check_letter_input(*self.locator.L_APP_9, name=N.L_APP_9)

        #self.max_symbol_12_input(*self.locator.M_APP_9, name=N.M_APP_9)
        self.check_zero_value_input(*self.locator.M_APP_9, name=N.M_APP_9)
        self.check_special_symbol_input(*self.locator.M_APP_9, name=N.M_APP_9)
        self.check_letter_input(*self.locator.M_APP_9, name=N.M_APP_9)

        #self.max_symbol_12_input(*self.locator.N_APP_9, name=N.N_APP_9)
        self.check_zero_value_input(*self.locator.N_APP_9, name=N.N_APP_9)
        self.check_special_symbol_input(*self.locator.N_APP_9, name=N.N_APP_9)
        self.check_letter_input(*self.locator.N_APP_9, name=N.N_APP_9)

        #self.max_symbol_12_input(*self.locator.O_APP_9, name=N.O_APP_9)
        self.check_zero_value_input(*self.locator.O_APP_9, name=N.O_APP_9)
        self.check_special_symbol_input(*self.locator.O_APP_9, name=N.O_APP_9)
        self.check_letter_input(*self.locator.O_APP_9, name=N.O_APP_9)

        #self.max_symbol_12_input(*self.locator.P_APP_9, name=N.P_APP_9)
        self.check_zero_value_input(*self.locator.P_APP_9, name=N.P_APP_9)
        self.check_special_symbol_input(*self.locator.P_APP_9, name=N.P_APP_9)
        self.check_letter_input(*self.locator.P_APP_9, name=N.P_APP_9)

        #self.max_symbol_12_input(*self.locator.Q_APP_9, name=N.Q_APP_9)
        self.check_zero_value_input(*self.locator.Q_APP_9, name=N.Q_APP_9)
        self.check_special_symbol_input(*self.locator.Q_APP_9, name=N.Q_APP_9)
        self.check_letter_input(*self.locator.Q_APP_9, name=N.Q_APP_9)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def validation_app_10(self):
        sleep(0.2)
        self.find_element(*self.locator.EARNING_TEN).click()
        sleep(0.2)
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.TEN_PAGE_1, name=N.TEN_PAGE_1)
        self.check_zero_value_input(*self.locator.TEN_PAGE_1, name=N.TEN_PAGE_1)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_1, name=N.TEN_PAGE_1)
        self.check_letter_input(*self.locator.TEN_PAGE_1, name=N.TEN_PAGE_1)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_2, name=N.TEN_PAGE_2)
        self.check_zero_value_input(*self.locator.TEN_PAGE_2, name=N.TEN_PAGE_2)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_2, name=N.TEN_PAGE_2)
        self.check_letter_input(*self.locator.TEN_PAGE_2, name=N.TEN_PAGE_2)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_3, name=N.TEN_PAGE_3)
        self.check_zero_value_input(*self.locator.TEN_PAGE_3, name=N.TEN_PAGE_3)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_3, name=N.TEN_PAGE_3)
        self.check_letter_input(*self.locator.TEN_PAGE_3, name=N.TEN_PAGE_3)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_4, name=N.TEN_PAGE_4)
        self.check_zero_value_input(*self.locator.TEN_PAGE_4, name=N.TEN_PAGE_4)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_4, name=N.TEN_PAGE_4)
        self.check_letter_input(*self.locator.TEN_PAGE_4, name=N.TEN_PAGE_4)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_5, name=N.TEN_PAGE_5)
        self.check_zero_value_input(*self.locator.TEN_PAGE_5, name=N.TEN_PAGE_5)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_5, name=N.TEN_PAGE_5)
        self.check_letter_input(*self.locator.TEN_PAGE_5, name=N.TEN_PAGE_5)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_6, name=N.TEN_PAGE_6)
        self.check_zero_value_input(*self.locator.TEN_PAGE_6, name=N.TEN_PAGE_6)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_6, name=N.TEN_PAGE_6)
        self.check_letter_input(*self.locator.TEN_PAGE_6, name=N.TEN_PAGE_6)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_7, name=N.TEN_PAGE_7)
        self.check_zero_value_input(*self.locator.TEN_PAGE_7, name=N.TEN_PAGE_7)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_7, name=N.TEN_PAGE_7)
        self.check_letter_input(*self.locator.TEN_PAGE_7, name=N.TEN_PAGE_7)
        sleep(0.2)
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.TEN_PAGE_8, name=N.TEN_PAGE_8)
        self.check_zero_value_input(*self.locator.TEN_PAGE_8, name=N.TEN_PAGE_8)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_8, name=N.TEN_PAGE_8)
        self.check_letter_input(*self.locator.TEN_PAGE_8, name=N.TEN_PAGE_8)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_9, name=N.TEN_PAGE_9)
        self.check_zero_value_input(*self.locator.TEN_PAGE_9, name=N.TEN_PAGE_9)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_9, name=N.TEN_PAGE_9)
        self.check_letter_input(*self.locator.TEN_PAGE_9, name=N.TEN_PAGE_9)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_10, name=N.TEN_PAGE_10)
        self.check_zero_value_input(*self.locator.TEN_PAGE_10, name=N.TEN_PAGE_10)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_10, name=N.TEN_PAGE_10)
        self.check_letter_input(*self.locator.TEN_PAGE_10, name=N.TEN_PAGE_10)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_12, name=N.TEN_PAGE_12)
        self.check_zero_value_input(*self.locator.TEN_PAGE_12, name=N.TEN_PAGE_12)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_12, name=N.TEN_PAGE_12)
        self.check_letter_input(*self.locator.TEN_PAGE_12, name=N.TEN_PAGE_12)
        sleep(0.2)
        self.scroll('500')
        self.find_element(*self.locator.EXPENSES_TEN).click()
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_I, name=N.TEN_PAGE_14_I)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_I, name=N.TEN_PAGE_14_I)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_I, name=N.TEN_PAGE_14_I)
        self.check_letter_input(*self.locator.TEN_PAGE_14_I, name=N.TEN_PAGE_14_I)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_II, name=N.TEN_PAGE_14_II)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_II, name=N.TEN_PAGE_14_II)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_II, name=N.TEN_PAGE_14_II)
        self.check_letter_input(*self.locator.TEN_PAGE_14_II, name=N.TEN_PAGE_14_II)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_III, name=N.TEN_PAGE_14_III)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_III, name=N.TEN_PAGE_14_III)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_III, name=N.TEN_PAGE_14_III)
        self.check_letter_input(*self.locator.TEN_PAGE_14_III, name=N.TEN_PAGE_14_III)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_IV, name=N.TEN_PAGE_14_IV)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_IV, name=N.TEN_PAGE_14_IV)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_IV, name=N.TEN_PAGE_14_IV)
        self.check_letter_input(*self.locator.TEN_PAGE_14_IV, name=N.TEN_PAGE_14_IV)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_V, name=N.TEN_PAGE_14_V)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_V, name=N.TEN_PAGE_14_V)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_V, name=N.TEN_PAGE_14_V)
        self.check_letter_input(*self.locator.TEN_PAGE_14_V, name=N.TEN_PAGE_14_V)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_VI, name=N.TEN_PAGE_14_VI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_VI, name=N.TEN_PAGE_14_VI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_VI, name=N.TEN_PAGE_14_VI)
        self.check_letter_input(*self.locator.TEN_PAGE_14_VI, name=N.TEN_PAGE_14_VI)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_VII, name=N.TEN_PAGE_14_VII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_VII, name=N.TEN_PAGE_14_VII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_VII, name=N.TEN_PAGE_14_VII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_VII, name=N.TEN_PAGE_14_VII)
        sleep(0.2)
        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_VIII, name=N.TEN_PAGE_14_VIII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_VIII, name=N.TEN_PAGE_14_VIII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_VIII, name=N.TEN_PAGE_14_VIII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_VIII, name=N.TEN_PAGE_14_VIII)

        sleep(0.2)
        self.scroll('650')

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_IX, name=N.TEN_PAGE_14_IX)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_IX, name=N.TEN_PAGE_14_IX)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_IX, name=N.TEN_PAGE_14_IX)
        self.check_letter_input(*self.locator.TEN_PAGE_14_IX, name=N.TEN_PAGE_14_IX)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_X, name=N.TEN_PAGE_14_X)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_X, name=N.TEN_PAGE_14_X)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_X, name=N.TEN_PAGE_14_X)
        self.check_letter_input(*self.locator.TEN_PAGE_14_X, name=N.TEN_PAGE_14_X)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XI, name=N.TEN_PAGE_14_XI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XI, name=N.TEN_PAGE_14_XI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XI, name=N.TEN_PAGE_14_XI)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XI, name=N.TEN_PAGE_14_XI)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XII, name=N.TEN_PAGE_14_XII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XII, name=N.TEN_PAGE_14_XII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XII, name=N.TEN_PAGE_14_XII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XII, name=N.TEN_PAGE_14_XII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIII, name=N.TEN_PAGE_14_XIII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIII, name=N.TEN_PAGE_14_XIII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIII, name=N.TEN_PAGE_14_XIII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIII, name=N.TEN_PAGE_14_XIII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIV, name=N.TEN_PAGE_14_XIV)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIV, name=N.TEN_PAGE_14_XIV)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIV, name=N.TEN_PAGE_14_XIV)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIV, name=N.TEN_PAGE_14_XIV)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XV, name=N.TEN_PAGE_14_XV)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XV, name=N.TEN_PAGE_14_XV)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XV, name=N.TEN_PAGE_14_XV)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XV, name=N.TEN_PAGE_14_XV)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XVI, name=N.TEN_PAGE_14_XVI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XVI, name=N.TEN_PAGE_14_XVI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XVI, name=N.TEN_PAGE_14_XVI)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XVI, name=N.TEN_PAGE_14_XVI)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XVII, name=N.TEN_PAGE_14_XVII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XVII, name=N.TEN_PAGE_14_XVII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XVII, name=N.TEN_PAGE_14_XVII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XVII, name=N.TEN_PAGE_14_XVII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XVIII, name=N.TEN_PAGE_14_XVIII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XVIII, name=N.TEN_PAGE_14_XVIII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XVIII, name=N.TEN_PAGE_14_XVIII)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XVIII, name=N.TEN_PAGE_14_XVIII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIX_A, name=N.TEN_PAGE_14_XIX_A)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIX_A, name=N.TEN_PAGE_14_XIX_A)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIX_A, name=N.TEN_PAGE_14_XIX_A)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIX_A, name=N.TEN_PAGE_14_XIX_A)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIX_B, name=N.TEN_PAGE_14_XIX_B)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIX_B, name=N.TEN_PAGE_14_XIX_B)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIX_B, name=N.TEN_PAGE_14_XIX_B)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIX_B, name=N.TEN_PAGE_14_XIX_B)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIX_C, name=N.TEN_PAGE_14_XIX_C)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIX_C, name=N.TEN_PAGE_14_XIX_C)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIX_C, name=N.TEN_PAGE_14_XIX_C)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIX_C, name=N.TEN_PAGE_14_XIX_C)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIX_D, name=N.TEN_PAGE_14_XIX_D)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIX_D, name=N.TEN_PAGE_14_XIX_D)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIX_D, name=N.TEN_PAGE_14_XIX_D)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIX_D, name=N.TEN_PAGE_14_XIX_D)

        sleep(0.2)
        self.scroll('700')

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XIX_E, name=N.TEN_PAGE_14_XIX_E)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XIX_E, name=N.TEN_PAGE_14_XIX_E)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XIX_E, name=N.TEN_PAGE_14_XIX_E)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XIX_E, name=N.TEN_PAGE_14_XIX_E)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XX, name=N.TEN_PAGE_14_XX)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XX, name=N.TEN_PAGE_14_XX)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XX, name=N.TEN_PAGE_14_XX)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XX, name=N.TEN_PAGE_14_XX)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_14_XXI, name=N.TEN_PAGE_14_XXI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_14_XXI, name=N.TEN_PAGE_14_XXI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_14_XXI, name=N.TEN_PAGE_14_XXI)
        self.check_letter_input(*self.locator.TEN_PAGE_14_XXI, name=N.TEN_PAGE_14_XXI)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_I, name=N.TEN_PAGE_15_I)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_I, name=N.TEN_PAGE_15_I)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_I, name=N.TEN_PAGE_15_I)
        self.check_letter_input(*self.locator.TEN_PAGE_15_I, name=N.TEN_PAGE_15_I)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_II, name=N.TEN_PAGE_15_II)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_II, name=N.TEN_PAGE_15_II)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_II, name=N.TEN_PAGE_15_II)
        self.check_letter_input(*self.locator.TEN_PAGE_15_II, name=N.TEN_PAGE_15_II)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_III, name=N.TEN_PAGE_15_III)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_III, name=N.TEN_PAGE_15_III)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_III, name=N.TEN_PAGE_15_III)
        self.check_letter_input(*self.locator.TEN_PAGE_15_III, name=N.TEN_PAGE_15_III)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_IV, name=N.TEN_PAGE_15_IV)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_IV, name=N.TEN_PAGE_15_IV)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_IV, name=N.TEN_PAGE_15_IV)
        self.check_letter_input(*self.locator.TEN_PAGE_15_IV, name=N.TEN_PAGE_15_IV)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_V, name=N.TEN_PAGE_15_V)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_V, name=N.TEN_PAGE_15_V)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_V, name=N.TEN_PAGE_15_V)
        self.check_letter_input(*self.locator.TEN_PAGE_15_V, name=N.TEN_PAGE_15_V)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_VI, name=N.TEN_PAGE_15_VI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_VI, name=N.TEN_PAGE_15_VI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_VI, name=N.TEN_PAGE_15_VI)
        self.check_letter_input(*self.locator.TEN_PAGE_15_VI, name=N.TEN_PAGE_15_VI)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_VII, name=N.TEN_PAGE_15_VII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_VII, name=N.TEN_PAGE_15_VII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_VII, name=N.TEN_PAGE_15_VII)
        self.check_letter_input(*self.locator.TEN_PAGE_15_VII, name=N.TEN_PAGE_15_VII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_VIII, name=N.TEN_PAGE_15_VIII)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_VIII, name=N.TEN_PAGE_15_VIII)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_VIII, name=N.TEN_PAGE_15_VIII)
        self.check_letter_input(*self.locator.TEN_PAGE_15_VIII, name=N.TEN_PAGE_15_VIII)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_IX, name=N.TEN_PAGE_15_IX)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_IX, name=N.TEN_PAGE_15_IX)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_IX, name=N.TEN_PAGE_15_IX)
        self.check_letter_input(*self.locator.TEN_PAGE_15_IX, name=N.TEN_PAGE_15_IX)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_X, name=N.TEN_PAGE_15_X)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_X, name=N.TEN_PAGE_15_X)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_X, name=N.TEN_PAGE_15_X)
        self.check_letter_input(*self.locator.TEN_PAGE_15_X, name=N.TEN_PAGE_15_X)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_15_XI, name=N.TEN_PAGE_15_XI)
        self.check_zero_value_input(*self.locator.TEN_PAGE_15_XI, name=N.TEN_PAGE_15_XI)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_15_XI, name=N.TEN_PAGE_15_XI)
        self.check_letter_input(*self.locator.TEN_PAGE_15_XI, name=N.TEN_PAGE_15_XI)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_16, name=N.TEN_PAGE_16)
        self.check_zero_value_input(*self.locator.TEN_PAGE_16, name=N.TEN_PAGE_16)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_16, name=N.TEN_PAGE_16)
        self.check_letter_input(*self.locator.TEN_PAGE_16, name=N.TEN_PAGE_16)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_17, name=N.TEN_PAGE_17)
        self.check_zero_value_input(*self.locator.TEN_PAGE_17, name=N.TEN_PAGE_17)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_17, name=N.TEN_PAGE_17)
        self.check_letter_input(*self.locator.TEN_PAGE_17, name=N.TEN_PAGE_17)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_18, name=N.TEN_PAGE_18)
        self.check_zero_value_input(*self.locator.TEN_PAGE_18, name=N.TEN_PAGE_18)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_18, name=N.TEN_PAGE_18)
        self.check_letter_input(*self.locator.TEN_PAGE_18, name=N.TEN_PAGE_18)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_19, name=N.TEN_PAGE_19)
        self.check_zero_value_input(*self.locator.TEN_PAGE_19, name=N.TEN_PAGE_19)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_19, name=N.TEN_PAGE_19)
        self.check_letter_input(*self.locator.TEN_PAGE_19, name=N.TEN_PAGE_19)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_20, name=N.TEN_PAGE_20)
        self.check_zero_value_input(*self.locator.TEN_PAGE_20, name=N.TEN_PAGE_20)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_20, name=N.TEN_PAGE_20)
        self.check_letter_input(*self.locator.TEN_PAGE_20, name=N.TEN_PAGE_20)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_21, name=N.TEN_PAGE_21)
        self.check_zero_value_input(*self.locator.TEN_PAGE_21, name=N.TEN_PAGE_21)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_21, name=N.TEN_PAGE_21)
        self.check_letter_input(*self.locator.TEN_PAGE_21, name=N.TEN_PAGE_21)

        self.max_symbol_15_input(*self.locator.TEN_PAGE_22, name=N.TEN_PAGE_22)
        self.check_zero_value_input(*self.locator.TEN_PAGE_22, name=N.TEN_PAGE_22)
        self.check_special_symbol_input(*self.locator.TEN_PAGE_22, name=N.TEN_PAGE_22)
        self.check_letter_input(*self.locator.TEN_PAGE_22, name=N.TEN_PAGE_22)

        self.find_element(*self.locator.AFTER).click()

    def validation_app_11(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()

        self.max_symbol_12_input(*self.locator.B_APP_11, name=N.B_APP_11)
        self.check_zero_value_input(*self.locator.B_APP_11, name=N.B_APP_11)
        self.check_special_symbol_input(*self.locator.B_APP_11, name=N.B_APP_11)
        self.check_letter_input(*self.locator.B_APP_11, name=N.B_APP_11)

        self.max_symbol_15_input(*self.locator.D_APP_11, name=N.D_APP_11)
        self.check_zero_value_input(*self.locator.D_APP_11, name=N.D_APP_11)
        self.check_special_symbol_input(*self.locator.D_APP_11, name=N.D_APP_11)
        self.check_letter_input(*self.locator.D_APP_11, name=N.D_APP_11)

        element = self.browser.find_element_by_xpath('//*[text()="Добавить"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

        self.max_symbol_15_input(*self.locator.G_A_APP_11, name=N.G_A_APP_11)
        self.check_zero_value_input(*self.locator.G_A_APP_11, name=N.G_A_APP_11)
        self.check_special_symbol_input(*self.locator.G_A_APP_11, name=N.G_A_APP_11)
        self.check_letter_input(*self.locator.G_A_APP_11, name=N.G_A_APP_11)

        self.max_symbol_15_input(*self.locator.H_APP_11, name=N.H_APP_11)
        self.check_zero_value_input(*self.locator.H_APP_11, name=N.H_APP_11)
        self.check_special_symbol_input(*self.locator.H_APP_11, name=N.H_APP_11)
        self.check_letter_input(*self.locator.H_APP_11, name=N.H_APP_11)

        self.max_symbol_15_input(*self.locator.I_APP_11, name=N.I_APP_11)
        self.check_zero_value_input(*self.locator.I_APP_11, name=N.I_APP_11)
        self.check_special_symbol_input(*self.locator.I_APP_11, name=N.I_APP_11)
        self.check_letter_input(*self.locator.I_APP_11, name=N.I_APP_11)
        sleep(0.2)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        sleep(0.2)
        self.find_element(*self.locator.AFTER).click()

    def validation_app_12(self):
        sleep(1)
        self.find_element(*self.locator.TWELVE_CHAPTER_1).click()
        self.scroll('400')
        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_1, name=N.TWELVE_PAGE_1)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_1, name=N.TWELVE_PAGE_1)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_1, name=N.TWELVE_PAGE_1)
        self.check_letter_input(*self.locator.TWELVE_PAGE_1, name=N.TWELVE_PAGE_1)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_2, name=N.TWELVE_PAGE_2)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_2, name=N.TWELVE_PAGE_2)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_2, name=N.TWELVE_PAGE_2)
        self.check_letter_input(*self.locator.TWELVE_PAGE_2, name=N.TWELVE_PAGE_2)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_3, name=N.TWELVE_PAGE_3)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_3, name=N.TWELVE_PAGE_3)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_3, name=N.TWELVE_PAGE_3)
        self.check_letter_input(*self.locator.TWELVE_PAGE_3, name=N.TWELVE_PAGE_3)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_4, name=N.TWELVE_PAGE_4)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_4, name=N.TWELVE_PAGE_4)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_4, name=N.TWELVE_PAGE_4)
        self.check_letter_input(*self.locator.TWELVE_PAGE_4, name=N.TWELVE_PAGE_4)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_5, name=N.TWELVE_PAGE_5)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_5, name=N.TWELVE_PAGE_5)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_5, name=N.TWELVE_PAGE_5)
        self.check_letter_input(*self.locator.TWELVE_PAGE_5, name=N.TWELVE_PAGE_5)

        self.find_element(*self.locator.TWELVE_CHAPTER_2).click()
        self.scroll('500')

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_7, name=N.TWELVE_PAGE_7)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_7, name=N.TWELVE_PAGE_7)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_7, name=N.TWELVE_PAGE_7)
        self.check_letter_input(*self.locator.TWELVE_PAGE_7, name=N.TWELVE_PAGE_7)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_8, name=N.TWELVE_PAGE_8)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_8, name=N.TWELVE_PAGE_8)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_8, name=N.TWELVE_PAGE_8)
        self.check_letter_input(*self.locator.TWELVE_PAGE_8, name=N.TWELVE_PAGE_8)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_9, name=N.TWELVE_PAGE_9)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_9, name=N.TWELVE_PAGE_9)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_9, name=N.TWELVE_PAGE_9)
        self.check_letter_input(*self.locator.TWELVE_PAGE_9, name=N.TWELVE_PAGE_9)

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_10, name=N.TWELVE_PAGE_10)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_10, name=N.TWELVE_PAGE_10)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_10, name=N.TWELVE_PAGE_10)
        self.check_letter_input(*self.locator.TWELVE_PAGE_10, name=N.TWELVE_PAGE_10)

        self.find_element(*self.locator.TWELVE_CHAPTER_3).click()
        self.scroll('500')

        self.max_symbol_15_input(*self.locator.TWELVE_PAGE_12, name=N.TWELVE_PAGE_12)
        self.check_zero_value_input(*self.locator.TWELVE_PAGE_12, name=N.TWELVE_PAGE_12)
        self.check_special_symbol_input(*self.locator.TWELVE_PAGE_12, name=N.TWELVE_PAGE_12)
        self.check_letter_input(*self.locator.TWELVE_PAGE_12, name=N.TWELVE_PAGE_12)

        self.find_element(*self.locator.AFTER).click()
