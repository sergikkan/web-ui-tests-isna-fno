from locators.fno_10103_locators import FNO10103Locators
from browser_interaction import BasePage
from time import sleep
import allure


class FNO10103Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO10103Locators

        '''ПЕРВАЯ СТРАНИЦА'''

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def first_page_with_correct_data(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        self.find_element(*self.locator.INITIAL_SELECT).click()
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        with allure.step('Заполнение раздела "ОБЩАЯ ИНФОРМАЦИЯ"'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Заполнение ОБЩАЯ ИНФОРМАЦИЯ',
                              attachment_type=allure.attachment_type.PNG)
        self.scroll('500')
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        self.find_element(*self.locator.SELECT_RESIDENT_TRUE).click()
        with allure.step('Выбор резидентсва "Резидент"'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Резидентсво',
                              attachment_type=allure.attachment_type.PNG)
        self.scroll('700')
        # 101.03.001Сумма выплачиваемого дохода за квартал
        self.find_element(*self.locator.FIRST_MONTH_I).send_keys('1000')
        self.find_element(*self.locator.SECOND_MONTH_I).send_keys('1000')
        self.find_element(*self.locator.THIRD_MONTH_I).send_keys('1000')
        sleep(0.3)
        assert '3000' in self.browser.page_source
        self.find_element(*self.locator.THIRD_MONTH_I).clear()
        sleep(0.3)
        assert '2000' in self.browser.page_source
        self.find_element(*self.locator.THIRD_MONTH_I).send_keys('1000')
        sleep(0.3)
        assert '3000' in self.browser.page_source

        with allure.step('Заполнение и проверка калькуляции "Сумма выплачиваемого дохода за квартал"'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Сумма выплачиваемого дохода',
                              attachment_type=allure.attachment_type.PNG)

        self.find_element(*self.locator.FIRST_MONTH_II).send_keys('2000')
        self.find_element(*self.locator.SECOND_MONTH_II).send_keys('2000')
        self.find_element(*self.locator.THIRD_MONTH_II).send_keys('2000')
        sleep(0.3)
        assert '6000' in self.browser.page_source
        self.find_element(*self.locator.THIRD_MONTH_II).clear()
        sleep(0.3)
        assert '4000' in self.browser.page_source
        self.find_element(*self.locator.THIRD_MONTH_II).send_keys('2000')
        sleep(0.3)
        assert '6000' in self.browser.page_source

        with allure.step(
                'Заполнение и проверка калькуляции "Сумма налога, удержанного у источника выплаты за квартал"'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Сумма налога',
                              attachment_type=allure.attachment_type.PNG)

        self.after_button_click()

    def second_page_sending(self):
        sleep(0.5)
        self.find_element(*self.locator.CODE).click()
        self.find_element(*self.locator.SELECT_0302).click()
        self.browser.find_element_by_xpath('//*[text()="ДГД по Акмолинской области"]')
        self.find_element(*self.locator.ACCEPT_CHECKBOX_FNO).click()
        self.scroll_500_px()
        self.find_element(*self.locator.FORM).click()
        sleep(5)
        with allure.step('Формирование документа'):
            try:
                self.browser.get_screenshot_as_png()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Формирование документа',
                              attachment_type=allure.attachment_type.PNG)

