from locators.fno_400_locators import FNO_400_01Locators, FNO_400_02Locators, FNO_400_03Locators, FNO_400_04Locators \
    , FNO_400_05Locators, FNO_400_06Locators, FNO_400_07Locators, FNO_400_08Locators
from browser_interaction import BasePage
import allure
from time import sleep


class FNO400Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO_400_01Locators
        self.locator02 = FNO_400_02Locators
        self.locator03 = FNO_400_03Locators
        self.locator04 = FNO_400_04Locators
        self.locator05 = FNO_400_05Locators
        self.locator06 = FNO_400_06Locators
        self.locator07 = FNO_400_07Locators
        self.locator08 = FNO_400_08Locators

    def check_tax_period_text(self):
        try:
            assert '400.00 Декларация по акцизу' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО400
    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.MONTH).click()
        self.find_element(*self.locator.MONTH_SELECT).click()
        self.find_element(*self.locator.YEAR).click()
        sleep(0.5)
        self.find_element(*self.locator.YEAR_SELECT).click()
        sleep(2)
        self.find_element(*self.locator.SEND_DOC).click()

    # Ниже первая страница
    # Заполнение информации о декларации
    def declaration_info(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.DECLARATION_TYPE).click()

    # Заполнение информации о налогоплательщике
    def taxpayer_info(self):
        self.scroll('500')
        self.find_element(*self.locator.TAXPAYER_CATEGORY).click()
        self.find_element(*self.locator.TAXPAYER_CATEGORY_SELECT).click()

    # Представленные приложения и нажатие на 421.00
    def annexes_and_confirm(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(0.3)
        self.find_element(*self.locator.ANNEXES_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_2(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(0.3)
        self.find_element(*self.locator.ANNEXES_SELECT2).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_3(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(0.3)
        self.find_element(*self.locator.ANNEXES_SELECT3).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_4(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(0.3)
        self.find_element(*self.locator.ANNEXES_SELECT4).click()
        sleep(0.3)
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_5(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(0.3)
        element = self.browser.find_element_by_xpath('//*[@title="Приложение 400.08  Облагаемые операции по '
                                                     'подакцизным товарам, предусмотренным подпунктом 6) статьи 462 '
                                                     'Налогового кодекса"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.ANNEXES_SELECT5).click()
        sleep(1)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        sleep(0.3)
        #self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_6(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(1)
        element = self.browser.find_element_by_xpath('//*[@title="Приложение 400.08  Облагаемые операции по '
                                                     'подакцизным товарам, предусмотренным подпунктом 6) статьи 462 '
                                                     'Налогового кодекса"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.ANNEXES_SELECT6).click()
        sleep(0.5)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        #self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_7(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(1)
        element = self.browser.find_element_by_xpath('//*[@title="Приложение 400.08  Облагаемые операции по '
                                                     'подакцизным товарам, предусмотренным подпунктом 6) статьи 462 '
                                                     'Налогового кодекса"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.ANNEXES_SELECT7).click()
        sleep(0.5)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        #self.find_element(*self.locator.CONFIRM).click()

    def annexes_and_confirm_8(self):
        self.find_element(*self.locator.ANNEXES).click()
        sleep(1)
        element = self.browser.find_element_by_xpath('//*[@title="Приложение 400.08  Облагаемые операции по '
                                                     'подакцизным товарам, предусмотренным подпунктом 6) статьи 462 '
                                                     'Налогового кодекса"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.ANNEXES_SELECT8).click()
        sleep(0.5)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        #self.find_element(*self.locator.CONFIRM).click()

    # Пэйджи для перехода на разные приложения
    def first_page_002(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_2()
        self.after_first_page()

    def first_page_003(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_3()
        self.after_first_page()

    def first_page_004(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_4()
        self.after_first_page()

    def first_page_005(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_5()
        self.after_first_page()

    def first_page_006(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_6()
        self.after_first_page()

    def first_page_007(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_7()
        self.after_first_page()

    def first_page_008(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm_8()
        self.after_first_page()

    # Переход на следующую
    def after_first_page(self):
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def first_page(self):
        self.declaration_info()
        self.taxpayer_info()
        self.annexes_and_confirm()
        self.after_first_page()

    # 2 страница
    # 401.01.001
    def type_and_code(self):
        self.find_element(*self.locator.PRODUCT_TYPE).send_keys('Спиртные напитки')
        sleep(1)
        self.find_element(*self.locator.QUALIFICATION_CODE).click()
        self.find_element(*self.locator.QUALIFICATION_CODE_SELECT).click()
        self.scroll('500')

    def operations(self):
        sleep(0.5)
        self.find_element(*self.locator.BUT_1).send_keys('10')
        sleep(0.5)
        self.find_element(*self.locator.BUT_2).send_keys('100')
        sleep(0.5)
        assert '1000' in self.browser.page_source
        self.find_element(*self.locator.BUT_3).send_keys('2000')
        sleep(0.5)
        self.find_element(*self.locator.BUT_4).send_keys('300')
        sleep(0.5)
        assert '600000' in self.browser.page_source
        self.find_element(*self.locator.BUT_5).send_keys('3000')
        sleep(0.5)
        self.find_element(*self.locator.BUT_6).send_keys('600')
        sleep(0.5)
        assert '1800000' in self.browser.page_source
        self.find_element(*self.locator.BUT_7).send_keys('8000')
        sleep(0.5)
        self.find_element(*self.locator.BUT_8).send_keys('900')
        sleep(0.5)
        assert '7200000' in self.browser.page_source
        self.find_element(*self.locator.BUT_9).send_keys('4000')
        sleep(0.5)
        self.find_element(*self.locator.BUT_10).send_keys('60')
        sleep(0.5)
        assert '240000' in self.browser.page_source
        self.find_element(*self.locator.BUT_11).send_keys('1100')
        sleep(0.5)
        self.find_element(*self.locator.BUT_12).send_keys('140')
        sleep(0.5)
        assert '154000' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.BUT_13).send_keys('1030')
        sleep(0.5)
        self.find_element(*self.locator.BUT_14).send_keys('130')
        sleep(0.5)
        assert '133900' in self.browser.page_source
        self.find_element(*self.locator.BUT_15).send_keys('140')
        sleep(0.5)
        self.find_element(*self.locator.BUT_16).send_keys('180')
        sleep(0.5)
        assert '25200' in self.browser.page_source
        self.find_element(*self.locator.BUT_17).send_keys('1680')
        sleep(0.5)
        self.find_element(*self.locator.BUT_18).send_keys('10')
        sleep(0.5)
        assert '16800' in self.browser.page_source
        self.find_element(*self.locator.BUT_19).send_keys('1540')
        sleep(0.5)
        self.find_element(*self.locator.BUT_20).send_keys('20')
        sleep(0.5)
        assert '30800' in self.browser.page_source
        self.find_element(*self.locator.BUT_21).send_keys('1350')
        sleep(0.5)
        self.find_element(*self.locator.BUT_22).send_keys('14')
        sleep(0.5)
        assert '18900' in self.browser.page_source
        self.find_element(*self.locator.BUT_23).send_keys('150')
        sleep(0.5)
        self.find_element(*self.locator.BUT_24).send_keys('140')
        sleep(0.5)
        assert '21000' in self.browser.page_source
        self.scroll('500')
        sleep(0.5)
        self.find_element(*self.locator.BUT_25).send_keys('50')
        self.find_element(*self.locator.AFTER).click()

    def second_page(self):
        self.type_and_code()
        self.operations()

    # 3 страница
    # Раздел. Исчислено акцизов к уплате
    def EXCISE_TO_PAY(self):
        sleep(0.5)
        self.scroll('700')
        self.find_element(*self.locator.BUTTON_TOTAL_8).send_keys('1000')
        sleep(0.5)
        self.scroll('500')
        self.find_element(*self.locator.BUTTON_TOTAL_12).send_keys('1000')
        sleep(0.5)
        self.scroll('500')


    def VALUES(self):
        self.scroll('500')
        self.find_element(*self.locator.VAL_1).send_keys('100')
        sleep(0.1)
        self.find_element(*self.locator.VAL_2).send_keys('200')
        sleep(0.1)
        self.find_element(*self.locator.VAL_3).send_keys('300')
        sleep(0.1)
        self.find_element(*self.locator.VAL_4).send_keys('400')
        sleep(0.1)
        self.find_element(*self.locator.VAL_5).send_keys('500')
        sleep(0.1)
        self.find_element(*self.locator.VAL_6).send_keys('600')
        sleep(0.1)
        self.find_element(*self.locator.VAL_7).send_keys('700')
        sleep(0.1)
        self.find_element(*self.locator.VAL_8).send_keys('800')
        sleep(0.1)
        self.scroll_500_px()
        self.find_element(*self.locator.VAL_9).send_keys('900')
        sleep(0.1)
        self.find_element(*self.locator.VAL_10).send_keys('110')
        sleep(0.1)
        self.find_element(*self.locator.VAL_11).send_keys('150')
        sleep(0.1)
        self.find_element(*self.locator.VAL_12).send_keys('170')
        sleep(0.1)
        self.scroll_500_px()
        self.find_element(*self.locator.VAL_13).send_keys('100')
        sleep(0.1)
        self.find_element(*self.locator.VAL_14).send_keys('180')
        sleep(2)
        self.scroll('1500')
        self.find_element(*self.locator.AFTER).click()

    def third_page(self):
        self.EXCISE_TO_PAY()
        self.VALUES()

    def fourth_page(self):
        sleep(1)
        self.find_element(*self.locator.CODE_OGD).click()
        sleep(1)
        self.find_element(*self.locator.CODE_OGD_SELECT).click()
        self.scroll_500_px()
        self.find_element(*self.locator.AFFIRMATION).click()
        sleep(2)
        self.find_element(*self.locator.FORM_DECLARATION).click()

    # 400.02

    def second_page_002(self):
        self.find_element(*self.locator02.ALC_TYPE).send_keys('Спирт')
        sleep(1)
        self.find_element(*self.locator02.QUAL_CODE).click()
        sleep(0.2)
        self.find_element(*self.locator02.QUAL_CODE_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator02.OP1).send_keys('15')
        sleep(0.2)
        self.find_element(*self.locator02.OP2).send_keys('10')
        sleep(0.2)
        self.find_element(*self.locator02.OP3).send_keys('20')
        sleep(0.2)
        self.find_element(*self.locator02.OP4).send_keys('150')
        sleep(0.2)
        self.find_element(*self.locator02.OP5).send_keys('50')
        sleep(0.2)
        self.find_element(*self.locator02.OP6).send_keys('15')
        sleep(0.2)
        self.find_element(*self.locator02.OP7).send_keys('10')
        sleep(0.2)
        self.find_element(*self.locator02.OP8).send_keys('20')
        sleep(0.2)
        self.scroll('500')
        self.find_element(*self.locator02.KM1).send_keys('80')
        sleep(0.2)
        self.find_element(*self.locator02.ET1).send_keys('25')
        sleep(0.3)
        assert '2000' in self.browser.page_source
        self.find_element(*self.locator02.KM2).send_keys('45')
        sleep(0.3)
        self.find_element(*self.locator02.ET2).send_keys('200')
        sleep(0.3)
        assert '9000' in self.browser.page_source
        self.find_element(*self.locator02.KM3).send_keys('130')
        sleep(0.3)
        self.find_element(*self.locator02.ET3).send_keys('210')
        sleep(0.3)
        assert '27300' in self.browser.page_source
        assert '38590' in self.browser.page_source
        self.find_element(*self.locator02.EXCISE_RATE).send_keys('10')
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def second_page_003(self):
        self.find_element(*self.locator03.TOBACCO_TYPE).send_keys('Коньяк')
        sleep(0.2)
        self.find_element(*self.locator03.BUDGET_CODE).click()
        self.find_element(*self.locator03.BUDGET_CODE_SELECT).click()
        self.scroll('500')
        self.find_element(*self.locator03.TOBACCO_OP1).send_keys('15')
        sleep(0.2)
        self.find_element(*self.locator03.TOBACCO_OP2).send_keys('10')
        sleep(0.2)
        self.find_element(*self.locator03.TOBACCO_OP3).send_keys('20')
        sleep(0.2)
        self.find_element(*self.locator03.TOBACCO_OP4).send_keys('25')
        sleep(0.2)
        self.find_element(*self.locator03.TOBACCO_OP5).send_keys('30')
        sleep(0.2)
        self.find_element(*self.locator03.TOBACCO_OP6).send_keys('40')
        sleep(0.2)
        self.find_element(*self.locator03.KAZ_REAL).send_keys('70')
        sleep(0.2)
        self.find_element(*self.locator03.EXPORT_REAL).send_keys('60')
        sleep(0.2)
        assert '130' in self.browser.page_source
        self.find_element(*self.locator03.TAX_CORRECT).send_keys('50')
        sleep(0.2)
        self.find_element(*self.locator03.DAMAGED).send_keys('30')
        sleep(0.2)
        self.scroll('500')
        self.find_element(*self.locator03.AMOUNT1).send_keys('30')
        sleep(0.2)
        self.find_element(*self.locator03.AMOUNT2).send_keys('35')
        sleep(0.2)
        assert '1050' in self.browser.page_source
        self.find_element(*self.locator03.AMOUNT3).send_keys('80')
        sleep(0.2)
        self.find_element(*self.locator03.AMOUNT4).send_keys('90')
        sleep(0.2)
        assert '7200' in self.browser.page_source
        self.scroll('500')
        sleep(0.2)
        self.find_element(*self.locator03.EXCISE_RATE).send_keys('10')
        sleep(0.2)
        self.find_element(*self.locator03.EXCISE_SUM).send_keys('20')
        sleep(2)
        self.find_element(*self.locator.AFTER).click()

    def second_page_004(self):
        self.find_element(*self.locator04.OIL_REAL).send_keys('10')
        self.find_element(*self.locator04.EXPORT_OIL1).send_keys('25')
        self.find_element(*self.locator04.EXPORT_OIL2).send_keys('30')
        sleep(0.5)
        assert '55' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator04.USING1).send_keys('40')
        self.find_element(*self.locator04.USING2).send_keys('35')
        self.find_element(*self.locator04.USING3).send_keys('27')
        self.find_element(*self.locator04.USING4).send_keys('70')
        self.find_element(*self.locator04.USING5).send_keys('80')
        self.find_element(*self.locator04.USING6).send_keys('95')
        self.find_element(*self.locator04.USING7).send_keys('60')
        self.find_element(*self.locator04.USING8).send_keys('55')
        sleep(0.2)
        assert '527' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator04.TON_RATE).send_keys('5O')
        self.find_element(*self.locator.AFTER).click()

    def second_page_005(self):
        self.scroll('500')
        self.find_element(*self.locator05.OPT_1).send_keys('5')
        self.find_element(*self.locator05.OPT_2).send_keys('100')
        assert '500' in self.browser.page_source
        self.find_element(*self.locator05.OPT_3).send_keys('55')
        self.find_element(*self.locator05.OPT_4).send_keys('20')
        sleep(0.2)
        assert '1100' in self.browser.page_source
        self.find_element(*self.locator05.OPT_5).send_keys('35')
        self.find_element(*self.locator05.OPT_6).send_keys('30')
        sleep(0.5)
        assert '1050' in self.browser.page_source
        self.find_element(*self.locator05.OPT_7).send_keys('15')
        self.find_element(*self.locator05.OPT_8).send_keys('40')
        sleep(0.2)
        assert '600' in self.browser.page_source
        self.scroll('700')
        self.find_element(*self.locator05.OPT_9).send_keys('8O')
        self.find_element(*self.locator05.OPT_10).send_keys('1O')
        sleep(0.2)
        assert '800' in self.browser.page_source
        self.scroll('300')
        self.find_element(*self.locator05.ROZN_1).send_keys('1O0')
        self.find_element(*self.locator05.ROZN_2).send_keys('2')
        sleep(0.2)
        assert '200' in self.browser.page_source
        self.find_element(*self.locator05.ROZN_3).send_keys('2O0')
        self.find_element(*self.locator05.ROZN_4).send_keys('10')
        sleep(0.2)
        assert '2000' in self.browser.page_source
        self.find_element(*self.locator05.ROZN_5).send_keys('300')
        self.find_element(*self.locator05.ROZN_6).send_keys('5')
        sleep(0.2)
        assert '1500' in self.browser.page_source
        self.find_element(*self.locator05.ROZN_7).send_keys('6O0')
        self.find_element(*self.locator05.ROZN_8).send_keys('4')
        sleep(0.2)
        assert '240' in self.browser.page_source
        self.scroll('700')
        self.find_element(*self.locator05.ROZN_9).send_keys('20')
        self.find_element(*self.locator05.ROZN_10).send_keys('5')
        sleep(0.2)
        assert '100' in self.browser.page_source
        self.find_element(*self.locator05.ROZN_11).send_keys('60')
        self.find_element(*self.locator05.ROZN_12).send_keys('7')
        sleep(0.2)
        assert '420' in self.browser.page_source
        self.find_element(*self.locator05.ROZN_13).send_keys('30')
        self.find_element(*self.locator05.ROZN_14).send_keys('20')
        sleep(0.2)
        assert '600' in self.browser.page_source
        self.scroll('800')
        self.find_element(*self.locator05.DOPT_1).send_keys('200')
        self.find_element(*self.locator05.DOPT_2).send_keys('10')
        self.find_element(*self.locator05.DOPT_3).send_keys('30')
        self.find_element(*self.locator05.DOPT_4).send_keys('40')
        self.find_element(*self.locator05.DOPT_5).send_keys('50')
        self.find_element(*self.locator05.DOPT_6).send_keys('60')
        self.find_element(*self.locator05.DOPT_7).send_keys('70')
        self.find_element(*self.locator05.DOPT_8).send_keys('90')
        self.scroll('700')
        self.find_element(*self.locator05.DOPT_9).send_keys('45')
        self.find_element(*self.locator05.DOPT_10).send_keys('70')
        self.find_element(*self.locator05.DROZ_1).send_keys('50')
        self.find_element(*self.locator05.DROZ_2).send_keys('10')
        self.find_element(*self.locator05.DROZ_3).send_keys('30')
        self.find_element(*self.locator05.DROZ_4).send_keys('20')
        self.scroll('600')
        self.find_element(*self.locator05.DROZ_5).send_keys('45')
        self.find_element(*self.locator05.DROZ_6).send_keys('40')
        self.find_element(*self.locator05.DROZ_7).send_keys('30')
        self.find_element(*self.locator05.DROZ_8).send_keys('20')
        self.find_element(*self.locator05.DROZ_9).send_keys('15')
        self.find_element(*self.locator05.DROZ_10).send_keys('60')
        self.find_element(*self.locator05.DROZ_11).send_keys('70')
        self.find_element(*self.locator05.DROZ_12).send_keys('50')
        self.scroll('200')
        self.find_element(*self.locator05.DROZ_13).send_keys('60')
        self.find_element(*self.locator05.DROZ_14).send_keys('80')
        self.scroll('800')
        self.find_element(*self.locator05.EXC_PAY1).click()
        sleep(0.2)
        self.find_element(*self.locator05.EXC_PAY).click()
        self.find_element(*self.locator05.EXC_PAY2).send_keys('10')
        self.scroll('2000')
        self.find_element(*self.locator.AFTER).click()

    def second_page_006(self):
        self.scroll('500')
        self.find_element(*self.locator06.ADD_STR).click()
        self.find_element(*self.locator06.QUAL_CODE).click()
        self.find_element(*self.locator06.QUAL_CODE_SELECT).click()
        self.find_element(*self.locator06.USED_MATERIALS).send_keys('5')
        self.find_element(*self.locator06.EXCISE_RATE).send_keys('20')
        self.find_element(*self.locator06.DEDUCTION_AMOUNT).send_keys('3')
        self.find_element(*self.locator06.ADD).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def second_page_007(self):
        self.scroll('500')
        self.find_element(*self.locator07.EXCISE_NO1).send_keys('2')
        self.find_element(*self.locator07.EXCISE_NO2).send_keys('10')
        self.find_element(*self.locator07.EXCISE_NO3).send_keys('3')
        self.find_element(*self.locator07.EXCISE_NO4).send_keys('2')
        self.find_element(*self.locator07.EXCISE_NO5).send_keys('50')
        self.find_element(*self.locator07.EXCISE_NO6).send_keys('1')
        self.find_element(*self.locator07.EXCISE_NO7).send_keys('25')
        self.find_element(*self.locator07.EXCISE_NO8).send_keys('4')
        self.scroll('700')
        self.find_element(*self.locator07.EXCISE_NO9).send_keys('2')
        self.find_element(*self.locator07.EXCISE_NO10).send_keys('16')
        self.find_element(*self.locator07.EXCISE_NO11).send_keys('1')
        self.find_element(*self.locator07.EXCISE_NO12).send_keys('7')
        self.find_element(*self.locator07.EXCISE_NO13).send_keys('2')
        self.find_element(*self.locator07.EXCISE_NO14).send_keys('3')
        self.find_element(*self.locator07.EXCISE_NO15).send_keys('9')
        self.find_element(*self.locator07.EXCISE_NO16).send_keys('5')
        self.scroll('800')
        self.find_element(*self.locator07.EXCISE_NO17).send_keys('5')
        self.find_element(*self.locator07.EXCISE_NO18).send_keys('2')
        self.find_element(*self.locator07.EXCISE_NO19).send_keys('4')
        self.find_element(*self.locator07.EXCISE_NO20).send_keys('10')
        self.find_element(*self.locator07.EXCISE_NO21).send_keys('3')
        self.find_element(*self.locator07.EXCISE_NO22).send_keys('1')
        self.find_element(*self.locator07.EXCISE_NO23).send_keys('8')
        self.find_element(*self.locator07.EXCISE_NO24).send_keys('2')
        self.scroll('850')
        self.find_element(*self.locator07.EXCISE_NO25).send_keys('9')
        sleep(0.2)
        self.find_element(*self.locator07.EXCISE_NO26).send_keys('5')
        sleep(0.2)
        self.find_element(*self.locator07.ALC_1).send_keys('3')
        sleep(0.2)
        self.find_element(*self.locator07.ALC_2).send_keys('20')
        sleep(0.2)
        self.find_element(*self.locator07.ALC_3).send_keys('50')
        sleep(0.2)
        self.find_element(*self.locator07.ALC_4).send_keys('2')
        sleep(0.2)
        self.find_element(*self.locator.AFTER).click()

    def second_page_008(self):
        self.scroll('300')
        self.find_element(*self.locator08.OPER1).send_keys('4')
        sleep(0.2)
        self.find_element(*self.locator08.OPER2).send_keys('3')
        sleep(0.2)
        self.find_element(*self.locator08.OPER3).send_keys('2')
        sleep(0.2)
        self.find_element(*self.locator08.OPER4).send_keys('1')
        sleep(0.2)
        self.find_element(*self.locator08.OPER5).send_keys('5')
        sleep(0.2)
        self.find_element(*self.locator08.OPER6).send_keys('10')
        sleep(0.2)
        self.find_element(*self.locator08.OPER7).send_keys('15')
        sleep(0.2)
        self.find_element(*self.locator08.OPER8).send_keys('4')
        sleep(0.2)
        self.scroll('500')
        self.find_element(*self.locator08.OPER10).send_keys('7')
        self.find_element(*self.locator.AFTER).click()
