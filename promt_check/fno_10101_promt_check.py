
from locators.fno_10101_locators import FNO1010locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
import allure



class FNO_10101_promt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO1010locators
        self.main_locator = MainPageLocators

    def activate_promt(self):
        with allure.step('Активация подсказок'):
            self.hover(*self.main_locator.PROMT)
            self.find_element(*self.main_locator.PROMT_ACTIVATE).click()
            allure.attach(self.browser.get_screenshot_as_png(), name='активация подсказок',
                          attachment_type=allure.attachment_type.PNG)

    def first_page_promt_check(self):
        self.hover(*self.locator.DECLARATION_TYPE_SELECT)
        sleep(0.1)
        assert 'Соответствующие ячейки отмечаются с учетом отнесения расчета до сдачи декларации к видам налоговой' \
               ' отчетности, указанным в ст. 206 НК' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.SEPERATE_CATEGORY)
        sleep(0.1)
        assert 'Ячейки отмечаются в случае, если НП относится к одной или нескольким категориям' in \
               self.browser.page_source
        self.hover(*self.locator.FIRST_TAX_CODEX_CHECKBOX)
        sleep(0.1)
        assert 'Заполняется если в предыдущем налоговом периоде исчисляли, и уплачивали авансовые' \
               ' платежи по КПН.' in self.browser.page_source
        self.hover(*self.locator.SECOND_TAX_CODEX_CHECKBOX)
        sleep(0.1)
        assert 'Заполняется если в предыдущем налоговом периоде не исчисляли, ' \
               'и не уплачивали авансовые платежи по КПН.' in self.browser.page_source
        self.hover(*self.locator.DECLARATION_TYPE_SELECT)

    def second_page_with_first_option(self):
        sleep(1)
        self.hover(*self.locator.TOTAL_ADVANCE_AMOUNT)
        sleep(0.1)
        assert 'В строке 101.01.001 указывается общая сумма АП по КПН, исчисленная НП в расчетах сумм ' \
               'АП за предыдущий налоговый период;' in self.browser.page_source
        self.hover(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION)
        sleep(0.1)
        assert 'В строке 101.01.002 указывается сумма АП по КПН, подлежащая уплате за период до сдачи декларации, ' \
               'определенная как одна четвертая от общей суммы АП, исчисленной в расчетах сумм АП за предыдущий ' \
               'налоговый период;' in self.browser.page_source

    def second_page_with_second_option(self):
        sleep(1)
        self.hover(*self.locator.EXPECTED_SUM)
        sleep(0.1)
        assert 'В 101.01.004 указывается сумма КПН, которая предположительно будет исчислена за отчетный налоговый ' \
               'период в соответствии с п. 1 ст. 302 НК' in self.browser.page_source
        self.hover(*self.locator.EXPECTED_SUM2)
        sleep(0.1)
        assert 'В строке 101.01.005 указывается сумма КПН, которая предположительно будет исчислена за отчетный' \
               ' налоговый период в соответствии со ст. 652 НК'
        self.scroll('500')
        self.hover(*self.locator.DECLINE_SUM1)
        sleep(0.1)
        self.hover(*self.locator.AVANCE_CALC_BEFORE_DEC)
        assert 'В строке 101.01.009 указывается ежемесячная сумма АП за январь, февраль, март месяцы налогового' \
               ' периода, определенная как (101.01.008/3);' in self.browser.page_source