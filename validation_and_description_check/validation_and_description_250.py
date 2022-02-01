from browser_interaction import BasePage
from time import sleep
from locators.fno_250_locators import FNO250Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_250_locators import FNO250LocatorsName as N


class FNO250MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO250Locators

    def first_page_validation(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.max_symbol_20_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_zero_value_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_special_symbol_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.check_letter_input(*self.locator.NOTICE_NUMBER, name=N.NOTICE_NUMBER)
        self.scroll('600')
        self.find_element(*self.locator.RESIDENTION).click()
        sleep(0.5)
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        self.find_element(*self.locator.PHONE_NUMBER).send_keys('123456789')
        self.find_element(*self.locator.E_MAIL).send_keys('Test_test')
        sleep(0.5)
        assert 'Некорректный адрес электронной почты' in self.browser.page_source
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_9_input(*self.locator.FIRST_PAGE_C, name=N.FIRST_PAGE_C)
        self.check_zero_value_input(*self.locator.FIRST_PAGE_C, name=N.FIRST_PAGE_C)
        self.check_special_symbol_input(*self.locator.FIRST_PAGE_C, name=N.FIRST_PAGE_C)
        self.check_letter_input(*self.locator.FIRST_PAGE_C, name=N.FIRST_PAGE_C)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_1_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_1_B_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_B_1).clear()
        self.find_element(*self.locator.APP_1_D_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_D_1).clear()

        self.max_symbol_16_input(*self.locator.APP_1_E_1, name=N.APP_1_E_1)
        self.check_zero_value_input(*self.locator.APP_1_E_1, name=N.APP_1_E_1)
        self.check_special_symbol_input(*self.locator.APP_1_E_1, name=N.APP_1_E_1)
        self.check_letter_input(*self.locator.APP_1_E_1, name=N.APP_1_E_1)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_1_B_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_B_2).clear()

        self.find_element(*self.locator.APP_1_C_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_C_2).clear()

        self.find_element(*self.locator.APP_1_E_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_E_2).clear()

        self.find_element(*self.locator.APP_1_F_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_1_F_2).clear()

        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_2_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_2_B_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_2_B_1).clear()
        self.find_element(*self.locator.APP_2_C_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_2_C_1).clear()
        self.max_symbol_12_input(*self.locator.APP_2_F_1, name=N.APP_2_F_1)
        self.check_zero_value_input(*self.locator.APP_2_F_1, name=N.APP_2_F_1)
        self.check_special_symbol_input(*self.locator.APP_2_F_1, name=N.APP_2_F_1)
        self.check_letter_input(*self.locator.APP_2_F_1, name=N.APP_2_F_1)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_2_B_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_2_B_2).clear()
        self.find_element(*self.locator.APP_2_C_2).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_2_C_2).clear()
        self.max_symbol_3_input(*self.locator.APP_2_E_2, name=N.APP_2_E_2)
        self.check_zero_value_input(*self.locator.APP_2_E_2, name=N.APP_2_E_2)
        self.check_special_symbol_input(*self.locator.APP_2_E_2, name=N.APP_2_E_2)
        self.check_letter_input(*self.locator.APP_2_E_2, name=N.APP_2_E_2)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.find_element(*self.locator.AFTER).click()

    def app_3_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_3_B_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_3_B_1).clear()
        self.find_element(*self.locator.APP_3_C_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_3_C_1).clear()
        self.find_element(*self.locator.APP_3_E_1).send_keys('123zxc{}+_')
        sleep(0.3)
        assert '123zxc{}+_' in self.browser.page_source
        self.find_element(*self.locator.APP_3_E_1).clear()
        self.max_symbol_12_input(*self.locator.APP_3_G_1, name=N.APP_3_G_1)
        self.check_zero_value_input(*self.locator.APP_2_E_2, name=N.APP_3_G_1)
        self.check_special_symbol_input(*self.locator.APP_3_G_1, name=N.APP_3_G_1)
        self.check_letter_input(*self.locator.APP_3_G_1, name=N.APP_3_G_1)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_9_input(*self.locator.APP_3_B_2, name=N.APP_3_B_2)
        self.check_zero_value_input(*self.locator.APP_3_B_2, name=N.APP_3_B_2)
        self.check_special_symbol_input(*self.locator.APP_3_B_2, name=N.APP_3_B_2)
        self.check_letter_input(*self.locator.APP_3_B_2, name=N.APP_3_B_2)
        self.max_symbol_12_input(*self.locator.APP_3_E_2, name=N.APP_3_E_2)
        self.check_zero_value_input(*self.locator.APP_3_E_2, name=N.APP_3_E_2)
        self.check_special_symbol_input(*self.locator.APP_3_E_2, name=N.APP_3_E_2)
        self.check_letter_input(*self.locator.APP_3_E_2, name=N.APP_3_E_2)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def app_4_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_12_input(*self.locator.APP_4_B_1, name=N.APP_4_B_1)
        self.check_zero_value_input(*self.locator.APP_4_B_1, name=N.APP_4_B_1)
        self.check_special_symbol_input(*self.locator.APP_4_B_1, name=N.APP_4_B_1)
        self.check_letter_input(*self.locator.APP_4_B_1, name=N.APP_4_B_1)

        self.max_symbol_12_input(*self.locator.APP_4_E_1, name=N.APP_4_E_1)
        self.check_zero_value_input(*self.locator.APP_4_E_1, name=N.APP_4_E_1)
        self.check_special_symbol_input(*self.locator.APP_4_E_1, name=N.APP_4_E_1)
        self.check_letter_input(*self.locator.APP_4_E_1, name=N.APP_4_E_1)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.max_symbol_9_input(*self.locator.APP_4_B_2, name=N.APP_4_B_2)
        self.check_zero_value_input(*self.locator.APP_4_B_2, name=N.APP_4_B_2)
        self.check_special_symbol_input(*self.locator.APP_4_B_2, name=N.APP_4_B_2)
        self.check_letter_input(*self.locator.APP_4_B_2, name=N.APP_4_B_2)

        self.max_symbol_12_input(*self.locator.APP_4_E_2, name=N.APP_4_E_2)
        self.check_zero_value_input(*self.locator.APP_4_E_2, name=N.APP_4_E_2)
        self.check_special_symbol_input(*self.locator.APP_4_E_2, name=N.APP_4_E_2)
        self.check_letter_input(*self.locator.APP_4_E_2, name=N.APP_4_E_2)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def app_5_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.check_zero_value_input(*self.locator.APP_5_B_1, name=N.APP_5_B_1)
        self.check_special_symbol_input(*self.locator.APP_5_B_1, name=N.APP_5_B_1)
        self.check_letter_input(*self.locator.APP_5_B_1, name=N.APP_5_B_1)

        self.check_zero_value_input(*self.locator.APP_5_C_1, name=N.APP_5_C_1)
        self.check_special_symbol_input(*self.locator.APP_5_C_1, name=N.APP_5_C_1)
        self.check_letter_input(*self.locator.APP_5_C_1, name=N.APP_5_C_1)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()

        self.check_zero_value_input(*self.locator.APP_5_B_2, name=N.APP_5_B_2)
        self.check_special_symbol_input(*self.locator.APP_5_B_2, name=N.APP_5_B_2)
        self.check_letter_input(*self.locator.APP_5_B_2, name=N.APP_5_B_2)

        self.max_symbol_9_input(*self.locator.APP_5_C_2, name=N.APP_5_C_2)
        self.check_zero_value_input(*self.locator.APP_5_C_2, name=N.APP_5_C_2)
        self.check_special_symbol_input(*self.locator.APP_5_C_2, name=N.APP_5_C_2)
        self.check_letter_input(*self.locator.APP_5_C_2, name=N.APP_5_C_2)

        self.max_symbol_12_input(*self.locator.APP_5_F_2, name=N.APP_5_F_2)
        self.check_zero_value_input(*self.locator.APP_5_F_2, name=N.APP_5_F_2)
        self.check_special_symbol_input(*self.locator.APP_5_F_2, name=N.APP_5_F_2)
        self.check_letter_input(*self.locator.APP_5_F_2, name=N.APP_5_F_2)
        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def app_6_validation(self):
        self.scroll('400')
        self.find_element(*self.locator.ADD_STR).click()
        self.check_zero_value_input(*self.locator.APP_6_C_1, name=N.APP_6_C_1)
        self.check_special_symbol_input(*self.locator.APP_6_C_1, name=N.APP_6_C_1)
        self.check_letter_input(*self.locator.APP_6_C_1, name=N.APP_6_C_1)

        self.check_zero_value_input(*self.locator.APP_6_D_1, name=N.APP_6_D_1)
        self.check_special_symbol_input(*self.locator.APP_6_D_1, name=N.APP_6_D_1)
        self.check_letter_input(*self.locator.APP_6_D_1, name=N.APP_6_D_1)

        self.max_symbol_12_input(*self.locator.APP_6_G_1, name=N.APP_6_G_1)
        self.check_zero_value_input(*self.locator.APP_6_G_1, name=N.APP_6_G_1)
        self.check_special_symbol_input(*self.locator.APP_6_G_1, name=N.APP_6_G_1)
        self.check_letter_input(*self.locator.APP_6_G_1, name=N.APP_6_G_1)

        self.find_element(*self.locator.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()

        self.check_zero_value_input(*self.locator.APP_6_B_2, name=N.APP_6_B_2)
        self.check_special_symbol_input(*self.locator.APP_6_B_2, name=N.APP_6_B_2)
        self.check_letter_input(*self.locator.APP_6_B_2, name=N.APP_6_B_2)

        self.check_zero_value_input(*self.locator.APP_6_C_2, name=N.APP_6_C_2)
        self.check_special_symbol_input(*self.locator.APP_6_C_2, name=N.APP_6_C_2)
        self.check_letter_input(*self.locator.APP_6_C_2, name=N.APP_6_C_2)

        self.max_symbol_12_input(*self.locator.APP_6_D_2, name=N.APP_6_D_2)
        self.check_zero_value_input(*self.locator.APP_6_D_2, name=N.APP_6_D_2)
        self.check_special_symbol_input(*self.locator.APP_6_D_2, name=N.APP_6_D_2)
        self.check_letter_input(*self.locator.APP_6_D_2, name=N.APP_6_D_2)
