from locators.fno_421_locators import FNO_421_Locators
from browser_interaction import BasePage
import allure
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains


class FNO421Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO_421_Locators

    def check_tax_period_text(self):
        try:
            assert '421.00 Расчет акциза за структурное подразделение или объекты, связанные с налогообложением' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО400
    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.MONTH).click()
        element = self.browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[9]/div")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        self.find_element(*self.locator.MONTH_SELECT).click()
        self.find_element(*self.locator.YEAR).click()
        sleep(0.5)
        self.find_element(*self.locator.YEAR_SELECT).click()
        sleep(2)
        self.find_element(*self.locator.SEND_DOC).click()

    # Ниже первая страница
    # Заполнение информации о декларации
    def declaration_info(self):
        self.scroll('100')
        self.find_element(*self.locator.PAYMENT_TYPE).click()
        self.find_element(*self.locator.PAYMENT_TYPE_SELECT).click()
        sleep(0.5)
        #self.find_element(*self.locator.DATE).click()
        self.scroll('400')
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES_SELECT).click()
        sleep(1)
        self.find_element(*self.locator.EXCISE_CALC).click()
        self.find_element(*self.locator.EXCISE_CALC_SELECT).click()
        sleep(1)

    # Сведения о налогоплательщике
    def taxpayer_info(self):
        self.scroll('400')
        self.find_element(*self.locator.CODE1).click()
        self.find_element(*self.locator.CODE1_SELECT).click()
        #self.find_element(*self.locator.CODE2).click()
        #self.find_element(*self.locator.CODE2_SELECT).click()
        self.find_element(*self.locator.APPLICATIONS).click()
        sleep(1)
        self.find_element(*self.locator.APPLICATION_01).click()
        sleep(1)
        self.scroll('50000')
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        self.find_element(*self.locator.AFTER).click()

    def taxpayer_info2(self):
        self.scroll('400')
        self.find_element(*self.locator.CODE1).click()
        self.find_element(*self.locator.CODE1_SELECT).click()
        #self.find_element(*self.locator.CODE2).click()
        #self.find_element(*self.locator.CODE2_SELECT).click()
        self.find_element(*self.locator.APPLICATIONS).click()
        sleep(0.3)
        self.find_element(*self.locator.APPLICATION_02).click()
        self.scroll('50000')
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        self.find_element(*self.locator.AFTER).click()

    def taxpayer_info_three(self):
        self.scroll('400')
        self.find_element(*self.locator.CODE1).click()
        self.find_element(*self.locator.CODE1_SELECT).click()
        #self.find_element(*self.locator.CODE2).click()
        #self.find_element(*self.locator.CODE2_SELECT).click()
        self.find_element(*self.locator.APPLICATIONS).click()
        element = self.browser.find_element_by_xpath('//*[text()="Приложение 421.04  Облагаемые операции по бензину ('
                                                     'за исключением авиационного) и (или) дизельному топливу"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.APPLICATION_03).click()
        sleep(3)
        self.scroll('50000')
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        self.find_element(*self.locator.AFTER).click()

    def taxpayer_info4(self):
        self.scroll('400')
        self.find_element(*self.locator.CODE1).click()
        self.find_element(*self.locator.CODE1_SELECT).click()
        #self.find_element(*self.locator.CODE2).click()
        #self.find_element(*self.locator.CODE2_SELECT).click()
        self.find_element(*self.locator.APPLICATIONS).click()
        element = self.browser.find_element_by_xpath('//*[text()="Приложение 421.04  Облагаемые операции по бензину ('
                                                     'за исключением авиационного) и (или) дизельному топливу"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(0.5)
        self.find_element(*self.locator.APPLICATION_04).click()
        sleep(3)
        self.scroll('50000')
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        self.find_element(*self.locator.AFTER).click()

    def first_page(self):
        self.declaration_info()
        self.taxpayer_info()

    def first_page2(self):
        self.declaration_info()
        self.taxpayer_info2()

    def first_page3(self):
        self.declaration_info()
        self.taxpayer_info_three()

    def first_page4(self):
        self.declaration_info()
        self.taxpayer_info4()

    # 2 страница

    def app_1(self):
        self.scroll('500')
        self.find_element(*self.locator.LITER_1).send_keys('1')
        sleep(0.3)
        self.find_element(*self.locator.EXC_RATE_1).send_keys('10')
        sleep(0.3)
        self.find_element(*self.locator.LITER_1).send_keys('2')
        sleep(0.3)
        self.find_element(*self.locator.EXC_RATE_2).send_keys('50')
        sleep(0.3)
        self.scroll('500')
        self.find_element(*self.locator.WINE_LITER_1).send_keys('5')
        sleep(0.3)
        self.find_element(*self.locator.WINE_EXC_1).send_keys('6')
        sleep(0.3)
        self.find_element(*self.locator.WINE_LITER_2).send_keys('7')
        sleep(0.3)
        self.find_element(*self.locator.WINE_EXC_2).send_keys('3')
        self.find_element(*self.locator.AFTER).click()

    def third_page(self):
        self.scroll('1800')
        self.find_element(*self.locator.BUT_1).send_keys('7')
        self.find_element(*self.locator.BUT_2).send_keys('4')
        self.find_element(*self.locator.BUT_3).send_keys('6')
        self.find_element(*self.locator.BUT_4).send_keys('2')
        self.find_element(*self.locator.BUT_5).send_keys('1')
        self.find_element(*self.locator.BUT_6).send_keys('30')
        self.find_element(*self.locator.BUT_7).send_keys('40')
        self.find_element(*self.locator.BUT_8).send_keys('90')
        self.find_element(*self.locator.BUT_9).send_keys('10')
        self.find_element(*self.locator.BUT_10).send_keys('70')
        self.find_element(*self.locator.BUT_11).send_keys('20')
        self.find_element(*self.locator.BUT_12).send_keys('8')
        self.scroll('750')
        self.find_element(*self.locator.BUT_13).send_keys('100')
        self.find_element(*self.locator.BUT_14).send_keys('7')
        self.find_element(*self.locator.BUT_15).send_keys('45')
        self.find_element(*self.locator.BUT_16).send_keys('4')
        self.find_element(*self.locator.BUT_17).send_keys('8')
        self.find_element(*self.locator.BUT_18).send_keys('20')
        self.find_element(*self.locator.BUT_19).send_keys('25')
        self.find_element(*self.locator.BUT_20).send_keys('8')
        self.find_element(*self.locator.BUT_21).send_keys('30')
        self.find_element(*self.locator.BUT_22).send_keys('4')
        self.scroll('5000')
        self.find_element(*self.locator.AFTER).click()

    def fourth_page(self):
        self.scroll('400')
        #self.find_element(*self.locator.CODE_OGD).click()
        sleep(1)
        #self.find_element(*self.locator.CODE_OGD_SELECT).click()
        self.find_element(*self.locator.CONFIRM).click()
        sleep(2)
        self.find_element(*self.locator.FORM).click()

    def app_2(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.B).click()
        sleep(0.3)
        self.find_element(*self.locator.B_SELECT).click()
        sleep(0.3)
        self.find_element(*self.locator.C).click()
        self.find_element(*self.locator.C_SELECT).click()
        self.find_element(*self.locator.D).send_keys('5')
        self.find_element(*self.locator.E).send_keys('4')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_3(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.B).click()
        self.find_element(*self.locator.B_SELECT).click()
        self.find_element(*self.locator.C).send_keys('5')
        self.find_element(*self.locator.D).send_keys('2')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_4(self):
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_1).send_keys('111')
        sleep(0.3)
        self.find_element(*self.locator.EXC_R_1).send_keys('222')
        sleep(0.5)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_2).send_keys('111')
        self.find_element(*self.locator.EXC_R_2).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_3).send_keys('111')
        self.find_element(*self.locator.EXC_R_3).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_4).send_keys('111')
        self.find_element(*self.locator.EXC_R_4).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_5).send_keys('111')
        self.find_element(*self.locator.EXC_R_5).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_6).send_keys('111')
        self.find_element(*self.locator.EXC_R_6).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_7).send_keys('111')
        self.find_element(*self.locator.EXC_R_7).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_8).send_keys('111')
        self.find_element(*self.locator.EXC_R_8).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_9).send_keys('111')
        self.find_element(*self.locator.EXC_R_9).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_10).send_keys('111')
        self.find_element(*self.locator.EXC_R_10).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('800')
        self.find_element(*self.locator.TAX_BASE_11).send_keys('111')
        self.find_element(*self.locator.EXC_R_11).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_12).send_keys('111')
        self.find_element(*self.locator.EXC_R_12).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_13).send_keys('111')
        self.find_element(*self.locator.EXC_R_13).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_14).send_keys('111')
        self.find_element(*self.locator.EXC_R_14).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_15).send_keys('111')
        self.find_element(*self.locator.EXC_R_15).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_16).send_keys('111')
        self.find_element(*self.locator.EXC_R_16).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_17).send_keys('111')
        self.find_element(*self.locator.EXC_R_17).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_18).send_keys('111')
        self.find_element(*self.locator.EXC_R_18).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.TAX_BASE_19).send_keys('111')
        self.find_element(*self.locator.EXC_R_19).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.find_element(*self.locator.TAX_BASE_20).send_keys('111')
        self.find_element(*self.locator.EXC_R_20).send_keys('222')
        sleep(0.3)
        assert '24642' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.BUDG_QUAL_CODE).click()
        sleep(0.3)
        self.find_element(*self.locator.BUDG_QUAL_CODE_SELECT).click()
        self.find_element(*self.locator.VOL_EXC).send_keys('111')
        self.find_element(*self.locator.SUM_EXC).send_keys('222')
        self.find_element(*self.locator.VOL_EXC_2).send_keys('111')
        self.find_element(*self.locator.SUM_EXC_2).send_keys('222')
        self.find_element(*self.locator.BUDG_QUAL_CODE_2).click()
        sleep(0.3)
        self.find_element(*self.locator.BUDG_QUAL_CODE_2_SELECT).click()
        self.find_element(*self.locator.AFTER).click()