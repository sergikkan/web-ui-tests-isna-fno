from locators.fno_220_locators import FNO220Locators
from browser_interaction import BasePage
import allure
from time import sleep


class FNO220Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO220Locators

    def first_page(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        sleep(0.3)
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator.RESIDENTION).click()
        sleep(0.3)
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        self.find_element(*self.locator.RESIDENTION_CODE).click()
        sleep(0.3)
        self.find_element(*self.locator.RESIDENTION_CODE_SELECT).click()
        self.find_element(*self.locator.TAX_NUMBER).send_keys('231213312231213312231213312')
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APPS_SELECT_ALL).click()
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        sleep(0.3)
        self.find_element(*self.locator.AFTER).click()

    def second_page(self):
        sleep(1)
        self.find_element(*self.locator.INCOME_1).send_keys('21')
        self.find_element(*self.locator.INCOME_2).send_keys('22')
        self.find_element(*self.locator.INCOME_3).send_keys('23')
        self.scroll('500')
        self.find_element(*self.locator.INCOME_5).send_keys('25')
        self.find_element(*self.locator.INCOME_6).send_keys('26')
        self.find_element(*self.locator.INCOME_7_I).send_keys('271')
        self.find_element(*self.locator.INCOME_7_II).send_keys('272')
        self.scroll('400')
        self.find_element(*self.locator.INCOME_8).send_keys('8')
        self.find_element(*self.locator.INCOME_9).send_keys('9')
        self.find_element(*self.locator.AFTER).click()

    def third_page(self):
        sleep(1)
        self.find_element(*self.locator.DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('800')
        self.find_element(*self.locator.STOCK_1).send_keys('31')
        self.find_element(*self.locator.STOCK_2).send_keys('32')
        self.find_element(*self.locator.STOCK_3_A).send_keys('331')
        self.find_element(*self.locator.STOCK_3_B).send_keys('332')
        self.find_element(*self.locator.STOCK_3_C).send_keys('333')
        self.find_element(*self.locator.STOCK_3_D).send_keys('334')
        self.find_element(*self.locator.STOCK_3_E).send_keys('335')
        self.find_element(*self.locator.STOCK_3_F).send_keys('336')
        self.scroll('500')
        self.find_element(*self.locator.STOCK_3_G).send_keys('335')
        self.find_element(*self.locator.STOCK_3_H).send_keys('336')
        self.find_element(*self.locator.STOCK_4).send_keys('34')
        self.find_element(*self.locator.STOCK_5).send_keys('35')
        self.find_element(*self.locator.STOCK_6).send_keys('36')
        self.find_element(*self.locator.STOCK_7).send_keys('37')
        self.scroll('500')
        self.find_element(*self.locator.STOCK_8).send_keys('38')
        self.find_element(*self.locator.STOCK_9).send_keys('39')
        self.find_element(*self.locator.THIRD_PAGE_12).send_keys('312')
        self.find_element(*self.locator.THIRD_PAGE_13).send_keys('313')
        self.scroll('500')
        self.find_element(*self.locator.THIRD_PAGE_14).send_keys('314')
        self.find_element(*self.locator.THIRD_PAGE_15).send_keys('315')
        self.find_element(*self.locator.THIRD_PAGE_16).send_keys('316')
        self.find_element(*self.locator.THIRD_PAGE_17).send_keys('317')
        self.find_element(*self.locator.THIRD_PAGE_18).send_keys('318')
        self.scroll('500')
        self.find_element(*self.locator.THIRD_PAGE_20).send_keys('320')
        self.find_element(*self.locator.AFTER).click()

    def fourth_page(self):
        sleep(1)
        self.find_element(*self.locator.DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('500')
        self.find_element(*self.locator.FOURTH_PAGE_22).send_keys('422')
        self.find_element(*self.locator.FOURTH_PAGE_24).send_keys('424')
        self.find_element(*self.locator.FOURTH_PAGE_25_I).send_keys('4251')
        self.find_element(*self.locator.FOURTH_PAGE_25_II).send_keys('4252')
        self.scroll('500')
        self.find_element(*self.locator.FOURTH_PAGE_25_III).send_keys('4253')
        self.find_element(*self.locator.AFTER).click()

    def fifth_page(self):
        sleep(1)
        self.find_element(*self.locator.FIFTH_PAGE_33_I).send_keys('5331')
        self.find_element(*self.locator.FIFTH_PAGE_33_I).send_keys('5332')
        self.find_element(*self.locator.FIFTH_PAGE_35).send_keys('535')
        self.scroll('500')
        self.find_element(*self.locator.FIFTH_PAGE_37).send_keys('537')
        self.find_element(*self.locator.FIFTH_PAGE_38).send_keys('538')
        self.find_element(*self.locator.AFTER).click()

    def sixth_page(self):
        sleep(1)
        self.scroll('500')
        #self.find_element(*self.locator.SIXTH_PAGE_42_III).send_keys('6423')
        #self.find_element(*self.locator.SIXTH_PAGE_42_IV).send_keys('6424')
        #self.find_element(*self.locator.SIXTH_PAGE_42_V).send_keys('6425')
        self.find_element(*self.locator.SIXTH_PAGE_43).send_keys('643')
        self.find_element(*self.locator.SIXTH_PAGE_44).send_keys('644')
        self.find_element(*self.locator.AFTER).click()

    def app_1(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.FIRST_APP_B).send_keys('123456789012')
        self.find_element(*self.locator.FIRST_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.FIRST_APP_C_SELECT).click()
        self.find_element(*self.locator.FIRST_APP_D).send_keys('4')
        self.find_element(*self.locator.FIRST_APP_E).click()
        sleep(0.3)
        self.find_element(*self.locator.FIRST_APP_E_SELECT).click()
        self.find_element(*self.locator.FIRST_APP_F).send_keys('6')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_2(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(1)
        self.find_element(*self.locator.SECOND_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_C_SELECT).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_D).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_APP_D_SELECT).click()
        self.find_element(*self.locator.SECOND_APP_E).send_keys('5')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_3(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(1)
        self.find_element(*self.locator.THIRD_APP_B).click()
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_B_SELECT).click()
        self.find_element(*self.locator.THIRD_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_C_SELECT).click()
        self.find_element(*self.locator.THIRD_APP_D).click()
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_D_SELECT).click()
        self.find_element(*self.locator.THIRD_APP_E).send_keys('5')
        self.find_element(*self.locator.THIRD_APP_F).send_keys('6')
        self.find_element(*self.locator.THIRD_APP_G).send_keys('7')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_4(self):
        sleep(1)
        self.find_element(*self.locator.FOURTH_APP_DEDUCTIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.DEDUCTIONS_SELECT_ALL).click()
        self.scroll('800')
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.FOURTH_APP_1_I).send_keys('411')
        self.find_element(*self.locator.FOURTH_APP_1_II).send_keys('412')
        self.find_element(*self.locator.FOURTH_APP_1_III).send_keys('413')
        self.find_element(*self.locator.FOURTH_APP_1_IV).send_keys('414')

        self.find_element(*self.locator.FOURTH_APP_2_I).send_keys('421')
        self.find_element(*self.locator.FOURTH_APP_2_II).send_keys('422')
        self.find_element(*self.locator.FOURTH_APP_2_III).send_keys('423')
        self.find_element(*self.locator.FOURTH_APP_2_IV).send_keys('424')
        self.scroll('600')
        self.find_element(*self.locator.FOURTH_APP_3_I).send_keys('431')
        self.find_element(*self.locator.FOURTH_APP_3_II).send_keys('432')
        self.find_element(*self.locator.FOURTH_APP_3_III).send_keys('433')
        self.find_element(*self.locator.FOURTH_APP_3_IV).send_keys('434')

        self.find_element(*self.locator.FOURTH_APP_4_I).send_keys('441')
        self.find_element(*self.locator.FOURTH_APP_4_II).send_keys('442')
        self.find_element(*self.locator.FOURTH_APP_4_III).send_keys('443')
        self.find_element(*self.locator.FOURTH_APP_4_IV).send_keys('444')
        self.scroll('600')
        self.find_element(*self.locator.FOURTH_APP_5_I).send_keys('451')
        self.find_element(*self.locator.FOURTH_APP_5_II).send_keys('452')
        self.find_element(*self.locator.FOURTH_APP_5_III).send_keys('453')
        self.find_element(*self.locator.FOURTH_APP_5_IV).send_keys('454')

        self.find_element(*self.locator.FOURTH_APP_6_I).send_keys('461')
        self.find_element(*self.locator.FOURTH_APP_6_II).send_keys('462')
        self.find_element(*self.locator.FOURTH_APP_6_III).send_keys('463')
        self.find_element(*self.locator.FOURTH_APP_6_IV).send_keys('464')
        self.scroll('600')
        self.find_element(*self.locator.FOURTH_APP_7_I).send_keys('471')
        self.find_element(*self.locator.FOURTH_APP_7_II).send_keys('472')
        self.find_element(*self.locator.FOURTH_APP_7_III).send_keys('473')
        self.find_element(*self.locator.FOURTH_APP_7_IV).send_keys('474')

        self.find_element(*self.locator.FOURTH_APP_8_I).send_keys('481')
        self.find_element(*self.locator.FOURTH_APP_8_II).send_keys('482')
        self.find_element(*self.locator.FOURTH_APP_8_III).send_keys('483')
        self.find_element(*self.locator.FOURTH_APP_8_IV).send_keys('484')
        self.scroll('500')
        self.find_element(*self.locator.FOURTH_APP_9_I).send_keys('491')
        self.find_element(*self.locator.FOURTH_APP_9_II).send_keys('492')
        self.find_element(*self.locator.FOURTH_APP_9_III).send_keys('493')
        self.find_element(*self.locator.FOURTH_APP_9_IV).send_keys('494')

        self.find_element(*self.locator.FOURTH_APP_10_I).send_keys('4101')
        self.find_element(*self.locator.FOURTH_APP_10_II).send_keys('4102')
        self.find_element(*self.locator.FOURTH_APP_10_III).send_keys('4103')
        self.find_element(*self.locator.FOURTH_APP_10_IV).send_keys('4104')
        self.scroll('600')
        self.find_element(*self.locator.FOURTH_APP_11_I).send_keys('4111')
        self.find_element(*self.locator.FOURTH_APP_11_II).send_keys('4112')
        self.find_element(*self.locator.FOURTH_APP_11_III).send_keys('4113')
        self.find_element(*self.locator.FOURTH_APP_11_IV).send_keys('4114')

        self.find_element(*self.locator.FOURTH_APP_12).send_keys('412')
        self.find_element(*self.locator.AFTER).click()

    def app_5(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.FIFTH_APP_B).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_C).click()
        sleep(0.3)
        self.find_element(*self.locator.FIFTH_APP_C_SELECT).click()
        self.find_element(*self.locator.FIFTH_APP_F).click()
        sleep(0.3)
        self.find_element(*self.locator.FIFTH_APP_F_SELECT).click()
        self.find_element(*self.locator.FIFTH_APP_D).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_E).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_G).send_keys('1d\][')
        element = self.browser.find_element_by_xpath('//*[text()="????????????????"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.FIFTH_APP_H).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_I).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_J).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_K).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_L).send_keys('1d\][')
        self.find_element(*self.locator.FIFTH_APP_M).send_keys('1d\][')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()