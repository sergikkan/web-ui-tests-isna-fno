from locators.fno_10101_locators import FNO1010locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import allure



class FNO10101Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO1010locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        with allure.step('Выбор налогового периода 101.01 ФНО'):
            try:
                assert 'Налоговый период' in self.browser.page_source
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                              attachment_type=allure.attachment_type.PNG)
        assert '101.01 Расчет суммы авансовых платежей по корпоративному подоходному' \
               ' налогу, подлежащей уплате за период до ' \
               'сдачи декларации' in self.browser.page_source

        '''ВЫБОР НАЛОГОВОГО ПЕРИОДА'''

    def select_tax_period(self):
        self.find_element(*self.locator.YEAR_SELECT).click()
        self.hover(*self.locator.SELECT_2021)
        self.find_element(*self.locator.SELECT_2021).click()

    # КНОПКА ДАЛЕЕ ПОСЛЕ ВЫБОРАНАЛОГОВОГО ПЕРИОДА
    def submit_button(self):
        self.find_element(*self.locator.SUBMIT_BUTTON).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_tax_period()
        sleep(1)
        self.submit_button()

        '''ПЕРВАЯ СТРАНИЦА'''

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def section_general_information(self):
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.INITIAL_SELECT).click()
        with allure.step('Заполнение раздела "ОБЩАЯ ИНФОРМАЦИЯ"'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Заполнение ОБЩАЯ ИНФОРМАЦИЯ',
                              attachment_type=allure.attachment_type.PNG)
        self.scroll('500')

    # РАЗДЕЛ ИНФОРМАЦИЯ О НАЛОГОПЛАТЕЛЬЩИКЕ
    def section_information_about_taxpayer(self):
        self.find_element(*self.locator.SEPERATE_CATEGORY).click()
        self.find_element(*self.locator.CONFIDENTIONAL_SELECT).click()
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        self.find_element(*self.locator.RESIDENTION_TRUE).click()
        with allure.step('Заполнение раздела "Информация о налогоплательщике"'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Заполнение налогоплательщика',
                              attachment_type=allure.attachment_type.PNG)

    # ПЕРВЫЙ ВАРИАНТ С ВЫБОРОМ ПЕРВОГО ПОДПУНТКА
    def select_first_subparagraph(self):
        self.find_element(*self.locator.FIRST_TAX_CODEX_CHECKBOX).click()
        with allure.step('Выбор первого подпункта, 5 статьи 305'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выбор первого подпункта',
                              attachment_type=allure.attachment_type.PNG)

    # ВТОРОЙ ВАРИАНТ С ВЫБОРОМ ПЕРВОГО ПОДПУНТКА
    def select_second_subparagraph(self):
        self.browser.find_element(By.XPATH, "//*[contains(.,'Расчет суммы авансовых платежей по КНП в соответствии с"
                                            " подпунктом 1) пункта 5 статьи 305 Налогового кодекса')]").is_displayed()
        self.browser.find_element(By.XPATH, "//*[contains(.,'Расчет суммы авансовых платежей по КНП в соответствии с"
                                            " подпунктом 2) пункта 5 статьи 305 Налогового кодекса')]").is_displayed()
        self.find_element(*self.locator.SECOND_TAX_CODEX_CHECKBOX).click()
        with allure.step('Выбор второго подпункта, 5 статьи 305'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выбор второго подпункта',
                              attachment_type=allure.attachment_type.PNG)

    def after_button_first_page(self):
        self.after_button_click()

    def first_page_first_option(self):
        self.section_general_information()
        self.section_information_about_taxpayer()
        self.select_first_subparagraph()
        self.after_button_first_page()

    def first_page_second_option(self):
        self.section_general_information()
        self.section_information_about_taxpayer()
        self.select_second_subparagraph()
        self.after_button_first_page()
        '''ВТОРАЯ СТРАНИЦА '''

    # Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового кодекса
    # 100.00.001Общая сумма авансовых платежей за предыдущий налоговый период
    def sum_amount_first_option(self):
        assert 'Общая сумма авансовых платежей за предыдущий налоговый период' in self.browser.page_source
        self.find_element(*self.locator.TOTAL_ADVANCE_AMOUNT).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION).send_keys('5000')
        self.scroll('200')
        sleep(6)
        assert '1 667' in self.browser.page_source
        # CHECK CALCULATION
        self.find_element(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION).clear()
        self.find_element(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION).send_keys('10000')
        sleep(1)
        assert '3 333' in self.browser.page_source
        with allure.step('Заполнение первой страницы после выбора первого подпункта и проверка калькуляции'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Первая страница первый подпункт',
                              attachment_type=allure.attachment_type.PNG)

    def sum_amount_second_option(self):
        self.side_stepper_true()
        self.find_element(*self.locator.EXPECTED_SUM).send_keys('10000')
        self.find_element(*self.locator.EXPECTED_SUM2).send_keys('10000')
        sleep(0.3)
        assert '5 000' in self.browser.page_source
        self.find_element(*self.locator.EXPECTED_SUM2).clear()
        self.find_element(*self.locator.EXPECTED_SUM2).send_keys('5000')
        sleep(0.3)
        assert '3 750' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.DECLINE_SUM1).send_keys('1000')
        sleep(0.3)
        assert '2 750' in self.browser.page_source
        with allure.step('Заполнение первой страницы после выбора второго подпункта и проверка калькуляции'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Первая страница второй подпункт',
                              attachment_type=allure.attachment_type.PNG)

    def after_button_second_page(self):
        self.scroll('900')
        self.after_button_click()

    def second_page_first_option(self):
        self.sum_amount_first_option()
        self.after_button_second_page()

    def second_page_second_option(self):
        self.sum_amount_second_option()
        self.after_button_second_page()

        '''ТРЕТЬЯ СТРАНИЦА ОТПРАВКА'''

    # Код ОГД по месту нахождения
    def code(self):
        sleep(1)
        assert 'Обязательное поле' in self.browser.page_source
        self.scroll('700')
        self.browser.execute_script('window.scroll(0, -700)')
        self.find_element(*self.locator.CODE).click()
        self.find_element(*self.locator.SELECT_0302).click()
        self.find_element(*self.locator.ACCEPT_CHECKBOX_FNO).click()

    # Кнопка сформировать
    def to_form(self):
        sleep(1)
        self.find_element(*self.locator.FORM).click()
        self.browser.find_element(By.XPATH, "//*[contains(.,'(Форма 101.01) Расчет суммы авансовых платежей по "
                                            "корпоративному подоходному налогу, подлежащей уплате за период до"
                                            " сдачи декларации')]").is_displayed()
        with allure.step('Сформирование документа последняя страница'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Последняя страница',
                              attachment_type=allure.attachment_type.PNG)

    def third_page(self):
        self.code()
        self.to_form()