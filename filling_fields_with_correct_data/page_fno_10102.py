from locators.fno_10102_locators import FNO10102locators
from locators.fno_10101_locators import FNO1010locators
from browser_interaction import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import allure


class FNO_10102_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO10102locators
        self.locator_10101 = FNO1010locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        with allure.step('Выбор налогового периода 101.02 ФНО'):
            try:
                self.browser.find_element(By.XPATH, "//*[contains(.,'Налоговый период')]").is_displayed()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                              attachment_type=allure.attachment_type.PNG)
        self.browser.find_element(By.XPATH, "//*[contains(.,'101.02 Расчет суммы авансовых платежей по корпоративному"
                                            " подоходному налогу, подлежащей уплате за период"
                                            " после сдачи декларации')]").is_displayed()

        '''ВЫБОР НАЛОГОВОГО ПЕРИОДА'''

    # ВЫБОР НАЛОВОГО ПЕРИОДА (ДАТА)
    def select_tax_period(self):
        self.find_element(*self.locator.YEAR_SELECT).click()
        self.hover(*self.locator.SELECT_2021)
        self.find_element(*self.locator.SELECT_2021).click()

    # КНОПКА ДАЛЕЕ ПОСЛЕ ВЫБОРАНАЛОГОВОГО ПЕРИОДА
    def submit_button(self):
        sleep(1)
        self.find_element(*self.locator.SUBMIT_BUTTON).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_tax_period()
        self.submit_button()

        '''ПЕРВАЯ СТРАНИЦА'''

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def section_general_information(self):
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        sleep(0.3)
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
        sleep(0.2)
        self.find_element(*self.locator.CONFIDENTIONAL_SELECT).click()
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        sleep(0.2)
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
        self.find_element(*self.locator.SECOND_TAX_CODEX_CHECKBOX).click()
        with allure.step('Выбор второго подпункта, 5 статьи 305'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выбор второго подпункта',
                              attachment_type=allure.attachment_type.PNG)

    # КНОПКА ДАЛЕЕ НА ПЕРВОЙ СТРАНИЦ

    def first_page_first_option(self):
        self.section_general_information()
        self.section_information_about_taxpayer()
        self.select_first_subparagraph()
        self.after_button_click()

    def first_page_second_option(self):
        self.section_general_information()
        self.section_information_about_taxpayer()
        self.select_second_subparagraph()
        self.after_button_click()

        '''ВТОРАЯ СТРАНИЦА '''

    # Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового кодекса
    # 100.00.001Общая сумма авансовых платежей за предыдущий налоговый период
    def second_page_with_input_first_two_input(self):
        self.find_element(*self.locator.FIRST_PARAPGRAPH_INPUT).send_keys('10000')
        self.find_element(*self.locator.SECOND_PARAPGRAPH_INPUT).send_keys('10000')
        sleep(0.5)
        assert '20000' in self.browser.page_source
        self.find_element(*self.locator.FIRST_PARAPGRAPH_INPUT).clear()
        self.find_element(*self.locator.FIRST_PARAPGRAPH_INPUT).send_keys('5000')
        assert '15000' in self.browser.page_source

    def second_page_select_first_subparapgraph(self):
        # Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 3) пункта 5 статьи 305 Налогового кодекса]
        self.scroll('500')
        #self.find_element(*self.locator.ADVANCE_PAYMENT_3_5).send_keys('10000')
        self.find_element(*self.locator.ADVANCE_PAYMENT_700).send_keys('10000')
        self.scroll('900')
        sleep(0.7)
        self.find_element(*self.locator.ADVANCE_PAYMENT_MONTHLY).send_keys('10000')
        sleep(0.5)
        self.find_element(*self.locator.AFTER_BUTTON_FIRST_PAGE).click()

    def second_page_select_second_subparagraph(self):
        self.browser.find_element_by_xpath('//*[@data-icon="check"]')
        self.scroll_500_px()
        self.find_element(*self.locator.SUPPOSED_SUM1).send_keys('10000')
        self.find_element(*self.locator.SUPPOSED_SUM2).send_keys('10000')
        self.browser.find_element_by_xpath("//*[contains(.,'15 000 ')]").is_displayed()
        self.find_element(*self.locator.SUPPOSED_SUM2).clear()
        self.find_element(*self.locator.SUPPOSED_SUM2).send_keys('5000')
        self.browser.find_element_by_xpath("//*[contains(.,'11 250 ')]").is_displayed()
        self.find_element(*self.locator.DECREASE_AVANCE_PAYMENT).send_keys('10000')
        self.find_element(*self.locator.TOTAL_AVANCE_PAYMENT).send_keys('10000')
        self.scroll('900')
        self.after_button_click()

    '''ТРЕТЬЯ СТРАНИЦА ОТПРАВКА'''

    # Код ОГД по месту нахождения
    def code(self):
        sleep(1)
        assert 'Обязательное поле' in self.browser.page_source
        self.scroll('700')
        self.browser.find_element_by_xpath('//button[@disabled]')
        self.browser.execute_script('window.scroll(0, -700)')
        sleep(1)
        self.find_element(*self.locator_10101.CODE).click()
        self.find_element(*self.locator_10101.SELECT_0302).click()
        self.find_element(*self.locator_10101.ACCEPT_CHECKBOX_FNO).click()

    # Кнопка сформировать
    def to_form(self):
        self.find_element(*self.locator_10101.FORM).click()
        assert 'Внимание!' in self.browser.page_source
        with allure.step('Сформирование документа последняя страница'):
            try:
                self.browser.find_element_by_xpath("//*[contains(.,'(Форма 101.02) Расчет суммы авансовых платежей по"
                                                   " корпоративному подоходному налогу, подлежащей уплате за период"
                                                   " после сдачи декларации')]").is_displayed()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Последняя страница',
                              attachment_type=allure.attachment_type.PNG)

    def third_page(self):
        self.code()
        self.to_form()
