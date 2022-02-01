from browser_interaction import BasePage
from time import sleep
from locators.fno_220_locators import FNO220Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_220_locators import FNO220LocatorsName as N


class FNO220MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO220Locators

        # НАЧАТО СО ВТОРОЙ СТРАНИЦЫ

    def second_page_validation(self):
        sleep(1)
        self.max_symbol_15_input(*self.locator.INCOME_1, name=N.INCOME_1)
        self.check_zero_value_input(*self.locator.INCOME_1, name=N.INCOME_1)
        self.check_special_symbol_input(*self.locator.INCOME_1, name=N.INCOME_1)
        self.check_letter_input(*self.locator.INCOME_1, name=N.INCOME_1)

        self.max_symbol_15_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_zero_value_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_special_symbol_input(*self.locator.INCOME_2, name=N.INCOME_2)
        self.check_letter_input(*self.locator.INCOME_2, name=N.INCOME_2)

        self.max_symbol_15_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_zero_value_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_special_symbol_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.check_letter_input(*self.locator.INCOME_3, name=N.INCOME_3)
        self.scroll('500')

        self.max_symbol_15_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_zero_value_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_special_symbol_input(*self.locator.INCOME_5, name=N.INCOME_5)
        self.check_letter_input(*self.locator.INCOME_5, name=N.INCOME_5)

        self.max_symbol_15_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_zero_value_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_special_symbol_input(*self.locator.INCOME_6, name=N.INCOME_6)
        self.check_letter_input(*self.locator.INCOME_6, name=N.INCOME_6)

        self.max_symbol_15_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_zero_value_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_special_symbol_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)
        self.check_letter_input(*self.locator.INCOME_7_I, name=N.INCOME_7_I)

        self.max_symbol_15_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_zero_value_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_special_symbol_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)
        self.check_letter_input(*self.locator.INCOME_7_II, name=N.INCOME_7_II)

        self.scroll('400')

        self.max_symbol_15_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_zero_value_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_special_symbol_input(*self.locator.INCOME_8, name=N.INCOME_8)
        self.check_letter_input(*self.locator.INCOME_8, name=N.INCOME_8)

        self.max_symbol_15_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_zero_value_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_special_symbol_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.check_letter_input(*self.locator.INCOME_9, name=N.INCOME_9)
        self.find_element(*self.locator.AFTER).click()

    def third_page_validation(self):
        sleep(1)
        self.find_element(*self.locator.DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('800')
        self.max_symbol_15_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_zero_value_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_special_symbol_input(*self.locator.STOCK_1, name=N.STOCK_1)
        self.check_letter_input(*self.locator.STOCK_1, name=N.STOCK_1)

        self.max_symbol_15_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_zero_value_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_special_symbol_input(*self.locator.STOCK_2, name=N.STOCK_2)
        self.check_letter_input(*self.locator.STOCK_2, name=N.STOCK_2)

        self.max_symbol_15_input(*self.locator.STOCK_3_A, name=N.STOCK_3_A)
        self.check_zero_value_input(*self.locator.STOCK_3_A, name=N.STOCK_3_A)
        self.check_special_symbol_input(*self.locator.STOCK_3_A, name=N.STOCK_3_A)
        self.check_letter_input(*self.locator.STOCK_3_A, name=N.STOCK_3_A)

        self.max_symbol_15_input(*self.locator.STOCK_3_B, name=N.STOCK_3_B)
        self.check_zero_value_input(*self.locator.STOCK_3_B, name=N.STOCK_3_B)
        self.check_special_symbol_input(*self.locator.STOCK_3_B, name=N.STOCK_3_B)
        self.check_letter_input(*self.locator.STOCK_3_B, name=N.STOCK_3_B)

        self.max_symbol_15_input(*self.locator.STOCK_3_C, name=N.STOCK_3_C)
        self.check_zero_value_input(*self.locator.STOCK_3_C, name=N.STOCK_3_C)
        self.check_special_symbol_input(*self.locator.STOCK_3_C, name=N.STOCK_3_C)
        self.check_letter_input(*self.locator.STOCK_3_C, name=N.STOCK_3_C)

        self.max_symbol_15_input(*self.locator.STOCK_3_D, name=N.STOCK_3_D)
        self.check_zero_value_input(*self.locator.STOCK_3_D, name=N.STOCK_3_D)
        self.check_special_symbol_input(*self.locator.STOCK_3_D, name=N.STOCK_3_D)
        self.check_letter_input(*self.locator.STOCK_3_D, name=N.STOCK_3_D)

        self.max_symbol_15_input(*self.locator.STOCK_3_E, name=N.STOCK_3_E)
        self.check_zero_value_input(*self.locator.STOCK_3_E, name=N.STOCK_3_E)
        self.check_special_symbol_input(*self.locator.STOCK_3_E, name=N.STOCK_3_E)
        self.check_letter_input(*self.locator.STOCK_3_E, name=N.STOCK_3_E)

        self.max_symbol_15_input(*self.locator.STOCK_3_F, name=N.STOCK_3_F)
        self.check_zero_value_input(*self.locator.STOCK_3_F, name=N.STOCK_3_F)
        self.check_special_symbol_input(*self.locator.STOCK_3_F, name=N.STOCK_3_F)
        self.check_letter_input(*self.locator.STOCK_3_F, name=N.STOCK_3_F)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.STOCK_3_G, name=N.STOCK_3_G)
        self.check_zero_value_input(*self.locator.STOCK_3_G, name=N.STOCK_3_G)
        self.check_special_symbol_input(*self.locator.STOCK_3_G, name=N.STOCK_3_G)
        self.check_letter_input(*self.locator.STOCK_3_G, name=N.STOCK_3_G)

        self.max_symbol_15_input(*self.locator.STOCK_3_H, name=N.STOCK_3_H)
        self.check_zero_value_input(*self.locator.STOCK_3_H, name=N.STOCK_3_H)
        self.check_special_symbol_input(*self.locator.STOCK_3_H, name=N.STOCK_3_H)
        self.check_letter_input(*self.locator.STOCK_3_H, name=N.STOCK_3_H)

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

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_zero_value_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_special_symbol_input(*self.locator.STOCK_8, name=N.STOCK_8)
        self.check_letter_input(*self.locator.STOCK_8, name=N.STOCK_8)

        self.max_symbol_15_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_zero_value_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_special_symbol_input(*self.locator.STOCK_9, name=N.STOCK_9)
        self.check_letter_input(*self.locator.STOCK_9, name=N.STOCK_9)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_12, name=N.THIRD_PAGE_12)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_12, name=N.THIRD_PAGE_12)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_12, name=N.THIRD_PAGE_12)
        self.check_letter_input(*self.locator.THIRD_PAGE_12, name=N.THIRD_PAGE_12)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_13, name=N.THIRD_PAGE_13)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_13, name=N.THIRD_PAGE_13)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_13, name=N.THIRD_PAGE_13)
        self.check_letter_input(*self.locator.THIRD_PAGE_13, name=N.THIRD_PAGE_13)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_14, name=N.THIRD_PAGE_14)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_14, name=N.THIRD_PAGE_14)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_14, name=N.THIRD_PAGE_14)
        self.check_letter_input(*self.locator.THIRD_PAGE_14, name=N.THIRD_PAGE_14)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_15, name=N.THIRD_PAGE_15)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_15, name=N.THIRD_PAGE_15)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_15, name=N.THIRD_PAGE_15)
        self.check_letter_input(*self.locator.THIRD_PAGE_15, name=N.THIRD_PAGE_15)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_16, name=N.THIRD_PAGE_16)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_16, name=N.THIRD_PAGE_16)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_16, name=N.THIRD_PAGE_16)
        self.check_letter_input(*self.locator.THIRD_PAGE_16, name=N.THIRD_PAGE_16)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_17, name=N.THIRD_PAGE_17)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_17, name=N.THIRD_PAGE_17)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_17, name=N.THIRD_PAGE_17)
        self.check_letter_input(*self.locator.THIRD_PAGE_17, name=N.THIRD_PAGE_17)

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_18, name=N.THIRD_PAGE_18)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_18, name=N.THIRD_PAGE_18)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_18, name=N.THIRD_PAGE_18)
        self.check_letter_input(*self.locator.THIRD_PAGE_18, name=N.THIRD_PAGE_18)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.THIRD_PAGE_20, name=N.THIRD_PAGE_20)
        self.check_zero_value_input(*self.locator.THIRD_PAGE_20, name=N.THIRD_PAGE_20)
        self.check_special_symbol_input(*self.locator.THIRD_PAGE_20, name=N.THIRD_PAGE_20)
        self.check_letter_input(*self.locator.THIRD_PAGE_20, name=N.THIRD_PAGE_20)

        self.find_element(*self.locator.AFTER).click()

    def fourth_page_validation(self):
        sleep(1)
        self.find_element(*self.locator.DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('500')

        self.max_symbol_15_input(*self.locator.FOURTH_PAGE_22, name=N.FOURTH_PAGE_22)
        self.check_zero_value_input(*self.locator.FOURTH_PAGE_22, name=N.FOURTH_PAGE_22)
        self.check_special_symbol_input(*self.locator.FOURTH_PAGE_22, name=N.FOURTH_PAGE_22)
        self.check_letter_input(*self.locator.FOURTH_PAGE_22, name=N.FOURTH_PAGE_22)

        self.max_symbol_15_input(*self.locator.FOURTH_PAGE_24, name=N.FOURTH_PAGE_24)
        self.check_zero_value_input(*self.locator.FOURTH_PAGE_24, name=N.FOURTH_PAGE_24)
        self.check_special_symbol_input(*self.locator.FOURTH_PAGE_24, name=N.FOURTH_PAGE_24)
        self.check_letter_input(*self.locator.FOURTH_PAGE_24, name=N.FOURTH_PAGE_24)

        self.max_symbol_15_input(*self.locator.FOURTH_PAGE_25_I, name=N.FOURTH_PAGE_25_I)
        self.check_zero_value_input(*self.locator.FOURTH_PAGE_25_I, name=N.FOURTH_PAGE_25_I)
        self.check_special_symbol_input(*self.locator.FOURTH_PAGE_25_I, name=N.FOURTH_PAGE_25_I)
        self.check_letter_input(*self.locator.FOURTH_PAGE_25_I, name=N.FOURTH_PAGE_25_I)

        self.max_symbol_15_input(*self.locator.FOURTH_PAGE_25_II, name=N.FOURTH_PAGE_25_II)
        self.check_zero_value_input(*self.locator.FOURTH_PAGE_25_II, name=N.FOURTH_PAGE_25_II)
        self.check_special_symbol_input(*self.locator.FOURTH_PAGE_25_II, name=N.FOURTH_PAGE_25_II)
        self.check_letter_input(*self.locator.FOURTH_PAGE_25_II, name=N.FOURTH_PAGE_25_II)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.FOURTH_PAGE_25_III, name=N.FOURTH_PAGE_25_III)
        self.check_zero_value_input(*self.locator.FOURTH_PAGE_25_III, name=N.FOURTH_PAGE_25_III)
        self.check_special_symbol_input(*self.locator.FOURTH_PAGE_25_III, name=N.FOURTH_PAGE_25_III)
        self.check_letter_input(*self.locator.FOURTH_PAGE_25_III, name=N.FOURTH_PAGE_25_III)
        self.find_element(*self.locator.AFTER).click()

    def fifth_page_validation(self):
        sleep(1)
        self.max_symbol_15_input(*self.locator.FIFTH_PAGE_33_I, name=N.FIFTH_PAGE_33_I)
        self.check_zero_value_input(*self.locator.FIFTH_PAGE_33_I, name=N.FIFTH_PAGE_33_I)
        self.check_special_symbol_input(*self.locator.FIFTH_PAGE_33_I, name=N.FIFTH_PAGE_33_I)
        self.check_letter_input(*self.locator.FIFTH_PAGE_33_I, name=N.FIFTH_PAGE_33_I)

        self.max_symbol_15_input(*self.locator.FIFTH_PAGE_33_II, name=N.FIFTH_PAGE_33_II)
        self.check_zero_value_input(*self.locator.FIFTH_PAGE_33_II, name=N.FIFTH_PAGE_33_II)
        self.check_special_symbol_input(*self.locator.FIFTH_PAGE_33_II, name=N.FIFTH_PAGE_33_II)
        self.check_letter_input(*self.locator.FIFTH_PAGE_33_II, name=N.FIFTH_PAGE_33_II)

        self.max_symbol_15_input(*self.locator.FIFTH_PAGE_35, name=N.FIFTH_PAGE_35)
        self.check_zero_value_input(*self.locator.FIFTH_PAGE_35, name=N.FIFTH_PAGE_35)
        self.check_special_symbol_input(*self.locator.FIFTH_PAGE_35, name=N.FIFTH_PAGE_35)
        self.check_letter_input(*self.locator.FIFTH_PAGE_35, name=N.FIFTH_PAGE_35)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.FIFTH_PAGE_37, name=N.FIFTH_PAGE_37)
        self.check_zero_value_input(*self.locator.FIFTH_PAGE_37, name=N.FIFTH_PAGE_37)
        self.check_special_symbol_input(*self.locator.FIFTH_PAGE_37, name=N.FIFTH_PAGE_37)
        self.check_letter_input(*self.locator.FIFTH_PAGE_37, name=N.FIFTH_PAGE_37)

        self.max_symbol_15_input(*self.locator.FIFTH_PAGE_38, name=N.FIFTH_PAGE_38)
        self.check_zero_value_input(*self.locator.FIFTH_PAGE_38, name=N.FIFTH_PAGE_38)
        self.check_special_symbol_input(*self.locator.FIFTH_PAGE_38, name=N.FIFTH_PAGE_38)
        self.check_letter_input(*self.locator.FIFTH_PAGE_38, name=N.FIFTH_PAGE_38)
        self.find_element(*self.locator.AFTER).click()

    def sixth_page_validation(self):
        sleep(1)
        self.scroll('500')
        self.max_symbol_15_input(*self.locator.SIXTH_PAGE_43, name=N.SIXTH_PAGE_43)
        self.check_zero_value_input(*self.locator.SIXTH_PAGE_43, name=N.SIXTH_PAGE_43)
        self.check_special_symbol_input(*self.locator.SIXTH_PAGE_43, name=N.SIXTH_PAGE_43)
        self.check_letter_input(*self.locator.SIXTH_PAGE_43, name=N.SIXTH_PAGE_43)

        self.max_symbol_15_input(*self.locator.SIXTH_PAGE_44, name=N.SIXTH_PAGE_44)
        self.check_zero_value_input(*self.locator.SIXTH_PAGE_44, name=N.SIXTH_PAGE_44)
        self.check_special_symbol_input(*self.locator.SIXTH_PAGE_44, name=N.SIXTH_PAGE_44)
        self.check_letter_input(*self.locator.SIXTH_PAGE_44, name=N.SIXTH_PAGE_44)

        self.find_element(*self.locator.AFTER).click()

    def app_1_validation(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_12_input(*self.locator.FIRST_APP_B, name=N.FIRST_APP_B)
        self.check_zero_value_input(*self.locator.FIRST_APP_B, name=N.FIRST_APP_B)
        self.check_special_symbol_input(*self.locator.FIRST_APP_B, name=N.FIRST_APP_B)
        self.check_letter_input(*self.locator.FIRST_APP_B, name=N.FIRST_APP_B)
        self.find_element(*self.locator.FIRST_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.FIRST_APP_C_SELECT).click()
        self.find_element(*self.locator.FIRST_APP_D).send_keys('1234567890123456789')
        self.check_zero_value_input(*self.locator.FIRST_APP_D, name=N.FIRST_APP_D)
        self.check_special_symbol_input(*self.locator.FIRST_APP_D, name=N.FIRST_APP_D)
        self.check_letter_input(*self.locator.FIRST_APP_D, name=N.FIRST_APP_D)
        self.find_element(*self.locator.FIRST_APP_E).click()
        sleep(0.3)
        self.find_element(*self.locator.FIRST_APP_E_SELECT).click()
        self.max_symbol_15_input(*self.locator.FIRST_APP_F, name=N.FIRST_APP_F)
        self.check_zero_value_input(*self.locator.FIRST_APP_F, name=N.FIRST_APP_F)
        self.check_special_symbol_input(*self.locator.FIRST_APP_F, name=N.FIRST_APP_F)
        self.check_letter_input(*self.locator.FIRST_APP_F, name=N.FIRST_APP_F)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_2_validation(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.SECOND_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_C_SELECT).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_D).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_D_SELECT).click()
        self.max_symbol_15_input(*self.locator.SECOND_APP_E, name=N.SECOND_APP_E)
        self.check_zero_value_input(*self.locator.SECOND_APP_E, name=N.SECOND_APP_E)
        self.check_special_symbol_input(*self.locator.SECOND_APP_E, name=N.SECOND_APP_E)
        self.check_letter_input(*self.locator.SECOND_APP_E, name=N.SECOND_APP_E)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_3_validation(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(1)
        self.find_element(*self.locator.THIRD_APP_B).click()
        sleep(0.5)
        self.find_element(*self.locator.THIRD_APP_B_SELECT).click()
        self.find_element(*self.locator.THIRD_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_C_SELECT).click()
        self.find_element(*self.locator.THIRD_APP_D).click()
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_D_SELECT).click()

        self.max_symbol_15_input(*self.locator.THIRD_APP_E, name=N.THIRD_APP_E)
        self.check_zero_value_input(*self.locator.THIRD_APP_E, name=N.THIRD_APP_E)
        self.check_special_symbol_input(*self.locator.THIRD_APP_E, name=N.THIRD_APP_E)
        self.check_letter_input(*self.locator.THIRD_APP_E, name=N.THIRD_APP_E)

        self.max_symbol_15_input(*self.locator.THIRD_APP_F, name=N.THIRD_APP_F)
        self.check_zero_value_input(*self.locator.THIRD_APP_F, name=N.THIRD_APP_F)
        self.check_special_symbol_input(*self.locator.THIRD_APP_F, name=N.THIRD_APP_F)
        self.check_letter_input(*self.locator.THIRD_APP_F, name=N.THIRD_APP_F)

        self.max_symbol_15_input(*self.locator.THIRD_APP_G, name=N.THIRD_APP_G)
        self.check_zero_value_input(*self.locator.THIRD_APP_G, name=N.THIRD_APP_G)
        self.check_special_symbol_input(*self.locator.THIRD_APP_G, name=N.THIRD_APP_G)
        self.check_letter_input(*self.locator.THIRD_APP_G, name=N.THIRD_APP_G)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_4_validation(self):
        sleep(1)
        self.find_element(*self.locator.FOURTH_APP_DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('800')
        self.find_element(*self.locator.CONTROL_TEXT).click()

        self.max_symbol_15_input(*self.locator.FOURTH_APP_1_I, name=N.FOURTH_APP_1_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_1_I, name=N.FOURTH_APP_1_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_1_I, name=N.FOURTH_APP_1_I)
        self.check_letter_input(*self.locator.FOURTH_APP_1_I, name=N.FOURTH_APP_1_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_1_II, name=N.FOURTH_APP_1_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_1_II, name=N.FOURTH_APP_1_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_1_II, name=N.FOURTH_APP_1_II)
        self.check_letter_input(*self.locator.FOURTH_APP_1_II, name=N.FOURTH_APP_1_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_1_III, name=N.FOURTH_APP_1_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_1_III, name=N.FOURTH_APP_1_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_1_III, name=N.FOURTH_APP_1_III)
        self.check_letter_input(*self.locator.FOURTH_APP_1_III, name=N.FOURTH_APP_1_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_1_IV, name=N.FOURTH_APP_1_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_1_IV, name=N.FOURTH_APP_1_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_1_IV, name=N.FOURTH_APP_1_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_1_IV, name=N.FOURTH_APP_1_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_2_I, name=N.FOURTH_APP_2_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_2_I, name=N.FOURTH_APP_2_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_2_I, name=N.FOURTH_APP_2_I)
        self.check_letter_input(*self.locator.FOURTH_APP_2_I, name=N.FOURTH_APP_2_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_2_II, name=N.FOURTH_APP_2_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_2_II, name=N.FOURTH_APP_2_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_2_II, name=N.FOURTH_APP_2_II)
        self.check_letter_input(*self.locator.FOURTH_APP_2_II, name=N.FOURTH_APP_2_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_2_III, name=N.FOURTH_APP_2_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_2_III, name=N.FOURTH_APP_2_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_2_III, name=N.FOURTH_APP_2_III)
        self.check_letter_input(*self.locator.FOURTH_APP_2_III, name=N.FOURTH_APP_2_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_2_IV, name=N.FOURTH_APP_2_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_2_IV, name=N.FOURTH_APP_2_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_2_IV, name=N.FOURTH_APP_2_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_2_IV, name=N.FOURTH_APP_2_IV)
        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FOURTH_APP_3_I, name=N.FOURTH_APP_3_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_3_I, name=N.FOURTH_APP_3_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_3_I, name=N.FOURTH_APP_3_I)
        self.check_letter_input(*self.locator.FOURTH_APP_3_I, name=N.FOURTH_APP_3_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_3_II, name=N.FOURTH_APP_3_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_3_II, name=N.FOURTH_APP_3_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_3_II, name=N.FOURTH_APP_3_II)
        self.check_letter_input(*self.locator.FOURTH_APP_3_II, name=N.FOURTH_APP_3_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_3_III, name=N.FOURTH_APP_3_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_3_III, name=N.FOURTH_APP_3_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_3_III, name=N.FOURTH_APP_3_III)
        self.check_letter_input(*self.locator.FOURTH_APP_3_III, name=N.FOURTH_APP_3_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_3_IV, name=N.FOURTH_APP_3_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_3_IV, name=N.FOURTH_APP_3_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_3_IV, name=N.FOURTH_APP_3_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_3_IV, name=N.FOURTH_APP_3_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_4_I, name=N.FOURTH_APP_4_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_4_I, name=N.FOURTH_APP_4_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_4_I, name=N.FOURTH_APP_4_I)
        self.check_letter_input(*self.locator.FOURTH_APP_4_I, name=N.FOURTH_APP_4_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_4_II, name=N.FOURTH_APP_4_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_4_II, name=N.FOURTH_APP_4_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_4_II, name=N.FOURTH_APP_4_II)
        self.check_letter_input(*self.locator.FOURTH_APP_4_II, name=N.FOURTH_APP_4_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_4_III, name=N.FOURTH_APP_4_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_4_III, name=N.FOURTH_APP_4_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_4_III, name=N.FOURTH_APP_4_III)
        self.check_letter_input(*self.locator.FOURTH_APP_4_III, name=N.FOURTH_APP_4_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_4_IV, name=N.FOURTH_APP_4_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_4_IV, name=N.FOURTH_APP_4_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_4_IV, name=N.FOURTH_APP_4_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_4_IV, name=N.FOURTH_APP_4_IV)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FOURTH_APP_5_I, name=N.FOURTH_APP_5_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_5_I, name=N.FOURTH_APP_5_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_5_I, name=N.FOURTH_APP_5_I)
        self.check_letter_input(*self.locator.FOURTH_APP_5_I, name=N.FOURTH_APP_5_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_5_II, name=N.FOURTH_APP_5_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_5_II, name=N.FOURTH_APP_5_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_5_II, name=N.FOURTH_APP_5_II)
        self.check_letter_input(*self.locator.FOURTH_APP_5_II, name=N.FOURTH_APP_5_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_5_III, name=N.FOURTH_APP_5_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_5_III, name=N.FOURTH_APP_5_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_5_III, name=N.FOURTH_APP_5_III)
        self.check_letter_input(*self.locator.FOURTH_APP_5_III, name=N.FOURTH_APP_5_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_5_IV, name=N.FOURTH_APP_5_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_5_IV, name=N.FOURTH_APP_5_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_5_IV, name=N.FOURTH_APP_5_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_5_IV, name=N.FOURTH_APP_5_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_6_I, name=N.FOURTH_APP_6_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_6_I, name=N.FOURTH_APP_6_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_6_I, name=N.FOURTH_APP_6_I)
        self.check_letter_input(*self.locator.FOURTH_APP_6_I, name=N.FOURTH_APP_6_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_6_II, name=N.FOURTH_APP_6_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_6_II, name=N.FOURTH_APP_6_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_6_II, name=N.FOURTH_APP_6_II)
        self.check_letter_input(*self.locator.FOURTH_APP_6_II, name=N.FOURTH_APP_6_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_6_III, name=N.FOURTH_APP_6_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_6_III, name=N.FOURTH_APP_6_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_6_III, name=N.FOURTH_APP_6_III)
        self.check_letter_input(*self.locator.FOURTH_APP_6_III, name=N.FOURTH_APP_6_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_6_IV, name=N.FOURTH_APP_6_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_6_IV, name=N.FOURTH_APP_6_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_6_IV, name=N.FOURTH_APP_6_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_6_IV, name=N.FOURTH_APP_6_IV)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FOURTH_APP_7_I, name=N.FOURTH_APP_7_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_7_I, name=N.FOURTH_APP_7_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_7_I, name=N.FOURTH_APP_7_I)
        self.check_letter_input(*self.locator.FOURTH_APP_7_I, name=N.FOURTH_APP_7_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_7_II, name=N.FOURTH_APP_7_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_7_II, name=N.FOURTH_APP_7_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_7_II, name=N.FOURTH_APP_7_II)
        self.check_letter_input(*self.locator.FOURTH_APP_7_II, name=N.FOURTH_APP_7_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_7_III, name=N.FOURTH_APP_7_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_7_III, name=N.FOURTH_APP_7_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_7_III, name=N.FOURTH_APP_7_III)
        self.check_letter_input(*self.locator.FOURTH_APP_7_III, name=N.FOURTH_APP_7_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_7_IV, name=N.FOURTH_APP_7_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_7_IV, name=N.FOURTH_APP_7_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_7_IV, name=N.FOURTH_APP_7_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_7_IV, name=N.FOURTH_APP_7_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_8_I, name=N.FOURTH_APP_8_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_8_I, name=N.FOURTH_APP_8_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_8_I, name=N.FOURTH_APP_8_I)
        self.check_letter_input(*self.locator.FOURTH_APP_8_I, name=N.FOURTH_APP_8_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_8_II, name=N.FOURTH_APP_8_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_8_II, name=N.FOURTH_APP_8_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_8_II, name=N.FOURTH_APP_8_II)
        self.check_letter_input(*self.locator.FOURTH_APP_8_II, name=N.FOURTH_APP_8_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_8_III, name=N.FOURTH_APP_8_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_8_III, name=N.FOURTH_APP_8_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_8_III, name=N.FOURTH_APP_8_III)
        self.check_letter_input(*self.locator.FOURTH_APP_8_III, name=N.FOURTH_APP_8_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_8_IV, name=N.FOURTH_APP_8_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_8_IV, name=N.FOURTH_APP_8_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_8_IV, name=N.FOURTH_APP_8_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_8_IV, name=N.FOURTH_APP_8_IV)

        self.scroll('500')

        self.max_symbol_15_input(*self.locator.FOURTH_APP_9_I, name=N.FOURTH_APP_9_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_9_I, name=N.FOURTH_APP_9_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_9_I, name=N.FOURTH_APP_9_I)
        self.check_letter_input(*self.locator.FOURTH_APP_9_I, name=N.FOURTH_APP_9_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_9_II, name=N.FOURTH_APP_9_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_9_II, name=N.FOURTH_APP_9_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_9_II, name=N.FOURTH_APP_9_II)
        self.check_letter_input(*self.locator.FOURTH_APP_9_II, name=N.FOURTH_APP_9_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_9_III, name=N.FOURTH_APP_9_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_9_III, name=N.FOURTH_APP_9_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_9_III, name=N.FOURTH_APP_9_III)
        self.check_letter_input(*self.locator.FOURTH_APP_9_III, name=N.FOURTH_APP_9_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_9_IV, name=N.FOURTH_APP_9_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_9_IV, name=N.FOURTH_APP_9_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_9_IV, name=N.FOURTH_APP_9_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_9_IV, name=N.FOURTH_APP_9_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_10_I, name=N.FOURTH_APP_10_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_10_I, name=N.FOURTH_APP_10_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_10_I, name=N.FOURTH_APP_10_I)
        self.check_letter_input(*self.locator.FOURTH_APP_10_I, name=N.FOURTH_APP_10_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_10_II, name=N.FOURTH_APP_10_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_10_II, name=N.FOURTH_APP_10_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_10_II, name=N.FOURTH_APP_10_II)
        self.check_letter_input(*self.locator.FOURTH_APP_10_II, name=N.FOURTH_APP_10_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_10_III, name=N.FOURTH_APP_10_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_10_III, name=N.FOURTH_APP_10_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_10_III, name=N.FOURTH_APP_10_III)
        self.check_letter_input(*self.locator.FOURTH_APP_10_III, name=N.FOURTH_APP_10_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_10_IV, name=N.FOURTH_APP_10_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_10_IV, name=N.FOURTH_APP_10_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_10_IV, name=N.FOURTH_APP_10_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_10_IV, name=N.FOURTH_APP_10_IV)

        self.scroll('600')

        self.max_symbol_15_input(*self.locator.FOURTH_APP_11_I, name=N.FOURTH_APP_11_I)
        self.check_zero_value_input(*self.locator.FOURTH_APP_11_I, name=N.FOURTH_APP_11_I)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_11_I, name=N.FOURTH_APP_11_I)
        self.check_letter_input(*self.locator.FOURTH_APP_11_I, name=N.FOURTH_APP_11_I)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_11_II, name=N.FOURTH_APP_11_II)
        self.check_zero_value_input(*self.locator.FOURTH_APP_11_II, name=N.FOURTH_APP_11_II)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_11_II, name=N.FOURTH_APP_11_II)
        self.check_letter_input(*self.locator.FOURTH_APP_11_II, name=N.FOURTH_APP_11_II)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_11_III, name=N.FOURTH_APP_11_III)
        self.check_zero_value_input(*self.locator.FOURTH_APP_11_III, name=N.FOURTH_APP_11_III)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_11_III, name=N.FOURTH_APP_11_III)
        self.check_letter_input(*self.locator.FOURTH_APP_11_III, name=N.FOURTH_APP_11_III)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_11_IV, name=N.FOURTH_APP_11_IV)
        self.check_zero_value_input(*self.locator.FOURTH_APP_11_IV, name=N.FOURTH_APP_11_IV)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_11_IV, name=N.FOURTH_APP_11_IV)
        self.check_letter_input(*self.locator.FOURTH_APP_11_IV, name=N.FOURTH_APP_11_IV)

        self.max_symbol_15_input(*self.locator.FOURTH_APP_12, name=N.FOURTH_APP_12)
        self.check_zero_value_input(*self.locator.FOURTH_APP_12, name=N.FOURTH_APP_12)
        self.check_special_symbol_input(*self.locator.FOURTH_APP_12, name=N.FOURTH_APP_12)
        self.check_letter_input(*self.locator.FOURTH_APP_12, name=N.FOURTH_APP_12)
        self.find_element(*self.locator.AFTER).click()

    def app_5_validation(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.FIFTH_APP_B).send_keys('1d\][')
        sleep(0.3)
        assert '1d\][' in self.browser.page_source
        self.find_element(*self.locator.FIFTH_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.FIFTH_APP_C_SELECT).click()
        self.find_element(*self.locator.FIFTH_APP_D).send_keys('12345678901234567')
        sleep(0.3)
        assert '1234567890123456' in self.browser.page_source
        self.check_zero_value_input(*self.locator.FIFTH_APP_D, name=N.FIFTH_APP_D)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_D, name=N.FIFTH_APP_D)
        self.check_letter_input(*self.locator.FIFTH_APP_D, name=N.FIFTH_APP_D)

        self.find_element(*self.locator.FIFTH_APP_E).send_keys('1,2345678901234567')
        sleep(0.3)
        #assert '1,2345' in self.browser.page_source
        self.check_zero_value_input(*self.locator.FIFTH_APP_E, name=N.FIFTH_APP_E)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_E, name=N.FIFTH_APP_E)
        self.check_letter_input(*self.locator.FIFTH_APP_E, name=N.FIFTH_APP_E)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_G, name=N.FIFTH_APP_G)
        self.check_zero_value_input(*self.locator.FIFTH_APP_G, name=N.FIFTH_APP_G)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_G, name=N.FIFTH_APP_G)
        self.check_letter_input(*self.locator.FIFTH_APP_G, name=N.FIFTH_APP_G)

        element = self.browser.find_element_by_xpath('//*[text()="Добавить"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_H, name=N.FIFTH_APP_H)
        self.check_zero_value_input(*self.locator.FIFTH_APP_H, name=N.FIFTH_APP_H)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_H, name=N.FIFTH_APP_H)
        self.check_letter_input(*self.locator.FIFTH_APP_H, name=N.FIFTH_APP_H)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_I, name=N.FIFTH_APP_I)
        self.check_zero_value_input(*self.locator.FIFTH_APP_I, name=N.FIFTH_APP_I)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_I, name=N.FIFTH_APP_I)
        self.check_letter_input(*self.locator.FIFTH_APP_I, name=N.FIFTH_APP_I)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_J, name=N.FIFTH_APP_J)
        self.check_zero_value_input(*self.locator.FIFTH_APP_J, name=N.FIFTH_APP_J)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_J, name=N.FIFTH_APP_J)
        self.check_letter_input(*self.locator.FIFTH_APP_J, name=N.FIFTH_APP_J)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_K, name=N.FIFTH_APP_K)
        self.check_zero_value_input(*self.locator.FIFTH_APP_K, name=N.FIFTH_APP_K)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_K, name=N.FIFTH_APP_K)
        self.check_letter_input(*self.locator.FIFTH_APP_K, name=N.FIFTH_APP_K)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_L, name=N.FIFTH_APP_L)
        self.check_zero_value_input(*self.locator.FIFTH_APP_L, name=N.FIFTH_APP_L)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_L, name=N.FIFTH_APP_L)
        self.check_letter_input(*self.locator.FIFTH_APP_L, name=N.FIFTH_APP_L)

        self.max_symbol_12_input(*self.locator.FIFTH_APP_M, name=N.FIFTH_APP_M)
        self.check_zero_value_input(*self.locator.FIFTH_APP_M, name=N.FIFTH_APP_M)
        self.check_special_symbol_input(*self.locator.FIFTH_APP_M, name=N.FIFTH_APP_M)
        self.check_letter_input(*self.locator.FIFTH_APP_M, name=N.FIFTH_APP_M)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()