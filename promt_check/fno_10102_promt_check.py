from locators.fno_10102_locators import FNO10102locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
import allure


class PromtFNO1002(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO10102locators
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
        self.scroll_500_px()
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
        self.after_button_click()

    def second_page_with_first_option_promt_check(self):
        self.hover(*self.locator.KNP_BEFORE)
        assert 'В строке 101.02.001 определяется за предыдущий налоговый период сумма КПН, по формуле' \
               ' 101.02.001 I + 101.02.001 II'
        self.hover(*self.locator.FIRST_PARAPGRAPH_INPUT)
        assert 'В строке 101.02.001 I указывается сумма КПН, исчисленная за предыдущий налоговый период в ' \
               'соответствии с п.1 ст. 302 НК' in self.browser.page_source
        self.hover(*self.locator.SECOND_PARAPGRAPH_INPUT)
        assert 'В строке 101.02.001 II указывается сумма КПН, исчисленная за предыдущий налоговый период в ' \
               'соответствии со ст. 652 НК на чистый доход.' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.ADVANCE_PAYMENT_3_5)
        assert 'В строке 101.02.002 указывается сумма АП по КПН, подлежащая уплате за период после сдачи декларации' \
               ' и определенная в размере трех четвертых от указанной в строке 101.02.001 суммы КПН ' \
               'за предыдущий налоговый период' in self.browser.page_source
        self.hover(*self.locator.ADVANCE_PAYMENT_MONTHLY)
        assert 'В строке 101.02.004 определяется сумма ежемесячного АП по КПН, подлежащая уплате за 2, 3 и 4 ' \
               'кварталы отчетного налогового периода.' in self.browser.page_source
        self.scroll('900')
        self.hover(*self.main_locator.ACTIVATE_SLIDER)
        self.find_element(*self.main_locator.FIRST_PAGE).click()
        self.scroll('700')
        self.find_element(*self.locator.SECOND_TAX_CODEX_CHECKBOX).click()
        self.find_element(*self.locator.AFTER_BUTTON_FIRST_PAGE).click()
        self.scroll('500')
        self.hover(*self.locator.SUPPOSED_SUM1)
        assert 'В строке 101.02.005 указывается сумма КПН, которая предположительно будет получена по итогам отчетного' \
               ' налогового периода при ее исчислении в соответствии с п.1 ст. 302 НК' in self.browser.page_source
        self.hover(*self.locator.SUPPOSED_SUM2)
        assert 'В строке 101.02.006 указывается сумма КПН, которая предположительно будет получена по итогам ' \
               'отчетного налогового периода при ее исчислении в соответствии со ст. 652 НК'
        self.hover(*self.locator.CALC_DECLARATION007)
        assert 'В строке 101.02.007 указывается сумма АП по КПН, подлежащая уплате после сдачи декларации,' \
               ' исчисленная как ' \
               '(101.02.005 + 101.02.006) х (3/4)' in self.browser.page_source
        self.hover(*self.locator.TOTAL_AVANCE_PAYMENT)
        assert 'В строке 101.02.009 указывается сумма ежемесячного АП по КПН, подлежащая уплате за 2, 3 и 4' \
               ' кварталы отчетного налогового периода' in self.browser.page_source



