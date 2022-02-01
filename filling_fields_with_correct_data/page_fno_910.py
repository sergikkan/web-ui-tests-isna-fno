from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.fno_910_page_locators import FNO910Locators
from browser_interaction import BasePage
from time import sleep
import allure


class FNO910Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO910Locators

    # ПРОВЕРКА ТОГО ЧТО МЫ ВЫБРАЛИ ПРАВИЛЬНОЕ ФНО
    def check_tax_period_text(self):
        try:
            self.browser.find_element(By.XPATH, "//*[contains(.,'Налоговый период')]").is_displayed()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)
        self.browser.find_element(By.XPATH, "//*[contains(.,'910.00 Упрощенная декларация"
                                            " для субъектов малого бизнеса')]").is_displayed()

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО910
    def select_date_tax_pay(self):
        self.find_element(*self.locator.HALF_YEAR_SELECT).click()
        self.find_element(*self.locator.FIRST_HALF_YEAR).click()
        self.find_element(*self.locator.INPUT_YEAR).click()
        sleep(1)
        try:
            self.find_element(*self.locator.SELECT_YEAR_2020).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода 2020 г.',
                          attachment_type=allure.attachment_type.PNG)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def tax_period_select(self):
        self.check_tax_period_text()
        self.select_date_tax_pay()

        '''Ниже первая страница'''

    # Раздел. Общая информация
    def section_general_information(self):
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        try:
            self.find_element(*self.locator.INITIAL_SELECT).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка Вид отчетности (декларации)',
                          attachment_type=allure.attachment_type.PNG)

    # Сведения о налогоплательщике (налоговом агенте, агенте или плательщике социальных платежей)
    def information_about_the_taxpayer(self):
        self.scroll('400')
        self.find_element(*self.locator.SEPERATE_CATEGORY).click()
        self.find_element(*self.locator.CLASS_SELECT).click()
        self.find_element(*self.locator.ACCOUNTANT).click()
        self.find_element(*self.locator.RESIDENTION_SELECT).click()
        try:
            self.find_element(*self.locator.SELECT_RESIDENT_TRUE).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Сведения о налогоплательщике выборка',
                          attachment_type=allure.attachment_type.PNG)

    # Наличие трехкомпонентной интегрированной системы (ТИС)
    def tis_availability(self):
        self.find_element(*self.locator.TIS_CHECKBOX).click()
        self.scroll('500')
        self.find_element(*self.locator.TIS_NAME_INPUT).send_keys('Test')
        self.find_element(*self.locator.TIS_CARD_NUMBER_INPUT).send_keys('54632')
        self.find_element(*self.locator.TIS_DATE_INPUT).click()
        self.find_element(*self.locator.TIS_DATE_SELECT).click()
        self.scroll('900')
        # Раздел. Сведения о запасах

    # КНОПКА Далее после заполнения первой страницы
    def after_first_page(self):
        self.find_element(*self.locator.AFTER_BUTTON).click()

    def first_page_without_annexes_to_tax_reporting(self):
        self.section_general_information()
        self.information_about_the_taxpayer()
        self.tis_availability()
        self.after_first_page()

        '''Ниже вторая страница'''



    def income_with_cash_and_cashless(self):
        # 910.00.001 Доход
        self.find_element(*self.locator.A_INPUT_INCOME_CASHLESS).send_keys('10000')
        self.find_element(*self.locator.B_INPUT_INCOME_CASHLESS).send_keys('10000')
        sleep(2)
        #self.find_element(*self.locator.A_I).send_keys('10000')
        #try:
        #    self.find_element(*self.locator.B_I).send_keys('10000')
        #finally:
        #    allure.attach(self.browser.get_screenshot_as_png(), name='Раздел. Исчисление налогов 910.00.001 Доход',
         #                 attachment_type=allure.attachment_type.PNG)

    def income_with_law(self):
        # 910.00.002 В том числе доход от корректировки в соответствии с Законом о трансфертном ценообразовании

        self.find_element(*self.locator.INCOME_WITH_LAW).send_keys('10000')
        self.scroll('350')
        sleep(1)

    def employee(self):
        # 910.00.003 Среднесписочная численность работников, в том числе:
        self.find_element(*self.locator.EMPLOYEE_QUANTITY).send_keys('29')
        self.find_element(*self.locator.PENSIONER_QUANTITY).send_keys('3')
        self.find_element(*self.locator.INVALID_QUANTITY).send_keys('1')
        sleep(2)
        try:
            self.find_element(*self.locator.AVERAGE_SALARY).send_keys('100000')
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='910.00.003 Среднесписочная '
                                                                     'численность работников, в том числе:',
                          attachment_type=allure.attachment_type.PNG)

    def after_second_page(self):
        self.browser.execute_script('window.scroll(0, 1300)')
        self.find_element(*self.locator.AFTER_BUTTON).click()

    def second_page(self):
        self.income_with_cash_and_cashless()
        self.income_with_law()
        self.employee()
        self.after_second_page()

    def SO(self):
        self.scroll('500')
        self.find_element(*self.locator.INCOME_SO_1).send_keys('10')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_SO_2).send_keys('5')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_SO_3).send_keys('3')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_SO_4).send_keys('2')
        sleep(0.3)
        assert '35' in self.browser.page_source
        assert '70' in self.browser.page_source
        assert '53' in self.browser.page_source
        assert '18' in self.browser.page_source
        self.scroll('400')
        self.find_element(*self.locator.INCOME_SO_5).send_keys('100')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_SO_6).send_keys('500')
        sleep(0.3)
        assert '4' in self.browser.page_source
        assert '18' in self.browser.page_source

    def opv(self):
        self.scroll('700')
        self.find_element(*self.locator.INCOME_OPV_1).send_keys('300')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_OPV_2).send_keys('200')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_OPV_3).send_keys('100')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_OPV_4).send_keys('400')
        sleep(0.3)
        assert '30' in self.browser.page_source
        assert '20' in self.browser.page_source
        assert '10' in self.browser.page_source
        assert '40' in self.browser.page_source
        self.scroll('400')
        self.find_element(*self.locator.INCOME_OPV_5).send_keys('700')
        sleep(0.3)
        self.find_element(*self.locator.INCOME_OPV_6).send_keys('800')
        sleep(0.3)
        assert '70' in self.browser.page_source
        assert '80' in self.browser.page_source
        assert '1000' in self.browser.page_source
        assert '100' in self.browser.page_source
        self.scroll('800')

    def sum(self):
        self.find_element(*self.locator.CON_SUM_1).send_keys('80')
        sleep(0.5)
        self.find_element(*self.locator.CON_SUM_2).send_keys('10')
        sleep(0.5)
        self.find_element(*self.locator.CON_SUM_3).send_keys('50')
        sleep(0.5)
        self.find_element(*self.locator.CON_SUM_4).send_keys('100')
        sleep(0.5)
        self.find_element(*self.locator.CON_SUM_5).send_keys('70')
        sleep(0.5)
        self.find_element(*self.locator.CON_SUM_6).send_keys('90')
        sleep(0.5)
        assert '400' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.AFTER_BUTTON).click()

    def third_page(self):
        self.SO()
        self.opv()
        self.sum()



    def inp(self):
        self.browser.find_element_by_xpath('//*[@data-icon="check"]')
        self.find_element(*self.locator.IPN_1_MONTH).send_keys('200')
        sleep(0.5)
        self.find_element(*self.locator.IPN_2_MONTH).send_keys('300')
        sleep(0.5)
        self.find_element(*self.locator.IPN_3_MONTH).send_keys('100')
        sleep(0.5)
        self.find_element(*self.locator.IPN_4_MONTH).send_keys('500')
        sleep(0.5)
        self.find_element(*self.locator.IPN_5_MONTH).send_keys('400')
        sleep(0.5)
        self.find_element(*self.locator.IPN_6_MONTH).send_keys('900')
        sleep(0.5)
        assert '2400' in self.browser.page_source
        self.browser.execute_script('window.scroll(0,600)')

    def inp2(self):
        self.find_element(*self.locator.IPN_NO_RESIDENT_1).send_keys('100')
        sleep(0.5)
        self.find_element(*self.locator.IPN_NO_RESIDENT_2).send_keys('350')
        sleep(0.5)
        self.find_element(*self.locator.IPN_NO_RESIDENT_3).send_keys('250')
        sleep(0.5)
        self.find_element(*self.locator.IPN_NO_RESIDENT_4).send_keys('900')
        sleep(0.5)
        self.find_element(*self.locator.IPN_NO_RESIDENT_5).send_keys('700')
        sleep(0.5)
        self.find_element(*self.locator.IPN_NO_RESIDENT_6).send_keys('400')
        sleep(0.5)
        assert '2700' in self.browser.page_source
        self.browser.execute_script('window.scroll(0, 1300)')

    def fl_income(self):
        self.find_element(*self.locator.FL_INCOME_1).send_keys('10000')
        sleep(0.5)
        assert '350' in self.browser.page_source
        self.find_element(*self.locator.FL_INCOME_2).send_keys('20000')
        sleep(0.5)
        assert '700' in self.browser.page_source
        self.find_element(*self.locator.FL_INCOME_3).send_keys('30000')
        sleep(0.5)
        assert '1050' in self.browser.page_source
        self.find_element(*self.locator.FL_INCOME_4).send_keys('40000')
        sleep(0.5)
        self.find_element(*self.locator.FL_INCOME_5).send_keys('50000')
        sleep(0.5)
        self.find_element(*self.locator.FL_INCOME_6).send_keys('60000')
        sleep(0.5)
        assert '7350' in self.browser.page_source
        assert '210000' in self.browser.page_source
        self.scroll('2000')

    def opv1(self):
        self.find_element(*self.locator.OPV_1).send_keys('5000')
        sleep(0.5)
        self.find_element(*self.locator.OPV_2).send_keys('10000')
        sleep(0.5)
        self.find_element(*self.locator.OPV_3).send_keys('7000')
        sleep(0.5)
        self.find_element(*self.locator.OPV_4).send_keys('6000')
        sleep(0.5)
        self.find_element(*self.locator.OPV_5).send_keys('3000')
        sleep(0.5)
        self.find_element(*self.locator.OPV_6).send_keys('9000')
        sleep(0.5)
        assert '40000' in self.browser.page_source
        assert '4000' in self.browser.page_source
        self.scroll('2700')

    def oppv1(self):
        self.find_element(*self.locator.OPPV_1).send_keys('30000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_1_TO_PAY).send_keys('3000')
        self.find_element(*self.locator.OPPV_2).send_keys('20000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_2_TO_PAY).send_keys('2000')
        self.find_element(*self.locator.OPPV_3).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_3_TO_PAY).send_keys('1000')
        self.find_element(*self.locator.OPPV_4).send_keys('40000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_4_TO_PAY).send_keys('4000')
        self.find_element(*self.locator.OPPV_5).send_keys('50000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_5_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OPPV_6).send_keys('60000')
        sleep(0.3)
        self.find_element(*self.locator.OPPV_6_TO_PAY).send_keys('6000')
        sleep(0.5)
        assert '210000' in self.browser.page_source
        assert '21000' in self.browser.page_source
        self.scroll('3400')

    def osms1(self):
        self.find_element(*self.locator.OSMS_1).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_1_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OSMS_2).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_2_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OSMS_3).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_3_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OSMS_4).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_4_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OSMS_5).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_5_TO_PAY).send_keys('5000')
        self.find_element(*self.locator.OSMS_6).send_keys('10000')
        sleep(0.3)
        self.find_element(*self.locator.OSMS_6_TO_PAY).send_keys('5000')
        sleep(0.5)
        assert '60000' in self.browser.page_source
        assert '30000' in self.browser.page_source
        self.scroll('3700')

    def after4(self):
        self.find_element(*self.locator.AFTER_BUTTON).click()
        sleep(1)

    def fourth_page(self):
        self.inp()
        self.inp2()
        self.fl_income()
        self.opv1()
        self.oppv1()
        self.osms1()
        self.after4()

    def check_without_filling_og_code(self):
        sleep(1)
        assert 'Обязательное поле' in self.browser.page_source
        self.scroll('700')
        self.browser.find_element_by_xpath('//button[@disabled]')

    def OGD(self):
        self.browser.execute_script('window.scroll(0, -700)')
        sleep(1)
        self.find_element(*self.locator.CODE).click()
        self.find_element(*self.locator.SELECT_0301).click()

    def checkbox(self):
        self.browser.execute_script('window.scroll(0, 500)')
        self.find_element(*self.locator.ACCEPT_CHECKBOX_FNO).click()

    def final(self):
        sleep(15)
        self.find_element(*self.locator.FORM)
        assert '910.00 Упрощенная декларация для субъектов" " малого бизнеса'
        sleep(15)

    def sending_page(self):
        self.check_without_filling_og_code()
        #self.OGD()
        self.checkbox()
        self.final()

        '''first_page_with_annexes_to_tax_reporting'''

