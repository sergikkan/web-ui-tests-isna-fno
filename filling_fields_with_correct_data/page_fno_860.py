from locators.fno_860_locators import FNO860Locators
from browser_interaction import BasePage
import allure
from time import sleep
import pyautogui


class FNO860Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO860Locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        try:
            assert '860.00 Декларация по плате за пользование водными ресурсами поверхностных источников' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО860
    def select_date_tax_pay(self):
        self.find_element(*self.locator.QUARTER_SELECT).click()
        self.find_element(*self.locator.FIRST_QUARTER_SELECT).click()
        self.find_element(*self.locator.YEAR_SELECT).click()
        self.find_element(*self.locator.SELECT_2020).click()
        sleep(0.5)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_date_tax_pay()

        '''Ниже первая страница'''

    # Раздел. Общая информация
    def section_general_information(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        try:
            self.find_element(*self.locator.INITIAL_SELECT).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка Вид отчетности (декларации)',
                          attachment_type=allure.attachment_type.PNG)

    # Сведения о налогоплательщике (налоговом агенте, агенте или плательщике социальных платежей)
    def information_about_the_taxpayer(self):
        self.scroll_500_px()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        self.find_element(*self.locator.TRUSTEE_SELECT).click()
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        self.find_element(*self.locator.SUBMITTED_ANNEXES_TO_TAX_REPORTING).click()
        sleep(0.5)
        try:
            self.find_element(*self.locator.PAYMENT_FOR_USING_WATER_RESOURCES).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Сведения о налогоплательщике выборка',
                          attachment_type=allure.attachment_type.PNG)

    def after_first_page(self):
        self.after_button_click()

    def first_page(self):
        self.section_general_information()
        self.information_about_the_taxpayer()
        self.after_first_page()

    def second_page(self):
        sleep(0.5)
        self.side_stepper_true()
        assert '001' in self.browser.page_source
        self.find_element(*self.locator.BUTTON_ADD_NEW_FORM).click()
        assert '002' in self.browser.page_source
        self.find_element(*self.locator.BUTTON_REMOVE_NEW_FORM).click()
        #self.find_element(*self.locator.CHECKBOX_AVALIABLE_RESOLUTION).click()
        #assert 'Дата выдачи' in self.browser.page_source
        #assert '№ разрешительного документа' in self.browser.page_source
        self.scroll('200')
        #self.find_element(*self.locator.SELECT_DATE).click()
        sleep(0.5)
        #self.find_element(*self.locator.SELECT_FIRST_DATE).click()
        #self.find_element(*self.locator.SELECT_DATE).click()
        #self.find_element(*self.locator.INPUT_ALLOW_DOC).send_keys('150160')
        pyautogui.moveTo(305, 637, 0.1)
        pyautogui.click()
        sleep(0.5)
        self.find_element(*self.locator.INDUSTRY).click()
        pyautogui.moveTo(592, 637, 0.1)
        pyautogui.click()
        sleep(0.5)
        self.find_element(*self.locator.CUB).click()
        self.scroll('700')
        self.find_element(*self.locator.FIRST_MONTH_LIMIT).send_keys('500')
        self.find_element(*self.locator.SECOND_MONTH_LIMIT).send_keys('500')
        self.find_element(*self.locator.THIRD_MONTH_LIMIT).send_keys('500')
        self.find_element(*self.locator.FIRST_MONTH_FACT).send_keys('1000')
        self.find_element(*self.locator.SECOND_MONTH_FACT).send_keys('1000')
        self.find_element(*self.locator.THIRD_MOTH_FACT).send_keys('1000')
        sleep(0.5)
        assert '1500' in self.browser.page_source
        assert '500' in self.browser.page_source
        self.scroll('900')
        self.find_element(*self.locator.RATE_WITHIN_THE_LIMIT).send_keys('1000')
        sleep(0.5)
        assert '5000' in self.browser.page_source
        self.scroll('1500')
        self.find_element(*self.locator.CALCULATED_WITH_LIMIT).send_keys('500')
        sleep(0.5)
        assert '7500000' in self.browser.page_source
        assert '7500500' in self.browser.page_source
        self.after_button_click()

    def third_page(self):
        sleep(1)
        #self.find_element(*self.locator.OGD_CODE).click()
        sleep(0.5)
        #self.find_element(*self.locator.SELECT_0301).click()
        self.scroll('500')
        self.find_element(*self.locator.FIO_GOV).send_keys('М.И. Автотестеров')
        self.find_element(*self.locator.DATE_END_DECLARATION).click()
        sleep(0.5)
        self.find_element(*self.locator.SELECT_FIRST_DATE_END).click()
        self.find_element(*self.locator.COD_GOV).click()
        sleep(0.3)
        self.find_element(*self.locator.URAL_CASP_SELECT).click()
        self.find_element(*self.locator.CHECKBOX_ACCEPT).click()
        self.find_element(*self.locator.FORM).click()


