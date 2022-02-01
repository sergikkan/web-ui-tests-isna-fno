from locators.fno_871_locators import FNO871Locators
from browser_interaction import BasePage
from time import sleep
import allure
import pyautogui


class FNO870Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO871Locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        try:
            assert '871.00 Реестр договоров аренды пользования' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    def select_date_tax_pay(self):
        sleep(1)
        pyautogui.moveTo(516, 500, 0.1)
        pyautogui.click()
        self.find_element(*self.locator.SELECT_2021).click()
        sleep(1)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_date_tax_pay()

    '''Первая страница ФНО'''

    # Раздел. Общая информация
    def first_page(self):
        self.scroll('300')
        self.find_element(*self.locator.REGISTRY_TYPE).click()
        sleep(0.2)
        self.find_element(*self.locator.REGISTRY_TYPE).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.NOTICE_NUMBER).send_keys('12345678901234567890')
        self.find_element(*self.locator.NOTICE_DATE).click()
        sleep(0.2)
        self.find_element(*self.locator.NOTICE_DATE_SELECT).click()
        self.find_element(*self.locator.APPS).click()
        sleep(0.2)
        self.find_element(*self.locator.APP_SELECT).click()
        self.find_element(*self.locator.AFTER).click()

    def second_and_third_page(self):
        self.scroll('5000')
        self.find_element(*self.locator.AFTER).click()
        self.find_element(*self.locator.ADD_APP).click()
        sleep(0.5)
        self.find_element(*self.locator.REMOVE_APP).click()
        self.scroll('400')
        self.find_element(*self.locator.NAME_OF_TRADE_ORGANISATION).send_keys('123zxc')
        self.find_element(*self.locator.GENERAL_SQUARE).send_keys('123zxc')
        self.find_element(*self.locator.TRADE_SQUARE).send_keys('123zxc')
        self.find_element(*self.locator.NUMBER_OF_TRADE_PLACES).send_keys('123zxc')
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.CATEGORY_OF_OBJECT).click()
        sleep(0.3)
        self.find_element(*self.locator.CATEGORY_OF_OBJECT_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator.ADDRESS).send_keys('123zxc')
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_E).send_keys('123zxc')
        self.find_element(*self.locator.APP_G).send_keys('123zxc')
        self.find_element(*self.locator.APP_I).send_keys('123zxc')
        self.find_element(*self.locator.APP_F).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_F_SELECT).click()
        self.find_element(*self.locator.APP_H).click()
        sleep(0.3)
        self.find_element(*self.locator.APP_H_SELECT).click()
        element = self.browser.find_element_by_xpath('//*[text()="Далее"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.APP_J).send_keys('123zxc')
        self.find_element(*self.locator.APP_L).send_keys('123zxc')
        self.find_element(*self.locator.APP_M).send_keys('123zxc')
        self.find_element(*self.locator.APP_N).send_keys('123zxc')
        self.find_element(*self.locator.APP_O).send_keys('123zxc')
        self.find_element(*self.locator.FROM).click()
        sleep(0.3)
        self.find_element(*self.locator.FROM_SELECT).click()
        sleep(0.3)
        self.find_element(*self.locator.TO_SELECT).click()
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.GO_TO_SECOND_PAGE).click()
        self.scroll('800')
        assert '123' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()
        sleep(1)
        self.scroll('8000')
        self.find_element(*self.locator.AFTER).click()
        self.scroll('500')
        self.find_element(*self.locator.CONFIRM_2).click()
        self.find_element(*self.locator.FORM).click()