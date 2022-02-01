from locators.fno_701_locators import FNO701Locators
from browser_interaction import BasePage
import allure
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium import webdriver


class FNO701Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO701Locators

    def check_tax_period_text(self):
        try:
            assert '701.00 Расчет текущих платежей по налогу на транспортные средства' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО701
    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.YEAR).click()
        sleep(0.5)
        self.find_element(*self.locator.SELECT_2021).click()
        sleep(2)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def first_page(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.NOTICE_NUMBER).send_keys('123zxc')
        self.find_element(*self.locator.NOTICE_DATE).click()
        sleep(0.3)
        self.find_element(*self.locator.NOTICE_DATE_SELECT).click()
        self.scroll('600')
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        sleep(0.3)
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT_2).click()
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_SELECT).click()
        self.find_element(*self.locator.AFTER).click()

    def app_1_and_third_page(self):
        sleep(1)
        self.find_element(*self.locator.TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.TYPE_SELECT).click()
        self.find_element(*self.locator.FIELD).send_keys('123zxc')
        self.scroll('600')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0101).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.APP_C).send_keys('123zxc')
        self.find_element(*self.locator.ADD).click()
        self.scroll('600')
        self.find_element(*self.locator.AFTER).click()
        assert '246' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

    def fourth_page(self):
        sleep(0.5)
        self.scroll('600')
        self.find_element(*self.locator.CONFIRMATION).click()
        sleep(0.5)
        self.find_element(*self.locator.FORM).click()
        sleep(3)