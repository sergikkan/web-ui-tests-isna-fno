from browser_interaction import BasePage
from time import sleep
from locators.fno_910_page_locators import FNO910Locators
from locators.main_page_locators import MainPageLocators
from locators.fno_910_page_locators import FNO910LocatorsName as N


class FNO910MaxSymbolAnd0ValueCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO910Locators

        '''Ниже первая страница'''

    def first_page(self):
        self.find_element(*self.locator.TIS_CHECKBOX).click()
        self.scroll('500')
        self.find_element(*self.locator.TIS_NAME_INPUT).send_keys('Test45symbolsTestsymbolssymbolsBolsSymbol'
                                                                  'sSymbolsTestTESTTest Test ISNA autotest IA')
        assert 'Test45symbolsTestsymbolssymbolsBolsSymbolsSymbolsTestTESTTest Test ISNA autotest IA' not in \
               self.browser.page_source
        self.find_element(*self.locator.TIS_CARD_NUMBER_INPUT).send_keys('5463215784678543675432345673456')
        assert '5463215784678543675432345673456' not in self.browser.page_source
        self.scroll_900_px()
        #self.find_element(*self.locator.TIS_STOCK_BEGINNING_TAX_PERIOD).send_keys('1111111111111')
        #assert '1111111111111' not in self.browser.page_source
        #self.find_element(*self.locator.TIS_STOCK_ENDING_TAX_PERIOD).send_keys('1111111111111')
        #assert '1111111111111' not in self.browser.page_source
        self.find_element(*self.locator.AFTER_BUTTON).click()
        '''Ниже вторая страница'''

    def income_with_cash_and_cashless(self):
        # 910.00.001 Доход
        self.max_symbol_12_input(*self.locator.A_INPUT_INCOME_CASHLESS, name=N.A_INPUT_INCOME_CASHLESS)
        self.check_zero_value_input(*self.locator.A_INPUT_INCOME_CASHLESS, name=N.A_INPUT_INCOME_CASHLESS)
        self.check_letter_input(*self.locator.A_INPUT_INCOME_CASHLESS, name=N.A_INPUT_INCOME_CASHLESS)
        self.check_special_symbol_input(*self.locator.A_INPUT_INCOME_CASHLESS, name=N.A_INPUT_INCOME_CASHLESS)

        self.max_symbol_12_input(*self.locator.B_INPUT_INCOME_CASHLESS, name=N.B_INPUT_INCOME_CASHLESS)
        self.check_zero_value_input(*self.locator.B_INPUT_INCOME_CASHLESS, name=N.B_INPUT_INCOME_CASHLESS)
        self.check_letter_input(*self.locator.B_INPUT_INCOME_CASHLESS, name=N.B_INPUT_INCOME_CASHLESS)
        self.check_special_symbol_input(*self.locator.B_INPUT_INCOME_CASHLESS, name=N.B_INPUT_INCOME_CASHLESS)

        self.max_symbol_12_input(*self.locator.A_I, name=N.A_I)
        self.check_zero_value_input(*self.locator.A_I, name=N.A_I)
        self.check_letter_input(*self.locator.A_I, name=N.A_I)
        self.check_special_symbol_input(*self.locator.A_I, name=N.A_I)

        self.max_symbol_12_input(*self.locator.B_I, name=N.B_I)
        self.check_zero_value_input(*self.locator.B_I, name=N.B_I)
        self.check_letter_input(*self.locator.B_I, name=N.B_I)
        self.check_special_symbol_input(*self.locator.B_I, name=N.B_I)

    def income_with_law(self):
        # 910.00.002 В том числе доход от корректировки в соответствии с Законом о трансфертном ценообразовании
        self.max_symbol_12_input(*self.locator.INCOME_WITH_LAW, name=N.INCOME_WITH_LAW)
        self.check_zero_value_input(*self.locator.INCOME_WITH_LAW, name=N.INCOME_WITH_LAW)
        self.check_letter_input(*self.locator.INCOME_WITH_LAW, name=N.INCOME_WITH_LAW)
        self.check_special_symbol_input(*self.locator.INCOME_WITH_LAW, name=N.INCOME_WITH_LAW)

    def employee(self):
        # 910.00.003 Среднесписочная численность работников, в том числе:
        self.max_symbol_3_input(*self.locator.EMPLOYEE_QUANTITY, name=N.EMPLOYEE_QUANTITY)
        self.check_zero_value_input(*self.locator.EMPLOYEE_QUANTITY, name=N.EMPLOYEE_QUANTITY)
        self.check_letter_input(*self.locator.EMPLOYEE_QUANTITY, name=N.EMPLOYEE_QUANTITY)
        self.check_special_symbol_input(*self.locator.EMPLOYEE_QUANTITY, name=N.EMPLOYEE_QUANTITY)

        self.max_symbol_3_input(*self.locator.PENSIONER_QUANTITY, name=N.PENSIONER_QUANTITY)
        self.check_zero_value_input(*self.locator.PENSIONER_QUANTITY, name=N.PENSIONER_QUANTITY)
        self.check_letter_input(*self.locator.PENSIONER_QUANTITY, name=N.PENSIONER_QUANTITY)
        self.check_special_symbol_input(*self.locator.PENSIONER_QUANTITY, name=N.PENSIONER_QUANTITY)

        self.max_symbol_3_input(*self.locator.INVALID_QUANTITY, name=N.INVALID_QUANTITY)
        self.check_zero_value_input(*self.locator.INVALID_QUANTITY, name=N.INVALID_QUANTITY)
        self.check_letter_input(*self.locator.INVALID_QUANTITY, name=N.INVALID_QUANTITY)
        self.check_special_symbol_input(*self.locator.INVALID_QUANTITY, name=N.INVALID_QUANTITY)

        self.find_element(*self.locator.AVERAGE_SALARY).send_keys('1234567890123')
        assert '1234567890123' not in self.browser.page_source

    def after_second_page(self):
        self.browser.execute_script('window.scroll(0, 1300)')
        self.after_button_click()

    def second_page_validation_test(self):
        self.income_with_cash_and_cashless()
        self.income_with_law()
        self.employee()
        self.after_second_page()

    def inp(self):
        self.max_symbol_12_input(*self.locator.IPN_1_MONTH)
        self.check_zero_value_input(*self.locator.IPN_1_MONTH)
        self.check_letter_input(*self.locator.IPN_1_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_1_MONTH)

        self.max_symbol_12_input(*self.locator.IPN_2_MONTH)
        self.check_zero_value_input(*self.locator.IPN_2_MONTH)
        self.check_letter_input(*self.locator.IPN_2_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_2_MONTH)

        self.max_symbol_12_input(*self.locator.IPN_3_MONTH)
        self.check_zero_value_input(*self.locator.IPN_3_MONTH)
        self.check_letter_input(*self.locator.IPN_3_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_3_MONTH)

        self.max_symbol_12_input(*self.locator.IPN_4_MONTH)
        self.check_zero_value_input(*self.locator.IPN_4_MONTH)
        self.check_letter_input(*self.locator.IPN_4_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_4_MONTH)

        self.max_symbol_12_input(*self.locator.IPN_5_MONTH)
        self.check_zero_value_input(*self.locator.IPN_5_MONTH)
        self.check_letter_input(*self.locator.IPN_5_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_5_MONTH)

        self.max_symbol_12_input(*self.locator.IPN_6_MONTH)
        self.check_zero_value_input(*self.locator.IPN_6_MONTH)
        self.check_letter_input(*self.locator.IPN_6_MONTH)
        self.check_special_symbol_input(*self.locator.IPN_6_MONTH)

        self.browser.execute_script('window.scroll(0,1000)')

    def inp2(self):
        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_1)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_1)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_1)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_1)

        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_2)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_2)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_2)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_2)

        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_3)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_3)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_3)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_3)

        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_4)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_4)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_4)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_4)

        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_5)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_5)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_5)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_5)

        self.max_symbol_12_input(*self.locator.IPN_NO_RESIDENT_6)
        self.check_zero_value_input(*self.locator.IPN_NO_RESIDENT_6)
        self.check_letter_input(*self.locator.IPN_NO_RESIDENT_6)
        self.check_special_symbol_input(*self.locator.IPN_NO_RESIDENT_6)

        self.browser.execute_script('window.scroll(0, 1300)')

    def fl_income(self):
        self.max_symbol_12_input(*self.locator.FL_INCOME_1)
        self.check_zero_value_input(*self.locator.FL_INCOME_1)
        self.check_letter_input(*self.locator.FL_INCOME_1)
        self.check_special_symbol_input(*self.locator.FL_INCOME_1)

        self.max_symbol_12_input(*self.locator.FL_INCOME_2)
        self.check_zero_value_input(*self.locator.FL_INCOME_2)
        self.check_letter_input(*self.locator.FL_INCOME_2)
        self.check_special_symbol_input(*self.locator.FL_INCOME_2)

        self.max_symbol_12_input(*self.locator.FL_INCOME_3)
        self.check_zero_value_input(*self.locator.FL_INCOME_3)
        self.check_letter_input(*self.locator.FL_INCOME_3)
        self.check_special_symbol_input(*self.locator.FL_INCOME_3)

        self.max_symbol_12_input(*self.locator.FL_INCOME_4)
        self.check_zero_value_input(*self.locator.FL_INCOME_4)
        self.check_letter_input(*self.locator.FL_INCOME_4)
        self.check_special_symbol_input(*self.locator.FL_INCOME_4)

        self.max_symbol_12_input(*self.locator.FL_INCOME_5)
        self.check_zero_value_input(*self.locator.FL_INCOME_5)
        self.check_letter_input(*self.locator.FL_INCOME_5)
        self.check_special_symbol_input(*self.locator.FL_INCOME_5)

        self.max_symbol_12_input(*self.locator.FL_INCOME_6)
        self.check_zero_value_input(*self.locator.FL_INCOME_6)
        self.check_letter_input(*self.locator.FL_INCOME_6)
        self.check_special_symbol_input(*self.locator.FL_INCOME_6)

        self.browser.execute_script('window.scroll(0, 2000)')

    def opv1(self):
        self.max_symbol_12_input(*self.locator.OPV_1)
        self.check_zero_value_input(*self.locator.OPV_1)
        self.check_letter_input(*self.locator.OPV_1)
        self.check_special_symbol_input(*self.locator.OPV_1)

        self.max_symbol_12_input(*self.locator.OPV_2)
        self.check_zero_value_input(*self.locator.OPV_2)
        self.check_letter_input(*self.locator.OPV_2)
        self.check_special_symbol_input(*self.locator.OPV_2)

        self.max_symbol_12_input(*self.locator.OPV_3)
        self.check_zero_value_input(*self.locator.OPV_3)
        self.check_letter_input(*self.locator.OPV_3)
        self.check_special_symbol_input(*self.locator.OPV_3)

        self.max_symbol_12_input(*self.locator.OPV_4)
        self.check_zero_value_input(*self.locator.OPV_4)
        self.check_letter_input(*self.locator.OPV_4)
        self.check_special_symbol_input(*self.locator.OPV_4)

        self.max_symbol_12_input(*self.locator.OPV_5)
        self.check_zero_value_input(*self.locator.OPV_5)
        self.check_letter_input(*self.locator.OPV_5)
        self.check_special_symbol_input(*self.locator.OPV_5)

        self.max_symbol_12_input(*self.locator.OPV_6)
        self.check_zero_value_input(*self.locator.OPV_6)
        self.check_letter_input(*self.locator.OPV_6)
        self.check_special_symbol_input(*self.locator.OPV_6)

        self.browser.execute_script('window.scroll(0, 2700)')

    def oppv1(self):
        self.max_symbol_12_input(*self.locator.OPPV_1)
        self.check_zero_value_input(*self.locator.OPPV_1)
        self.check_letter_input(*self.locator.OPPV_1)
        self.check_special_symbol_input(*self.locator.OPPV_1)

        self.max_symbol_12_input(*self.locator.OPPV_2)
        self.check_zero_value_input(*self.locator.OPPV_2)
        self.check_letter_input(*self.locator.OPPV_2)
        self.check_special_symbol_input(*self.locator.OPPV_2)

        self.max_symbol_12_input(*self.locator.OPPV_3)
        self.check_zero_value_input(*self.locator.OPPV_3)
        self.check_letter_input(*self.locator.OPPV_3)
        self.check_special_symbol_input(*self.locator.OPPV_3)

        self.max_symbol_12_input(*self.locator.OPPV_4)
        self.check_zero_value_input(*self.locator.OPPV_4)
        self.check_letter_input(*self.locator.OPPV_4)
        self.check_special_symbol_input(*self.locator.OPPV_4)

        self.max_symbol_12_input(*self.locator.OPPV_5)
        self.check_zero_value_input(*self.locator.OPPV_5)
        self.check_letter_input(*self.locator.OPPV_5)
        self.check_special_symbol_input(*self.locator.OPPV_5)

        self.max_symbol_12_input(*self.locator.OPPV_6)
        self.check_zero_value_input(*self.locator.OPPV_6)
        self.check_letter_input(*self.locator.OPPV_6)
        self.check_special_symbol_input(*self.locator.OPPV_6)

        self.browser.execute_script('window.scroll(0, 3400)')

    def osms1(self):
        self.max_symbol_12_input(*self.locator.OSMS_1)
        self.check_zero_value_input(*self.locator.OSMS_1)
        self.check_letter_input(*self.locator.OSMS_1)
        self.check_special_symbol_input(*self.locator.OSMS_1)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_1_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_1_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_1_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_1_TO_PAY)

        self.max_symbol_12_input(*self.locator.OSMS_2)
        self.check_zero_value_input(*self.locator.OSMS_2)
        self.check_letter_input(*self.locator.OSMS_2)
        self.check_special_symbol_input(*self.locator.OSMS_2)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_2_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_2_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_2_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_2_TO_PAY)

        self.max_symbol_12_input(*self.locator.OSMS_3)
        self.check_zero_value_input(*self.locator.OSMS_3)
        self.check_letter_input(*self.locator.OSMS_3)
        self.check_special_symbol_input(*self.locator.OSMS_3)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_3_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_3_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_3_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_3_TO_PAY)

        self.max_symbol_12_input(*self.locator.OSMS_3)
        self.check_zero_value_input(*self.locator.OSMS_3)
        self.check_letter_input(*self.locator.OSMS_3)
        self.check_special_symbol_input(*self.locator.OSMS_3)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_4)
        self.check_zero_value_input(*self.locator.OSMS_4)
        self.check_letter_input(*self.locator.OSMS_4)
        self.check_special_symbol_input(*self.locator.OSMS_4)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_4_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_4_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_4_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_4_TO_PAY)

        self.max_symbol_12_input(*self.locator.OSMS_5)
        self.check_zero_value_input(*self.locator.OSMS_5)
        self.check_letter_input(*self.locator.OSMS_5)
        self.check_special_symbol_input(*self.locator.OSMS_5)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_5_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_5_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_5_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_5_TO_PAY)

        self.max_symbol_12_input(*self.locator.OSMS_5)
        self.check_zero_value_input(*self.locator.OSMS_5)
        self.check_letter_input(*self.locator.OSMS_5)
        self.check_special_symbol_input(*self.locator.OSMS_5)
        sleep(0.5)
        self.max_symbol_12_input(*self.locator.OSMS_6_TO_PAY)
        self.check_zero_value_input(*self.locator.OSMS_6_TO_PAY)
        self.check_letter_input(*self.locator.OSMS_6_TO_PAY)
        self.check_special_symbol_input(*self.locator.OSMS_6_TO_PAY)
        self.browser.execute_script('window.scroll(0, 3700)')
        sleep(1)

    def after4(self):
        self.after_button_click()
        sleep(1)
        self.scroll_900_px()
        self.check_without_filling_ogd_code()

    def third_page_validation_test(self):
        self.inp()
        self.inp2()
        self.fl_income()
        self.opv1()
        self.oppv1()
        self.osms1()
        self.after4()


class FNO910WithDescription(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO910Locators
        self.main_locator = MainPageLocators

    def currency_test_not_tenge(self):
        self.declaration_type_additional_with_notification_second()
        self.scroll_500_px()
        self.find_element(*self.locator.CURRENCY_TYPE).click()
        self.find_element(*self.locator.TALA_SELECT).click()
        self.browser.find_element_by_xpath('//input[@placeholder="WST"]')

    def test_income_with_no_tenge(self):
        self.browser.execute_script('window.scroll(0, 1000)')
        self.find_element(*self.locator.AFTER_BUTTON).click()
        sleep(0.5)
        assert 'WST' in self.browser.page_source
        self.find_element(*self.locator.A_INPUT_INCOME_CASHLESS).send_keys('100000000000')
        assert 'Доход за налоговый период превышает установленный показатель для специального' \
               ' налогового режима (24 038 МРП на 1 января соответствующего ' \
               'финансового года)!' not in self.browser.page_source

    def currency_decsription_test_with_no_tenge(self):
        self.currency_test_not_tenge()
        self.test_income_with_no_tenge()

    def return_to_first_page(self):
        self.hover(*self.main_locator.ACTIVATE_SLIDER)
        self.find_element(*self.main_locator.FIRST_PAGE).click()
        self.browser.refresh()
        sleep(2)
        assert 'Тала' not in self.browser.page_source
        assert 'Тенге' in self.browser.page_source

    def assert_required_field(self):
        self.browser.find_element_by_xpath("//*[contains(.,'Обязательное поле')]")
        self.browser.find_element_by_xpath('//span[text()= "*"]')

    def tis_description_test(self):
        self.find_element(*self.locator.TIS_CHECKBOX).click()
        self.browser.execute_script('window.scroll(0, 500)')
        self.find_element(*self.locator.TIS_NAME_INPUT).send_keys('Test')
        assert 'Наименование ТИС' in self.browser.page_source
        assert 'Номер регистрационной карточки' in self.browser.page_source
        assert 'Дата постановки на учет' in self.browser.page_source

    def continue_two_page(self):
        self.browser.execute_script('window.scroll(0, 1200)')
        self.find_element(*self.locator.AFTER_BUTTON).click()
        self.browser.find_element_by_xpath('//*[@data-icon="close"]')

    def check_description_second_page(self):

        # 910.00.001 Доход
        self.find_element(*self.locator.A_INPUT_INCOME_CASHLESS).send_keys('100000000000')
        self.browser.find_element_by_xpath("//*[contains(.,'Доход за налоговый период превышает установленный показате"
                                           "ль для специального налогового режима с применением ТИС (24 038 МРП + 70"
                                           " 048 МРП на 1 января соответствующего финансового года)!')]")
        sleep(0.5)
        assert 'Доход за налоговый период превышает установленный показатель для специального' \
               ' налогового режима (24 038 МРП на 1 января соответствующего финансового года)!' not \
               in self.browser.page_source
        self.find_element(*self.locator.A_INPUT_INCOME_CASHLESS).clear()
        self.find_element(*self.locator.A_I).send_keys('1000000')
        sleep(0.3)
        assert 'Значение поля A I не должно превышать значение поля А' in self.browser.page_source

        # 910.00.003 Среднесписочная численность работников, в том числе:
        self.find_element(*self.locator.EMPLOYEE_QUANTITY).send_keys('10')
        self.find_element(*self.locator.PENSIONER_QUANTITY).send_keys('11')
        self.find_element(*self.locator.INVALID_QUANTITY).send_keys('12')
        self.browser.find_element_by_xpath("//*[contains(.,'Количество пенсионеров и инвалидов не должно превышать "
                                           "среднесписочную численность работников')]")
        self.find_element(*self.locator.SALARY).is_displayed()
        self.find_element(*self.locator.EMPLOYEE_QUANTITY).clear()
        self.find_element(*self.locator.PENSIONER_QUANTITY).clear()
        self.find_element(*self.locator.INVALID_QUANTITY).clear()
        sleep(0.5)
        assert '910.00.004 Среднемесячная заработная плата на одного работника*' not in self.browser.page_source
        self.browser.execute_script('window.scroll(0, 1300)')
