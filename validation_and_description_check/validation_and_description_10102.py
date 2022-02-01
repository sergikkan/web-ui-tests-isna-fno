from locators.fno_10102_locators import FNO10102locators
from locators.fno_10101_locators import FNO1010locators
from browser_interaction import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from locators.fno_10102_locators import FNO10102locatorsName as N
import allure


class FNO10102ValidationAndDescription(BasePage):
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
        self.find_element(*self.locator.SUBMIT_BUTTON).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_tax_period()
        self.submit_button()

        '''ПЕРВАЯ СТРАНИЦА'''

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def section_general_information(self):
        self.declaration_type_additional_with_notification()
        with allure.step('Заполнение раздела "ОБЩАЯ ИНФОРМАЦИЯ"'):
            try:
                self.browser.get_screenshot_as_png()
                assert 'Вид отчетности (расчета)' in self.browser.page_source
                assert 'Код валюты' in self.browser.page_source
                assert 'Налоговый период' in self.browser.page_source
                assert 'Отдельная категория' in self.browser.page_source
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Заполнение ОБЩАЯ ИНФОРМАЦИЯ',
                              attachment_type=allure.attachment_type.PNG)
        self.scroll_500_px()

    # РАЗДЕЛ ИНФОРМАЦИЯ О НАЛОГОПЛАТЕЛЬЩИКЕ
    def section_information_about_taxpayer(self):
        self.residention_false_check()
        with allure.step('Заполнение раздела "Информация о налогоплательщике"'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Заполнение налогоплательщика',
                              attachment_type=allure.attachment_type.PNG)
        self.scroll_700_px()

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
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового ' \
               'кодекса' in self.browser.page_source
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 2) пункта 5 статьи 305 ' \
               'Налогового кодекса' in self.browser.page_source
        self.find_element(*self.locator.SECOND_TAX_CODEX_CHECKBOX).click()
        with allure.step('Выбор второго подпункта, 5 статьи 305'):
            try:
                self.browser.save_screenshot('test')
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Выбор второго подпункта',
                              attachment_type=allure.attachment_type.PNG)

    # КНОПКА ДАЛЕЕ НА ПЕРВОЙ СТРАНИЦ
    def after_button_first_page(self):
        self.scroll_900_px()
        self.find_element(*self.locator.AFTER_BUTTON_FIRST_PAGE).click()

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
    def second_page_with_input_first_two_input(self):
        self.side_stepper_false()
        assert '101.02.001 Исчисленная сумма КПН на предыдущий налоговый период' in self.browser.page_source
        assert 'в соответствии с пунктом 1 статьи 302 Налогового кодекса' in self.browser.page_source
        assert 'в соответствии со статьей 652 Налогового кодекса' in self.browser.page_source
        assert '101.02.002 Сумма авансовых платежей, подлежащая уплате за период после сдачи декларации' \
               in self.browser.page_source
        assert 'Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 4) пункта 5 статьи 305 ' \
               'Налогового кодекса' in self.browser.page_source
        assert '101.02.002 Сумма авансовых платежей, подлежащая уплате за период после сдачи декларации' \
               in self.browser.page_source
        self.max_symbol_15_input(*self.locator.FIRST_PARAPGRAPH_INPUT, N.FIRST_PARAPGRAPH_INPUT)
        self.max_symbol_15_input(*self.locator.SECOND_PARAPGRAPH_INPUT, N.SECOND_PARAPGRAPH_INPUT)
        self.check_zero_value_input(*self.locator.FIRST_PARAPGRAPH_INPUT, N.FIRST_PARAPGRAPH_INPUT)
        self.check_zero_value_input(*self.locator.SECOND_PARAPGRAPH_INPUT, N.SECOND_PARAPGRAPH_INPUT)
        self.check_letter_input(*self.locator.FIRST_PARAPGRAPH_INPUT, N.FIRST_PARAPGRAPH_INPUT)
        self.check_letter_input(*self.locator.SECOND_PARAPGRAPH_INPUT, N.SECOND_PARAPGRAPH_INPUT)
        self.check_special_symbol_input(*self.locator.FIRST_PARAPGRAPH_INPUT, N.FIRST_PARAPGRAPH_INPUT)
        self.check_special_symbol_input(*self.locator.SECOND_PARAPGRAPH_INPUT, N.SECOND_PARAPGRAPH_INPUT)

    def second_page_select_first_subparapgraph(self):
        # Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 3) пункта 5 статьи 305 Налогового кодекса]
        self.scroll_500_px()
        assert '101.02.003 Уменьшение суммы авансовых платежей в соответствии со статьей ' \
               '700 Налогового кодекса' in self.browser.page_source
        assert '101.02.004 Сумма ежемесячного авансового платежа' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.ADVANCE_PAYMENT_3_5, N.ADVANCE_PAYMENT_3_5)
        self.max_symbol_15_input(*self.locator.ADVANCE_PAYMENT_700, N.ADVANCE_PAYMENT_700)
        self.check_zero_value_input(*self.locator.ADVANCE_PAYMENT_3_5, N.ADVANCE_PAYMENT_3_5)
        self.check_zero_value_input(*self.locator.ADVANCE_PAYMENT_700, N.ADVANCE_PAYMENT_700)
        self.check_letter_input(*self.locator.ADVANCE_PAYMENT_3_5, N.ADVANCE_PAYMENT_3_5)
        self.check_letter_input(*self.locator.ADVANCE_PAYMENT_700, N.ADVANCE_PAYMENT_700)
        self.check_special_symbol_input(*self.locator.ADVANCE_PAYMENT_3_5, N.ADVANCE_PAYMENT_3_5)
        self.check_special_symbol_input(*self.locator.ADVANCE_PAYMENT_700, N.ADVANCE_PAYMENT_700)
        self.scroll_900_px()
        self.max_symbol_15_input(*self.locator.ADVANCE_PAYMENT_MONTHLY, N.ADVANCE_PAYMENT_MONTHLY)
        self.check_zero_value_input(*self.locator.ADVANCE_PAYMENT_MONTHLY, N.ADVANCE_PAYMENT_MONTHLY)
        self.check_letter_input(*self.locator.ADVANCE_PAYMENT_MONTHLY, N.ADVANCE_PAYMENT_MONTHLY)
        self.check_special_symbol_input(*self.locator.ADVANCE_PAYMENT_MONTHLY, N.ADVANCE_PAYMENT_MONTHLY)
        self.after_button_click()

    def second_page_select_second_subparapgraph(self):
        self.side_stepper_false()
        self.scroll_500_px()
        assert '101.02.005 Предполагаемая сумма КПН, исчисленная в соответствии ' \
               'с пунктом 1 статьи 302 Налогового кодекса' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.SUPPOSED_SUM1, N.SUPPOSED_SUM1)
        self.max_symbol_15_input(*self.locator.SUPPOSED_SUM2, N.SUPPOSED_SUM2)
        self.check_zero_value_input(*self.locator.SUPPOSED_SUM1, N.SUPPOSED_SUM1)
        self.check_zero_value_input(*self.locator.SUPPOSED_SUM2, N.SUPPOSED_SUM2)
        self.check_letter_input(*self.locator.SUPPOSED_SUM1, N.SUPPOSED_SUM1)
        self.check_letter_input(*self.locator.SUPPOSED_SUM2, N.SUPPOSED_SUM2)
        self.check_special_symbol_input(*self.locator.SUPPOSED_SUM1, N.SUPPOSED_SUM1, N.SUPPOSED_SUM2)
        self.check_special_symbol_input(*self.locator.SUPPOSED_SUM2, N.SUPPOSED_SUM2)
        self.max_symbol_15_input(*self.locator.DECREASE_AVANCE_PAYMENT, N.DECREASE_AVANCE_PAYMENT)
        self.max_symbol_15_input(*self.locator.TOTAL_AVANCE_PAYMENT, N.TOTAL_AVANCE_PAYMENT)
        self.check_zero_value_input(*self.locator.DECREASE_AVANCE_PAYMENT, N.DECREASE_AVANCE_PAYMENT)
        self.check_zero_value_input(*self.locator.TOTAL_AVANCE_PAYMENT, N.TOTAL_AVANCE_PAYMENT)
        self.check_letter_input(*self.locator.DECREASE_AVANCE_PAYMENT, N.DECREASE_AVANCE_PAYMENT)
        self.check_letter_input(*self.locator.TOTAL_AVANCE_PAYMENT, N.TOTAL_AVANCE_PAYMENT)
        self.check_special_symbol_input(*self.locator.DECREASE_AVANCE_PAYMENT, N.DECREASE_AVANCE_PAYMENT)
        self.check_special_symbol_input(*self.locator.TOTAL_AVANCE_PAYMENT, N.TOTAL_AVANCE_PAYMENT)
        assert '101.02.006 Предполагаемая сумма КПН, исчисленная в ' \
               'соответствии со статьей 652 Налогового кодекса' in self.browser.page_source
        assert '101.02.008 Уменьшение суммы авансовых платежей в соответствии ' \
               'со статьей 700 Налогового кодекса' in self.browser.page_source
        self.scroll_900_px()
        self.after_button_click()

    '''ТРЕТЬЯ СТРАНИЦА ОТПРАВКА'''

    # Кнопка сформировать
    def to_form(self):
        self.scroll_900_px()
        self.check_without_filling_ogd_code()
        with allure.step('Сформирование документа последняя страница'):
            try:
                self.browser.find_element_by_xpath("//*[contains(.,'(Форма 101.02) Расчет суммы авансовых платежей по"
                                                   " корпоративному подоходному налогу, подлежащей уплате за период"
                                                   " после сдачи декларации')]").is_displayed()
            finally:
                allure.attach(self.browser.get_screenshot_as_png(), name='Последняя страница',
                              attachment_type=allure.attachment_type.PNG)

    def third_page(self):
        self.to_form()
