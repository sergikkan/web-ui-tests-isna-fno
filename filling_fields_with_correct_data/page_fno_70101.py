from browser_interaction import BasePage
from time import sleep
from locators.fno_70101_locators import FNO70101Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_70101_locators import FNO70101LocatorsName as N
import allure


class FNO70101Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO70101Locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        try:
            assert '701.01 701.01 Расчет текущих платежей по земельному налогу и налогу на имущество' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО860
    def select_date_tax_pay(self):
        self.find_element(*self.locator.YEAR_SELECT).click()
        self.find_element(*self.locator.SELECT_2021).click()
        sleep(0.5)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_date_tax_pay()

        '''Ниже первая страница'''

    # Первая страница
    def first_page(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT_1).click()
        self.find_element(*self.locator.NOTICE_NUMBER).send_keys('123zxc')
        self.find_element(*self.locator.NOTICE_DATE).click()
        self.find_element(*self.locator.NOTICE_DATE_SELECT).click()
        self.scroll('600')
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        sleep(0.3)
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT_2).click()
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def second_page(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_PAGE_A).click()
        sleep(0.3)
        self.find_element(*self.locator.SECOND_PAGE_A_SELECT).click()
        assert 'Земельный налог на земли населенных пунктов' in self.browser.page_source
        self.find_element(*self.locator.SECOND_PAGE_C).send_keys('123')
        self.find_element(*self.locator.SECOND_PAGE_D).send_keys('123')
        self.find_element(*self.locator.SECOND_PAGE_E).send_keys('123')
        self.find_element(*self.locator.SECOND_PAGE_F).send_keys('123')
        sleep(0.3)
        assert '492' in self.browser.page_source
        self.find_element(*self.locator.ADD).click()
        assert '104302' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

    def app_1(self):
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0305).click()
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.APP_C).send_keys('123')
        self.find_element(*self.locator.APP_D).send_keys('123')
        self.find_element(*self.locator.APP_E).send_keys('123')
        self.find_element(*self.locator.APP_F).send_keys('123')
        sleep(0.5)
        assert '492' in self.browser.page_source
        self.find_element(*self.locator.ADD).click()
        sleep(0.5)
        self.find_element(*self.locator.AFTER).click()

    def end_page(self):
        self.scroll('500')
        self.find_element(*self.locator.CONFIRMATION).click()
        self.find_element(*self.locator.FORM).click()
        sleep(3)
