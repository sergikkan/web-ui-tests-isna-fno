from locators.fno_870_locators import FNO870Locators
from browser_interaction import BasePage
from time import sleep
import allure
import pyautogui


class FNO870Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO870Locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        try:
            assert '870.00 Декларация по плате за эмиссии в окружающую среду' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    def select_date_tax_pay(self):
        sleep(1)
        pyautogui.moveTo(516, 475, 0.1)
        pyautogui.click()
        self.find_element(*self.locator.FIRST_QUARTAL_SELECT).click()
        self.find_element(*self.locator.YEAR_SLEECT).click()
        self.find_element(*self.locator.SELECT_2021).click()
        sleep(2)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_date_tax_pay()

    '''Первая страница ФНО'''

    # Раздел. Общая информация
    def section_general_information(self):
        sleep(3)
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        try:
            self.find_element(*self.locator.INITIAL).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка Вид отчетности (декларации)',
                          attachment_type=allure.attachment_type.PNG)
        # Сведения о налогоплательщике (налоговом агенте, агенте или плательщике социальных платежей)

    def information_about_the_taxpayer(self):
        self.scroll('500')
        self.find_element(*self.locator.BIN).send_keys('010815501417')
        self.find_element(*self.locator.TAXPAYER_CATEGORIES).click()
        self.find_element(*self.locator.TAXPAYER_CATEGORIES_SELECT).click()
        self.find_element(*self.locator.SUBMITTED_ANNEXES_TO_TAX_REPORTING).click()
        sleep(0.5)
        self.after_button_click()

    def first_page(self):
        self.tax_period_select()
        self.section_general_information()
        self.information_about_the_taxpayer()

    def second_page(self):
        sleep(1)
        self.find_element(*self.locator.ENVIRONMENTAL_PERMIT).click()
        self.scroll('200')
        self.find_element(*self.locator.PEMISSION_NO).send_keys('1020202')
        self.find_element(*self.locator.DATE_OF_ISSUE).click()
        sleep(0.3)
        self.find_element(*self.locator.DATE_SELECT).click()
        self.find_element(*self.locator.CATEGORIES_OF_OBJECT).click()
        self.find_element(*self.locator.CATEGORY_SELECT).click()
        pyautogui.moveTo(340, 671, 0.1)
        pyautogui.click()
        self.find_element(*self.locator.SELECT_TYPE).click()
        pyautogui.moveTo(620, 671, 0.1)
        pyautogui.click()
        self.find_element(*self.locator.SELECT_TYPE_OF_UNITS).click()
        self.scroll('500')
        self.find_element(*self.locator.TYPE_OF_POLLUTANT_PARAGRAPH).send_keys('1010')
        self.find_element(*self.locator.TYPE_OF_POLLUTANT_SUBPARAGRAPH).send_keys('1010')
        self.find_element(*self.locator.CLASSIFICATION_CODE).send_keys('12345')
        self.scroll('700')
        self.find_element(*self.locator.REMAINING_STANDARD_AT_THE_BEGINNING).send_keys('101012')
        self.find_element(*self.locator.ACTUAL_VOLUME_OF_EMISSIONS_1).send_keys('101012')
        self.find_element(*self.locator.ACTUAL_VOLUME_OF_EMISSIONS_2).send_keys('101012')
        self.find_element(*self.locator.REMAINING_STANDARD_AT_THE_END).send_keys('101012')
        self.find_element(*self.locator.THE_RATE_OF_PAYMENT_ESTABLISHED).send_keys('101')
        #self.scroll('1500')
        self.find_element(*self.locator.THE_SIZE_OF_THE_INCREASE_IN).send_keys('101012')
        self.find_element(*self.locator.COEFFICIENTS_APPLIED_TO_PAYERS).click()
        self.find_element(*self.locator.SELECT_COEFFICIENT).click()
        self.scroll('2000')
        self.after_button_click()

    def third_page(self):
        #self.find_element(*self.locator.CODE).click()
        #self.find_element(*self.locator.SELECT_0302).click()
        self.find_element(*self.locator.ACCEPT_CHECKBOX_FNO).click()
        self.find_element(*self.locator.FORM).click()
        assert 'Внимание!' in self.browser.page_source
        with allure.step('Формирование документа'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Формирование документа',
                              attachment_type=allure.attachment_type.PNG)
